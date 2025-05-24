# Laporan Proyek Machine Learning - I Gede Widnyana

# Laporan Proyek Machine Learning - Nama Anda

## Project Overview

Sistem rekomendasi telah menjadi bagian penting dalam berbagai layanan digital, terutama dalam industri hiburan seperti film. Dengan meningkatnya jumlah film dan preferensi pengguna yang beragam, dibutuhkan sistem yang mampu memberikan rekomendasi yang personal dan relevan. Proyek ini bertujuan untuk membangun sistem rekomendasi film berbasis dua pendekatan utama, yaitu Content-Based Filtering dan Collaborative Filtering, untuk meningkatkan pengalaman pengguna dalam menemukan film yang sesuai.

Menurut Ricci et al. (2011), sistem rekomendasi tidak hanya meningkatkan kepuasan pengguna tetapi juga meningkatkan pendapatan layanan digital secara signifikan. Oleh karena itu, proyek ini penting untuk memberikan nilai tambah baik bagi pengguna maupun penyedia layanan film.

Referensi:

* Ricci, F., Rokach, L., & Shapira, B. (2011). Introduction to Recommender Systems Handbook. Springer.

## Business Understanding

### Problem Statements

* Bagaimana cara merekomendasikan film yang relevan untuk pengguna berdasarkan riwayat atau minat mereka?
* Model rekomendasi apa yang memberikan hasil terbaik untuk kebutuhan ini?

### Goals

* Mengembangkan sistem rekomendasi film menggunakan dua pendekatan berbeda.
* Mengevaluasi dan membandingkan performa kedua pendekatan tersebut.

### Solution Approach

#### Solution 1: Content-Based Filtering

Model ini merekomendasikan film berdasarkan kemiripan konten seperti genre, sinopsis, dan metadata lainnya. Pendekatan ini fokus pada karakteristik film yang mirip dengan film yang disukai pengguna.

#### Solution 2: Collaborative Filtering

Model ini merekomendasikan film berdasarkan preferensi pengguna lain yang memiliki kesamaan perilaku. Pendekatan ini mengandalkan pola rating yang mirip antar pengguna.

## Data Understanding

Dataset yang digunakan terdiri dari dua file utama:

* **movies.csv**: Berisi 10.329 data film
* **ratings.csv**: Berisi 105.339 rating dari 668 pengguna unik

Contoh data dari `movies.csv`:

| movieId | title            | genres    |           |             |
| ------- | ---------------- | --------- | --------- | ----------- |
| 1       | Toy Story (1995) | Adventure | Animation | Children... |
| 2       | Jumanji (1995)   | Adventure | Children  | Fantasy     |

Contoh data dari `ratings.csv`:

| userId | movieId | rating | timestamp  |
| ------ | ------- | ------ | ---------- |
| 1      | 16      | 4.0    | 1217897793 |
| 1      | 24      | 1.5    | 1217895807 |

Penjelasan fitur/kolom pada kedua dataset:

* **user\_id**: ID pengguna
* **MovieId**: ID film
* **rating**: nilai rating dari 1 hingga 5
* **timestamp**: waktu rating diberikan
* **title**: judul film
* **genres**: genre film

Pada proyek sistem rekomendasi film ini, digunakan dua metode utama, yaitu **Content-Based Filtering** dan **Collaborative Filtering (User-Based)**. Masing-masing metode memanfaatkan fitur yang berbeda sesuai dengan pendekatannya.

### 1. Content-Based Filtering

Metode ini menggunakan fitur-fitur yang berasal langsung dari atribut film untuk membangun model rekomendasi. Fitur utama yang digunakan adalah:

- **Genres (Genre Film)**  
  Genre film seperti Adventure, Animation, Comedy, Fantasy, dan lain-lain menjadi fitur utama. Genre ini diolah menjadi representasi numerik melalui teknik representasi vektor untuk menghitung kemiripan antar film.

- **Title (Judul Film)**  
  Judul film digunakan sebagai indeks untuk pencarian dan pemetaan ke vektor fitur.

**Cara Kerja:**  
Setiap film direpresentasikan sebagai vektor fitur berdasarkan genre atau deskripsi filmnya. Kemiripan antar film dihitung menggunakan cosine similarity antara vektor-vektor tersebut. Film-film yang memiliki skor kemiripan tinggi akan direkomendasikan.

### 2. Collaborative Filtering (User-Based)

Metode ini menggunakan data interaksi pengguna (rating) terhadap film untuk merekomendasikan film baru. Fitur utama yang digunakan adalah:

- **User-Item Rating Matrix**  
  Matriks dua dimensi yang berisi rating dari setiap user terhadap film yang sudah ditonton. Baris adalah `userId`, kolom adalah `movieId`, dan nilai adalah rating (skala 1 sampai 5).

- **User Similarity**  
  Kemiripan antar pengguna dihitung berdasarkan pola rating mereka menggunakan cosine similarity. Pengguna yang memiliki pola rating mirip dianggap memiliki preferensi yang sama.

**Cara Kerja:**  
Sistem mencari pengguna-pengguna yang paling mirip dengan pengguna target berdasarkan kemiripan rating. Rekomendasi film dibuat dari film-film yang belum ditonton oleh pengguna target tapi diberi rating tinggi oleh pengguna mirip.

---

### Exploratory Data Analysis (EDA)

Untuk memahami struktur dan karakteristik data, dilakukan beberapa tahap eksplorasi visual dan analisis sebagai berikut:

#### 1. Sebaran Genre Film

Visualisasi pertama menunjukkan jumlah film untuk setiap genre berdasarkan representasi biner dari kolom `genres`. Hasil visualisasi ini memberikan gambaran dominasi genre dalam koleksi film:

* Genre **Drama** memiliki jumlah film terbanyak, mencapai hampir **5.000** film, menunjukkan dominasi genre ini dalam industri perfilman.
* **Comedy** dan **Thriller** juga populer dengan masing-masing mendekati **4.000** dan **3.000** film.
* Sebaliknya, genre seperti **Documentary**, **Musical**, dan **Western** memiliki kurang dari **1.000** film, menandakan segmentasi pasar yang lebih sempit atau produksi terbatas.
* Perbedaan ini mencerminkan tren industri, biaya produksi, dan preferensi penonton.

#### 2. Distribusi Rating Pengguna

Visualisasi histogram memperlihatkan distribusi nilai rating yang diberikan oleh pengguna:

* Mayoritas rating berada pada rentang **4 hingga 5**, dengan frekuensi sekitar **20.000–30.000**, menandakan mayoritas penilaian cenderung positif.
* Rating di bawah **3** sangat jarang, umumnya di bawah **10.000**, menunjukkan sedikit pengguna yang memberikan ulasan buruk.
* Rating ekstrem seperti **1** atau **6–7** memiliki jumlah yang sangat sedikit, mencerminkan kecenderungan pengguna untuk menghindari penilaian ekstrem.
* Hal ini dapat menunjukkan tingkat kepuasan pengguna secara umum atau bias dalam sistem rating.

#### 3. Film dengan Jumlah Rating Terbanyak

Analisis terhadap film dengan jumlah rating terbanyak mengungkap popularitas film tertentu:

* Film seperti **The Shawshank Redemption (1994)** dan **Pulp Fiction (1994)** mendominasi dengan jumlah rating melebihi **250**, menandakan daya tarik dan pengaruh budaya yang kuat.
* **Forrest Gump (1994)**, **The Matrix (1999)**, dan **Jurassic Park (1993)** juga memiliki banyak rating, mengindikasikan keberhasilan komersial dan daya ingat yang kuat di kalangan penonton.
* Sebagian besar film yang mendominasi daftar ini berasal dari dekade **1990-an**, yang bisa dikaitkan dengan era keemasan perfilman atau nostalgia terhadap film klasik.
* **Star Wars: Episode IV - A New Hope (1977)** adalah satu-satunya film dari era 1970-an yang masih populer.

#### 4. Rata-rata Rating per Genre (≥ 50 Rating)

Dengan menggabungkan informasi rating dan genre, diperoleh rata-rata rating per genre untuk film yang memiliki setidaknya 50 rating:

* **Film-Noir** dan **War** menempati posisi teratas dengan rata-rata mendekati **4.0**, menunjukkan bahwa meskipun film-filmnya sedikit, kualitasnya dihargai tinggi oleh penonton.
* Genre **Drama**, **Crime**, dan **Documentary** juga mencatat rating rata-rata di atas **3.5**, menandakan penghargaan terhadap konten mendalam dan berbobot.
* Sebaliknya, genre seperti **Horror**, **Action**, **Comedy**, dan **Sci-Fi** cenderung memiliki rating lebih rendah (sekitar **3.0** atau di bawahnya), yang mungkin mencerminkan ekspektasi penonton yang lebih tinggi atau cerita yang cenderung berulang.
* Genre **Western** mencatatkan rating terendah, mungkin karena minat penonton yang berkurang terhadap tema ini.


## Data Preparation

Tahapan yang dilakukan:

1. **Pembersihan Data**:

   * Memastikan tidak ada nilai kosong pada kedua dataset.

2. **Ekstraksi Genre**:

   * Genre diformat ulang dari string menjadi list menggunakan `.split('|')`.

3. **Encoding Genre**:

   * Menggunakan `MultiLabelBinarizer` untuk mengubah genre menjadi matriks biner.

4. **Perhitungan Cosine Similarity**:

   * Digunakan untuk mengukur kesamaan antar film berdasarkan genre.

5. **Index Mapping**:

   * Membuat mapping antara judul film dan indeks untuk memudahkan pencarian rekomendasi.

Alasan tahapan ini dilakukan adalah agar data dalam format yang dapat digunakan untuk perhitungan similarity dan pembuatan model.

## Modeling

## Tahap Modeling dan Evaluasi Sistem Rekomendasi

Pada tahap ini, kami membangun dua pendekatan sistem rekomendasi: **Content-Based Filtering (CBF)** dan **User-Based Collaborative Filtering (CF)**. Kedua metode ini memiliki karakteristik dan mekanisme kerja yang berbeda dalam menyajikan rekomendasi film kepada pengguna.

---

### 🎯 Content-Based Filtering (CBF)

#### Definisi

CBF adalah metode sistem rekomendasi yang merekomendasikan item kepada pengguna berdasarkan kemiripan konten dari item yang pernah disukai. Dalam kasus ini, kita menggunakan **kemiripan antar film** berdasarkan fitur `genres` yang telah diproses menjadi representasi vektor.

#### Parameter dan Cara Kerja:

* **Fitur yang digunakan**: `genres` dari setiap film, diproses dari dataset
* **Fungsi kemiripan**: `cosine_similarity` dari `sklearn`, menghitung kemiripan antara dua vektor genre.
* **Top-N**: jumlah rekomendasi yang diambil, dalam kasus ini `top_n=10`.
* **Algoritma rekomendasi**:

  * Ambil indeks film input (misal: 'Toy Story').
  * Hitung cosine similarity antara film tersebut dan seluruh film lain.
  * Urutkan berdasarkan nilai kemiripan, ambil 10 teratas (tidak termasuk film itu sendiri).

#### Fungsi Utama:

```python
def dapatkan_rekomendasi(title, cosine_sim=cosine_sim, top_n=10):
```

Fungsi ini mengembalikan 10 film dengan genre paling mirip dengan film input berdasarkan cosine similarity.

#### Evaluasi:

Metode evaluasi menggunakan **Precision\@K**, yaitu proporsi item yang direkomendasikan dan relevan (pernah diberi rating tinggi oleh user) dari total K rekomendasi.

```python
def evaluasi_precision_at_k(...)
```

Hasil evaluasi untuk 50 pengguna: **Precision\@10 = 0.072**

#### Kelebihan dan Kekurangan:

**Kelebihan:**

* Tidak memerlukan data rating dari banyak pengguna.
* Cocok untuk pengguna baru karena hanya butuh satu item yang disukai.
* Hasil rekomendasi cenderung konsisten dan dapat dijelaskan (berdasarkan genre, fitur item).

**Kekurangan:**

* Terbatas pada fitur yang tersedia (misal hanya `genres`).
* Cenderung merekomendasikan item yang terlalu mirip (kurang keberagaman).
* Tidak bisa menangkap selera pengguna yang kompleks di luar fitur konten.

---

### 🤝 Collaborative Filtering (User-Based CF)

#### Definisi

Collaborative Filtering adalah metode sistem rekomendasi yang menyarankan item berdasarkan preferensi pengguna lain yang serupa. Dalam pendekatan ini, kita menghitung kemiripan antar pengguna berdasarkan pola rating.

#### Parameter dan Cara Kerja:

* **Input utama**: matrix user-item dari data rating.
* **Metode kemiripan**: `cosine_similarity` antar baris (user) dari user-item matrix.
* **Top-K user**: pilih 5 pengguna paling mirip sebagai basis prediksi.
* **Rerata rating**: dihitung dari user-user mirip, untuk item yang belum ditonton oleh user target.

#### Algoritma rekomendasi:

* Buat user-item matrix.
* Hitung cosine similarity antar user.
* Temukan 5 user paling mirip dengan target user.
* Ambil film yang belum ditonton oleh user target.
* Hitung rata-rata rating dari user mirip pada film tersebut.
* Kembalikan 10 film dengan rata-rata tertinggi.

#### Fungsi Utama:

```python
def rekomendasi_cf_user(user_id, top_n=10):
```

Fungsi ini menghasilkan 10 rekomendasi film berdasarkan kemiripan preferensi antar pengguna.

#### Evaluasi:

Evaluasi dilakukan dengan **Precision\@K**:

* Data rating tiap user di-split 80:20 (train-test).
* Sistem hanya menggunakan data `train` untuk membangun rekomendasi.
* Kemudian dihitung berapa banyak film di `top-K` yang masuk ke test set dan punya rating >= 4.

```python
def evaluasi_precision_at_k_cf(...)
```

Hasil evaluasi untuk 50 pengguna: **Precision\@10 = 0.190**

#### Kelebihan dan Kekurangan:

**Kelebihan:**

* Dapat menangkap preferensi pengguna yang kompleks dan tidak terbatas pada fitur konten.
* Mampu memberikan rekomendasi yang lebih personal karena berbasis komunitas pengguna.
* Semakin banyak data pengguna, semakin baik performanya.

**Kekurangan:**

* Terkena masalah cold-start untuk pengguna baru tanpa rating.
* Sensitif terhadap sparsity (banyak nilai kosong dalam user-item matrix).
* Membutuhkan banyak data interaksi pengguna agar efektif.

---

### Kesimpulan Sementara

Berdasarkan hasil evaluasi, model Collaborative Filtering menghasilkan performa yang **lebih baik** (Precision\@10 = 0.190) dibanding Content-Based Filtering (Precision\@10 = 0.072). Hal ini menunjukkan bahwa memanfaatkan informasi preferensi antar pengguna (kolaboratif) memberikan hasil rekomendasi yang lebih akurat dalam kasus ini.


## 📋 Hasil Rekomendasi Top-N

Berikut ini adalah contoh hasil rekomendasi **Top-10** untuk film *"Toy Story (1995)"* berdasarkan masing-masing metode:

### 🎬 Content-Based Filtering

| No | Judul Film                                              | Genre                                           | Nilai Kemiripan |
| -- | ------------------------------------------------------- | ----------------------------------------------- | --------------- |
| 1  | Antz (1998)                                             | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 2  | Toy Story 2 (1999)                                      | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 3  | Adventures of Rocky and Bullwinkle, The (2000)          | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 4  | Emperor's New Groove, The (2000)                        | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 5  | Monsters, Inc. (2001)                                   | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 6  | DuckTales: The Movie - Treasure of the Lost Lamp (1990) | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 7  | Wild, The (2006)                                        | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 8  | Shrek the Third (2007)                                  | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 9  | Tale of Despereaux, The (2008)                          | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |
| 10 | Asterix and the Vikings (2006)                          | Adventure, Animation, Children, Comedy, Fantasy | 1.0             |

### 🤝 User-Based Collaborative Filtering

| No | Judul Film                                                    | Genre                                           |
| -- | ------------------------------------------------------------- | ----------------------------------------------- |
| 1  | Toy Story (1995)                                              | Adventure, Animation, Children, Comedy, Fantasy |
| 2  | Dumb & Dumber (Dumb and Dumber) (1994)                        | Adventure, Comedy                               |
| 3  | Lion King, The (1994)                                         | Adventure, Animation, Children, Drama, Musical  |
| 4  | Indiana Jones and the Last Crusade (1989)                     | Action, Adventure                               |
| 5  | Good Will Hunting (1997)                                      | Drama, Romance                                  |
| 6  | Green Mile, The (1999)                                        | Crime, Drama                                    |
| 7  | X-Men (2000)                                                  | Action, Adventure, Sci-Fi                       |
| 8  | Memento (2000)                                                | Mystery, Thriller                               |
| 9  | Finding Nemo (2003)                                           | Adventure, Animation, Children, Comedy          |
| 10 | Pirates of the Caribbean: The Curse of the Black Pearl (2003) | Action, Adventure, Comedy, Fantasy              |


## 📊 Evaluasi Model

### Metrik Evaluasi yang Digunakan: Precision\@K

Untuk mengevaluasi kinerja sistem rekomendasi dalam proyek ini, kami menggunakan metrik **Precision\@K**. Metrik ini banyak digunakan dalam domain sistem rekomendasi karena fokus utamanya adalah mengukur **kualitas relevansi dari item-item yang direkomendasikan** kepada pengguna.

### 📌 Definisi Precision\@K

Precision\@K (P\@K) adalah proporsi item yang relevan dari K item teratas yang direkomendasikan kepada pengguna.

$\text{Precision@K} = \frac{\text{Jumlah item relevan di top-K rekomendasi}}{K}$

Item dianggap relevan apabila item tersebut memiliki rating tinggi (≥ threshold yang ditentukan, misalnya 4.0) oleh pengguna.

Precision\@K berkisar dari 0 hingga 1, dengan nilai yang lebih tinggi menunjukkan bahwa sistem rekomendasi mampu memberikan lebih banyak item relevan di posisi atas.

### 🧪 Implementasi Evaluasi

Kami melakukan evaluasi pada dua sistem rekomendasi berbeda:

#### 1. **Content-Based Filtering**

* Metrik: Precision\@10
* Threshold rating relevan: ≥ 4.0
* Jumlah pengguna sampel: 50
* Rata-rata Precision\@10: **0.072**

📌 *Interpretasi*: Hanya sekitar 7.2% dari item yang direkomendasikan berada dalam daftar film relevan berdasarkan preferensi historis pengguna. Hal ini menunjukkan bahwa sistem content-based ini kurang mampu menemukan preferensi pengguna hanya berdasarkan kemiripan konten (genre).

#### 2. **User-Based Collaborative Filtering**

* Metrik: Precision\@10
* Threshold rating relevan: ≥ 4.0
* Jumlah pengguna sampel: 50
* Rata-rata Precision\@10: **0.190**

📌 *Interpretasi*: Sekitar 19% dari rekomendasi termasuk dalam daftar film relevan menurut pengguna. Ini menunjukkan bahwa model collaborative filtering memiliki performa yang jauh lebih baik dalam menemukan item yang sesuai dengan selera pengguna dibanding pendekatan content-based.

### 🎯 Relevansi dengan Problem Statement

Karena tujuan utama proyek ini adalah **memberikan rekomendasi film yang relevan berdasarkan preferensi pengguna**, maka metrik Precision\@K dipilih karena:

* Fokus pada relevansi (bukan hanya kemiripan konten atau popularitas).
* Memungkinkan untuk menilai kualitas rekomendasi di posisi atas (top-N).
* Sangat sesuai untuk kasus di mana kita ingin memberikan saran yang tepat dan terbatas (misalnya top-10 film).

### 🔍 Kelebihan Precision\@K

* Sederhana dan mudah diinterpretasikan.
* Fokus pada bagian atas daftar rekomendasi (top-N), yang biasanya paling penting bagi pengguna.
* Menghindari penalti terhadap item tidak relevan di luar top-N.

### ⚠️ Keterbatasan

* Tidak mempertimbangkan urutan dalam top-K (urutan 1 dan 10 dianggap sama).
* Tidak memperhitungkan item relevan yang tidak direkomendasikan (tidak menghitung recall).

### 🔚 Kesimpulan Evaluasi

Model user-based collaborative filtering memiliki performa yang **lebih baik dan lebih akurat** dalam menghasilkan rekomendasi film dibanding model content-based filtering, berdasarkan metrik evaluasi Precision\@10.

---

# **ANALISIS HASIL DUA METODE**
## Perbandingan Hasil Rekomendasi: Content-Based Filtering vs Collaborative Filtering

| Title             | Rekomendasi Metode Content-Based                        | Rekomendasi Metode Collaborative Filtering               |
|-------------------|---------------------------------------------------------|-----------------------------------------------------------|
| Toy Story (1995)  | Antz (1998)                                             | Toy Story (1995)                                           |
| Toy Story (1995)  | Toy Story 2 (1999)                                      | Dumb & Dumber (Dumb and Dumber) (1994)                    |
| Toy Story (1995)  | Adventures of Rocky and Bullwinkle, The (2000)          | Lion King, The (1994)                                      |
| Toy Story (1995)  | Emperor's New Groove, The (2000)                        | Indiana Jones and the Last Crusade (1989)                  |
| Toy Story (1995)  | Monsters, Inc. (2001)                                   | Good Will Hunting (1997)                                   |
| Toy Story (1995)  | DuckTales: The Movie - Treasure of the Lost Lamp (1990)| Green Mile, The (1999)                                     |
| Toy Story (1995)  | Wild, The (2006)                                        | X-Men (2000)                                              |
| Toy Story (1995)  | Shrek the Third (2007)                                 | Memento (2000)                                            |
| Toy Story (1995)  | Tale of Despereaux, The (2008)                         | Finding Nemo (2003)                                       |
| Toy Story (1995)  | Asterix and the Vikings (Astérix et les Vikings) (2006)| Pirates of the Caribbean: The Curse of the Black Pearl (2003)|

## Penjelasan Analisis Perbandingan Metode Rekomendasi Film: Content-Based Filtering vs Collaborative Filtering

Pada studi ini, dilakukan perbandingan antara dua metode populer dalam sistem rekomendasi film, yaitu Content-Based Filtering dan Collaborative Filtering, dengan menggunakan contoh film *Toy Story (1995)* sebagai sampel pengujian.

## Hasil Rekomendasi

- **Content-Based Filtering** menghasilkan rekomendasi film yang sangat mirip dari sisi genre dan karakteristik dengan film sampel. Film-film yang direkomendasikan seperti *Antz (1998)*, *Toy Story 2 (1999)*, dan *Monsters, Inc. (2001)* merupakan film animasi yang memiliki tema dan audiens yang serupa dengan *Toy Story (1995)*. Hal ini menunjukkan bahwa metode ini efektif dalam memberikan rekomendasi berdasarkan kesamaan atribut film, khususnya genre.

- **Collaborative Filtering** memberikan rekomendasi film yang lebih bervariasi dan tidak terbatas pada genre yang sama. Contohnya, film seperti *Dumb & Dumber (1994)*, *Indiana Jones and the Last Crusade (1989)*, dan *Good Will Hunting (1997)* direkomendasikan berdasarkan pola penilaian pengguna lain yang memiliki preferensi mirip. Metode ini mengandalkan interaksi dan preferensi pengguna dalam memberikan rekomendasi, sehingga dapat mengeksplorasi film yang berbeda genre namun berpotensi disukai oleh pengguna.

## Perbandingan Skor Evaluasi

- **Precision@10 (rata-rata 50 pengguna)** untuk Content-Based Filtering adalah **0.072**, yang menunjukkan tingkat kecocokan rekomendasi berdasarkan kemiripan genre.

- **Precision@10 (rata-rata 50 pengguna)** untuk Collaborative Filtering adalah **0.190**, yang menunjukkan bahwa metode ini lebih baik dalam merekomendasikan film yang disukai pengguna berdasarkan interaksi pengguna lain.

## Analisis Perbandingan

- Metode **Content-Based Filtering** unggul dalam memberikan rekomendasi yang konsisten dengan genre dan atribut film asli, cocok untuk pengguna yang ingin menemukan film dengan karakteristik serupa. Namun, metode ini cenderung kurang mampu memberikan rekomendasi yang beragam dan eksploratif.

- Metode **Collaborative Filtering** lebih unggul dalam aspek personalisasi karena mempertimbangkan preferensi pengguna secara kolektif. Hal ini memungkinkan rekomendasi yang lebih variatif dan sesuai dengan taste pengguna secara umum, meskipun terkadang rekomendasi tersebut kurang relevan jika dilihat dari segi genre.

## Kesimpulan

Pemilihan metode rekomendasi tergantung pada tujuan sistem:

- Jika fokus utama adalah mencari film dengan karakteristik serupa berdasarkan atribut konten, maka Content-Based Filtering lebih tepat digunakan.

- Jika tujuan utama adalah memberikan rekomendasi yang personal dan beragam berdasarkan preferensi pengguna, Collaborative Filtering lebih direkomendasikan.
