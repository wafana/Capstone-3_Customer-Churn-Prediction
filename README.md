# Pendahuluan
Churn pelanggan merupakan tantangan utama dalam industri e-commerce karena dapat berdampak langsung pada pendapatan dan profitabilitas perusahaan. Oleh karena itu, prediksi churn menjadi aspek krusial dalam strategi retensi pelanggan. Percobaan ini bertujuan untuk mengembangkan model machine learning yang dapat memprediksi kemungkinan pelanggan akan berhenti menggunakan layanan dalam periode tertentu. Dataset yang digunakan terdiri dari berbagai fitur yang mencerminkan perilaku pelanggan, termasuk riwayat transaksi, interaksi dengan platform, dan karakteristik demografis.

Dalam penelitian ini, diterapkan beberapa teknik pemodelan machine learning, yaitu Logistic Regression, Random Forest, dan XGBoost. Selain itu, dilakukan proses seleksi fitur, resampling data menggunakan SMOTE untuk menangani ketidakseimbangan kelas, serta optimasi hiperparameter guna meningkatkan performa model. Model dievaluasi menggunakan metrik F2-score untuk memastikan keseimbangan antara recall dan precision dalam mendeteksi churn.

Hasil eksperimen menunjukkan bahwa model XGBoost dengan SMOTE memberikan performa terbaik dengan F2-score sebesar 0.849220 pada data test yang telah dituning, mengungguli model lainnya. Temuan ini mengindikasikan bahwa kombinasi teknik oversampling dan pemilihan model yang tepat dapat meningkatkan akurasi prediksi churn. Implementasi model ini dapat membantu perusahaan dalam mengidentifikasi pelanggan yang berisiko churn lebih awal, sehingga memungkinkan pengambilan keputusan yang lebih proaktif dalam strategi retensi pelanggan.

**Kata Kunci:** Churn Prediction, Machine Learning, E-commerce, XGBoost, SMOTE, F2-score

Streamlit: https://capstone-3customer-churn-prediction-5woqv4x2qgheqxkzd7f9vy.streamlit.app/
