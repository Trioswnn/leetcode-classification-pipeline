### Topic: Macro-F1 test (CV)

| index | LogReg | RF | MLP |
|---|---|---|---|
| TF-IDF | 0.623 (0.598)* | 0.610 (0.574) | 0.599 (0.581) |
| GloVe | 0.524 (0.491) | 0.488 (0.478) | 0.561 (0.535) |
| FastText | 0.524 (0.503) | 0.506 (0.488) | 0.566 (0.541) |
| bge-small | 0.578 (0.542) | 0.534 (0.509) | 0.598 (0.582) |
| CodeBERT | 0.557 (0.545) | 0.487 (0.455) | 0.606 (0.566) |
| Random baseline | 0.153 |  |  |

** = terbaik menurut CV. Sel: test (CV). Baseline: prediksi acak sesuai prevalensi latih, rata-rata 50 undian.*

### Difficulty: Macro-F1 test (CV)

| index | LogReg | RF | MLP |
|---|---|---|---|
| TF-IDF | 0.498 (0.502) | 0.505 (0.511) | 0.484 (0.478) |
| TF-IDF+digits | 0.539 (0.544)* | 0.542 (0.544) | 0.534 (0.525) |
| GloVe | 0.424 (0.439) | 0.387 (0.384) | 0.452 (0.451) |
| FastText | 0.432 (0.428) | 0.395 (0.372) | 0.458 (0.455) |
| bge-small | 0.480 (0.482) | 0.376 (0.385) | 0.497 (0.483) |
| CodeBERT | 0.505 (0.512) | 0.443 (0.445) | 0.503 (0.525) |
| Majority class | 0.224 |  |  |
| Random (stratified) | 0.336 |  |  |

** = terbaik menurut CV. Sel: test (CV).*

### Topic: model terbaik per representasi (test set)

| Representation | Model | Macro-F1 (CV) | Macro-F1 | 95% CI | Micro-F1 | Hamming |
|---|---|---|---|---|---|---|
| TF-IDF | LogReg | 0.598 | 0.623 | [0.597, 0.645] | 0.68 | 0.105 |
| GloVe | MLP | 0.535 | 0.561 | [0.534, 0.584] | 0.602 | 0.145 |
| FastText | MLP | 0.541 | 0.566 | [0.539, 0.588] | 0.617 | 0.134 |
| bge-small | MLP | 0.582 | 0.598 | [0.574, 0.621] | 0.649 | 0.118 |
| CodeBERT | MLP | 0.566 | 0.606 | [0.583, 0.627] | 0.665 | 0.112 |

### Difficulty: model terbaik per representasi (test set)

| Representation | Model | Macro-F1 (CV) | Accuracy | Macro-P | Macro-R | Macro-F1 | 95% CI |
|---|---|---|---|---|---|---|---|
| TF-IDF | RF | 0.511 | 0.55 | 0.541 | 0.503 | 0.505 | [0.464, 0.542] |
| TF-IDF+digits | LogReg | 0.544 | 0.548 | 0.534 | 0.548 | 0.54 | [0.501, 0.577] |
| GloVe | MLP | 0.451 | 0.465 | 0.448 | 0.459 | 0.452 | [0.416, 0.489] |
| FastText | MLP | 0.455 | 0.473 | 0.454 | 0.465 | 0.458 | [0.420, 0.499] |
| bge-small | MLP | 0.483 | 0.518 | 0.502 | 0.493 | 0.497 | [0.458, 0.535] |
| CodeBERT | MLP | 0.525 | 0.525 | 0.507 | 0.5 | 0.503 | [0.461, 0.548] |

### Hyperparameter terpilih: topic

| rep | model | best_params | threshold |
|---|---|---|---|
| TF-IDF | LogReg | C=10.0 | 0.4 |
| TF-IDF | RF | n_estimators=200, max_depth=None, min_samples_leaf=1, max_features=0.2 | 0.2 |
| TF-IDF | MLP | lr=0.0003, weight_decay=0.01, epochs=60 | 0.15 |
| GloVe | LogReg | C=0.1 | 0.6 |
| GloVe | RF | n_estimators=400, max_depth=40, min_samples_leaf=1, max_features=sqrt | 0.15 |
| GloVe | MLP | lr=0.0003, weight_decay=0.01, epochs=30 | 0.5 |
| FastText | LogReg | C=0.1 | 0.5 |
| FastText | RF | n_estimators=200, max_depth=40, min_samples_leaf=1, max_features=0.2 | 0.2 |
| FastText | MLP | lr=0.0003, weight_decay=0.01, epochs=60 | 0.5 |
| bge-small | LogReg | C=0.1 | 0.65 |
| bge-small | RF | n_estimators=400, max_depth=None, min_samples_leaf=1, max_features=0.2 | 0.15 |
| bge-small | MLP | lr=0.0003, weight_decay=0.01, epochs=30 | 0.5 |
| CodeBERT | LogReg | C=0.1 | 0.55 |
| CodeBERT | RF | n_estimators=400, max_depth=None, min_samples_leaf=2, max_features=0.2 | 0.15 |
| CodeBERT | MLP | lr=0.0003, weight_decay=0.01, epochs=30 | 0.5 |

### Hyperparameter terpilih: difficulty

| rep | model | best_params |
|---|---|---|
| TF-IDF | LogReg | C=1.0 |
| TF-IDF | RF | n_estimators=400, max_depth=40, min_samples_leaf=2, max_features=sqrt |
| TF-IDF | MLP | lr=0.0003, weight_decay=0.01, epochs=30 |
| GloVe | LogReg | C=1.0 |
| GloVe | RF | n_estimators=400, max_depth=40, min_samples_leaf=2, max_features=sqrt |
| GloVe | MLP | lr=0.0003, weight_decay=0.01, epochs=30 |
| FastText | LogReg | C=1.0 |
| FastText | RF | n_estimators=400, max_depth=None, min_samples_leaf=2, max_features=0.2 |
| FastText | MLP | lr=0.0003, weight_decay=0.01, epochs=30 |
| bge-small | LogReg | C=0.1 |
| bge-small | RF | n_estimators=400, max_depth=None, min_samples_leaf=2, max_features=0.2 |
| bge-small | MLP | lr=0.0003, weight_decay=0.01, epochs=60 |
| CodeBERT | LogReg | C=0.1 |
| CodeBERT | RF | n_estimators=400, max_depth=None, min_samples_leaf=2, max_features=0.2 |
| CodeBERT | MLP | lr=0.0003, weight_decay=0.01, epochs=60 |
| TF-IDF+digits | LogReg | C=1.0 |
| TF-IDF+digits | RF | n_estimators=400, max_depth=40, min_samples_leaf=2, max_features=sqrt |
| TF-IDF+digits | MLP | lr=0.0003, weight_decay=0.01, epochs=60 |

### RQ2 dan RQ3: selisih Macro-F1 (CV dan test) per model

| task | comparison | model | delta_CV | delta_test | same_sign_all_models |
|---|---|---|---|---|---|
| topic | RQ2 FastText - GloVe | LogReg | 0.0123 | 0.0002 | True |
| topic | RQ2 FastText - GloVe | RF | 0.0108 | 0.0186 | True |
| topic | RQ2 FastText - GloVe | MLP | 0.0057 | 0.0044 | True |
| topic | RQ3 CodeBERT - bge-small | LogReg | 0.0025 | -0.0202 | False |
| topic | RQ3 CodeBERT - bge-small | RF | -0.0534 | -0.0471 | False |
| topic | RQ3 CodeBERT - bge-small | MLP | -0.0159 | 0.0077 | False |
| difficulty | RQ2 FastText - GloVe | LogReg | -0.0103 | 0.0079 | False |
| difficulty | RQ2 FastText - GloVe | RF | -0.012 | 0.0079 | False |
| difficulty | RQ2 FastText - GloVe | MLP | 0.0032 | 0.0066 | False |
| difficulty | RQ3 CodeBERT - bge-small | LogReg | 0.0303 | 0.0256 | True |
| difficulty | RQ3 CodeBERT - bge-small | RF | 0.06 | 0.0672 | True |
| difficulty | RQ3 CodeBERT - bge-small | MLP | 0.0417 | 0.0064 | True |

*Positif = representasi pertama lebih tinggi. same_sign_all_models=True berarti arah selisih konsisten di ketiga model.*

### RQ1: representasi sparse vs padat terbaik (menurut CV)

| task | sparse | dense_best | CV_sparse | CV_dense | test_sparse | test_dense | delta_test |
|---|---|---|---|---|---|---|---|
| topic | TF-IDF x LogReg | bge-small x MLP | 0.5979 | 0.5816 | 0.6234 | 0.5982 | 0.0252 |
| difficulty | TF-IDF x RF | CodeBERT x MLP | 0.5113 | 0.5251 | 0.5048 | 0.5031 | 0.0017 |
| difficulty | TF-IDF+digits x LogReg | CodeBERT x MLP | 0.5441 | 0.5251 | 0.5395 | 0.5031 | 0.0364 |

### RQ4: perbandingan topic vs difficulty dengan koreksi baseline acak

| task | best_model | CV_macro_f1 | test_macro_f1 | random_baseline | skill_test |
|---|---|---|---|---|---|
| topic | TF-IDF x LogReg | 0.5979 | 0.6234 | 0.1529 | 0.555 |
| difficulty | TF-IDF+digits x LogReg | 0.5441 | 0.5395 | 0.3355 | 0.307 |

*skill = (skor - baseline)/(1 - baseline). Macro-F1 mentah dua tugas tidak sebanding langsung karena baseline acaknya berbeda.*

### Ablasi angka: TF-IDF x LogReg

| target | variant | n_features | cv_macro_f1_mean | cv_macro_f1_std | test_macro_f1 |
|---|---|---|---|---|---|
| difficulty | clean | 10000 | 0.501 | 0.016 | 0.496 |
| difficulty | digits | 10000 | 0.545 | 0.012 | 0.546 |
| difficulty | digits_only | 2271 | 0.495 | 0.024 | 0.459 |
| topic | clean | 10000 | 0.597 | 0.009 | 0.626 |
| topic | digits | 10000 | 0.597 | 0.01 | 0.625 |
| topic | digits_only | 2271 | 0.342 | 0.007 | 0.359 |

*clean = tanpa angka; digits = kata + angka; digits_only = hanya token angka. Angka dari Notebook 07 dipakai hanya di tabel ablasi; tabel utama memakai Notebook 05/06/05b.*

### Ablasi angka: selisih berpasangan terhadap clean

| target | variant_vs_clean | delta_cv_mean | folds_better | delta_test | delta_test_ci_low | delta_test_ci_high | ci_excludes_0 |
|---|---|---|---|---|---|---|---|
| difficulty | digits | 0.0442 | 5/5 | 0.0501 | 0.0187 | 0.0821 | True |
| difficulty | digits_only | -0.0061 | 1/5 | -0.0363 | -0.0943 | 0.0155 | False |
| topic | digits | 0.0 | 2/5 | -0.001 | -0.0154 | 0.013 | False |
| topic | digits_only | -0.2552 | 0/5 | -0.2675 | -0.2943 | -0.2407 | True |

### Distribusi difficulty dan split

| difficulty | Problems | Share (%) | Train | Test |
|---|---|---|---|---|
| Easy | 833.0 | 25.6 | 667.0 | 166.0 |
| Medium | 1645.0 | 50.5 | 1316.0 | 329.0 |
| Hard | 778.0 | 23.9 | 622.0 | 156.0 |
| Total | 3256.0 | 100.0 | 2605.0 | 651.0 |

### Distribusi 15 topik teratas

| Topic | All | Train | Test | Prevalence (%) |
|---|---|---|---|---|
| array | 1909 | 1527 | 382 | 58.6 |
| string | 767 | 613 | 154 | 23.6 |
| hash_table | 703 | 562 | 141 | 21.6 |
| math | 609 | 487 | 122 | 18.7 |
| dynamic_programming | 594 | 475 | 119 | 18.2 |
| sorting | 459 | 367 | 92 | 14.1 |
| greedy | 432 | 346 | 86 | 13.3 |
| binary_search | 297 | 237 | 60 | 9.1 |
| depth_first_search | 263 | 211 | 52 | 8.1 |
| bit_manipulation | 259 | 207 | 52 | 8.0 |
| prefix_sum | 243 | 194 | 49 | 7.5 |
| matrix | 237 | 189 | 48 | 7.3 |
| two_pointers | 219 | 175 | 44 | 6.7 |
| breadth_first_search | 203 | 162 | 41 | 6.2 |
| tree | 200 | 160 | 40 | 6.1 |

### Statistik OOV (GloVe vs FastText)

| index | GloVe | FastText (word vocab) |
|---|---|---|
| token_oov_rate_% | 7.52 | 2.79 |
| type_oov_rate_% | 24.55 | 21.71 |
| docs_all_oov | 0.0 | 0.0 |
| doc_oov_mean_% | 8.07 | 2.32 |
| doc_oov_max_% | 72.73 | 53.97 |

### Statistik pemotongan token (maks. 512)

| model | max_len | tokens_mean | tokens_median | tokens_p95 | tokens_max | problems_truncated_n | problems_truncated_% | tokens_lost_% |
|---|---|---|---|---|---|---|---|---|
| BAAI/bge-small-en-v1.5 | 512 | 383.0 | 342.0 | 758.25 | 1935 | 633 | 19.44 | 9.58 |
| microsoft/codebert-base | 512 | 352.1 | 319.0 | 659.5 | 1572 | 464 | 14.25 | 6.09 |

### Contoh preprocessing (id=3, Longest Substring Without Repeating Characters)

| Stage | Content |
|---|---|
| Raw text | Given a string s , find the length of the longest substring without duplicate characters. Example 1: Input: s = "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers. Example 2: Input: s = "bbbbb" Output: 1 Explanation: The ... |
| text_light (transformers) | Given a string s , find the length of the longest substring without duplicate characters. Example 1: Input: s = "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers. Example 2: Input: s = "bbbbb" Output: 1 Explanation: The ... |
| text_clean (TF-IDF, static) | string find length longest substring without duplicate characters abcabcbb answer abc length bca cab also correct answers bbbbb answer length pwwkew answer wke length notice answer must substring pwke subsequence substring length consists english letters digits symbols spaces |
| text_clean_digits (TF-IDF+digits) | string find length longest substring without duplicate characters 1 abcabcbb 3 answer abc length 3 bca cab also correct answers 2 bbbbb 1 answer length 1 3 pwwkew 3 answer wke length 3 notice answer must substring pwke subsequence substring 0 length 10 5 consists english letters digits symbols ... |

### F1 per label (TF-IDF x LogReg)

| topic | support_test | f1 |
|---|---|---|
| string | 154 | 0.954 |
| tree | 40 | 0.95 |
| array | 382 | 0.931 |
| matrix | 48 | 0.911 |
| depth_first_search | 52 | 0.709 |
| math | 122 | 0.682 |
| breadth_first_search | 41 | 0.586 |
| dynamic_programming | 119 | 0.534 |
| hash_table | 141 | 0.492 |
| bit_manipulation | 52 | 0.479 |
| greedy | 86 | 0.453 |
| sorting | 92 | 0.448 |
| two_pointers | 44 | 0.438 |
| binary_search | 60 | 0.426 |
| prefix_sum | 49 | 0.358 |

### Recall per kelas difficulty

| model | recall_Easy | recall_Medium | recall_Hard |
|---|---|---|---|
| CodeBERT + MLP | 0.494 | 0.596 | 0.41 |
| TF-IDF+digits + LogReg | 0.596 | 0.547 | 0.5 |
