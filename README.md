# LeetCode Problem Classification Pipeline

Proyek ini adalah pipeline machine learning untuk mengklasifikasikan tingkat kesulitan dan topik dari soal-soal LeetCode berdasarkan deskripsi teksnya.

## Struktur Direktori
- `scraping/`: Script untuk mengumpulkan data dari LeetCode.
- `01_preprocessing/`: Pembersihan data teks.
- `02_eda_label_split/`: Exploratory Data Analysis dan pemisahan train/test.
- `03-features-static/`: Ekstraksi fitur menggunakan model statis (FastText, GloVe).
- `04-features-transformer/`: Ekstraksi fitur menggunakan model Transformer (CodeBERT, SBERT).
- `05-modeling-difficulty/`: Pemodelan untuk prediksi tingkat kesulitan.
- `06-modeling-topic/`: Pemodelan multilabel untuk prediksi topik.
- `08-paper-assets/`: Hasil evaluasi, tabel, dan gambar untuk kebutuhan laporan/paper.