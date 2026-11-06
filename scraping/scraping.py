"""
LeetCode Scraper - Data Collection untuk Tugas Text Mining
============================================================
Mengumpulkan daftar soal dari LeetCode (title, difficulty, category/topic tags)
beserta teks deskripsi tiap soal, lewat GraphQL API resmi yang dipakai
front-end leetcode.com sendiri (bukan scraping HTML biasa, karena halaman
problemset di-render lewat JavaScript).

Install dependency:
    pip install requests beautifulsoup4 pandas tqdm

Cara jalan:
    python leetcode_scraper.py

Output (tersimpan di folder yang sama):
    leetcode_problems_list.csv  -> metadata semua soal (id, title, slug,
                                   difficulty, category, is_paid_only)
    leetcode_raw_data.csv       -> metadata + teks deskripsi (raw_text),
                                   sudah dibersihkan dari tag HTML

Catatan:
- Soal berlabel "premium" (is_paid_only = True) TIDAK bisa diambil teksnya
  tanpa akun LeetCode Premium -> raw_text dikosongkan untuk soal ini.
- Script mendukung resume: kalau proses putus di tengah (misal koneksi
  error / rate limit), tinggal jalankan ulang, soal yang sudah diambil
  tidak akan diulang.
- Ada jeda (time.sleep) antar request supaya tidak kena rate-limit dari
  LeetCode. Untuk ~3000+ soal, proses pengambilan teks bisa makan waktu
  puluhan menit -- ini normal, biarkan berjalan.
"""

import os
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

GRAPHQL_URL = "https://leetcode.com/graphql/"

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/problemset/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
}

LIST_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      difficulty
      frontendQuestionId: questionFrontendId
      isPaidOnly
      title
      titleSlug
      topicTags {
        name
      }
    }
  }
}
"""

CONTENT_QUERY = """
query questionContent($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    content
  }
}
"""


def fetch_all_problems(page_size=100, pause=1.0):
    """Ambil daftar SEMUA soal (metadata saja) lewat pagination."""
    all_problems = []
    skip = 0
    total = None

    with tqdm(desc="Mengambil daftar soal") as pbar:
        while True:
            payload = {
                "query": LIST_QUERY,
                "variables": {
                    "categorySlug": "",
                    "skip": skip,
                    "limit": page_size,
                    "filters": {},
                },
                "operationName": "problemsetQuestionList",
            }
            resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=15)
            resp.raise_for_status()
            data = resp.json()["data"]["problemsetQuestionList"]

            if total is None:
                total = data["total"]
                pbar.total = total

            batch = data["questions"]
            if not batch:
                break

            all_problems.extend(batch)
            skip += len(batch)
            pbar.update(len(batch))

            if skip >= total:
                break
            time.sleep(pause)

    return all_problems


def clean_html(raw_html):
    """Buang tag HTML dari deskripsi soal, sisakan teks murni + rapikan spasi."""
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    text = soup.get_text(separator=" ")
    return " ".join(text.split())


def fetch_problem_content(slug):
    """Ambil deskripsi (content) satu soal berdasarkan slug-nya."""
    payload = {
        "query": CONTENT_QUERY,
        "variables": {"titleSlug": slug},
        "operationName": "questionContent",
    }
    resp = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    content = resp.json()["data"]["question"]["content"]
    return clean_html(content)


def main():
    list_csv = "leetcode_problems_list.csv"
    raw_csv = "leetcode_raw_data.csv"
    pause_between_content_calls = 0.5  # detik, jaga2 supaya tidak kena rate-limit

    # 1. Ambil daftar semua soal (metadata: title, difficulty, category)
    if os.path.exists(list_csv):
        print(f"Memuat daftar soal dari cache: {list_csv}")
        df_list = pd.read_csv(list_csv)
    else:
        problems = fetch_all_problems()
        df_list = pd.DataFrame(
            [
                {
                    "id": p["frontendQuestionId"],
                    "title": p["title"],
                    "slug": p["titleSlug"],
                    "difficulty": p["difficulty"],
                    "is_paid_only": p["isPaidOnly"],
                    "category": "; ".join(t["name"] for t in p["topicTags"]),
                }
                for p in problems
            ]
        )
        df_list.to_csv(list_csv, index=False)
        print(f"Tersimpan {len(df_list)} soal ke {list_csv}")

    # 2. Ambil teks deskripsi tiap soal (skip soal premium), dengan dukungan resume
    if os.path.exists(raw_csv):
        df_raw = pd.read_csv(raw_csv)
        done_slugs = set(df_raw["slug"])
    else:
        df_raw = pd.DataFrame(columns=list(df_list.columns) + ["raw_text"])
        done_slugs = set()

    rows_to_process = df_list[~df_list["slug"].isin(done_slugs)]
    print(f"Sisa soal yang perlu diambil teksnya: {len(rows_to_process)}")

    new_rows = []
    for _, row in tqdm(
        rows_to_process.iterrows(), total=len(rows_to_process), desc="Mengambil deskripsi soal"
    ):
        if row["is_paid_only"]:
            text = ""  # soal premium, tidak bisa diakses tanpa akun berbayar
        else:
            try:
                text = fetch_problem_content(row["slug"])
            except Exception as e:
                print(f"Gagal ambil '{row['slug']}': {e}")
                text = ""
            time.sleep(pause_between_content_calls)

        new_row = row.to_dict()
        new_row["raw_text"] = text
        new_rows.append(new_row)

        # Checkpoint tiap 50 soal supaya progress tidak hilang kalau putus di tengah
        if len(new_rows) % 50 == 0:
            df_raw = pd.concat([df_raw, pd.DataFrame(new_rows)], ignore_index=True)
            df_raw.to_csv(raw_csv, index=False)
            new_rows = []

    if new_rows:
        df_raw = pd.concat([df_raw, pd.DataFrame(new_rows)], ignore_index=True)
        df_raw.to_csv(raw_csv, index=False)

    print(f"Selesai. Total soal dengan data lengkap: {len(df_raw)} -> {raw_csv}")


if __name__ == "__main__":
    main()