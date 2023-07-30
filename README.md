# **Laporan Proyek Machine Learning - Adita Putri Puspaningrum**

---

# **PREDIKSI HARGA RUMAH YANG TERSEDIA UNTUK DISEWAKAN**

# **Domain Proyek**

India adalah negara yang kaya akan keanekaragaman geografis dan sosial. Namun, negara ini juga dihadapkan pada tantangan yang serius terkait masalah perumahan. Perbedaan signifikan dalam kondisi perumahan antara wilayah perkotaan dan pedesaan menjadi salah satu isu krusial yang perlu diperhatikan.

Wilayah perkotaan di India umumnya ditandai dengan infrastruktur yang lebih baik, aksesibilitas yang lebih baik terhadap pendidikan dan layanan kesehatan, serta beragam pilihan pekerjaan. Namun, sebagai akibat dari urbanisasi berkelanjutan, kota-kota di India seringkali menghadapi lonjakan penduduk yang cepat, yang mengakibatkan peningkatan permintaan akan perumahan. Tingginya angka pertumbuhan penduduk dan kebutuhan perumahan yang belum terpenuhi menyebabkan semakin meningkatnya kesenjangan pemenuhan kebutuhan perumahan di wilayah perkotaan [1].

Di sisi lain, wilayah pedesaan memiliki kondisi perumahan dan infrastruktur yang sering kali lebih sederhana. Akses ke layanan, termasuk pendidikan dan kesehatan, mungkin terbatas di wilayah-wilayah ini. Sebagian besar penduduk pedesaan bergantung pada mata pencaharian pertanian atau pekerjaan terkait pedesaan, dan ketidakstabilan ekonomi di sektor ini dapat mempengaruhi kemampuan mereka untuk membeli atau memiliki rumah yang layak.

Menurut _Human Rights Measurement Initiative_ [8], India baru mencapai 68,7% dari potensi hak atas perumahan yang semestinya dapat terpenuhi berdasarkan tingkat pendapatan negara tersebut. Artinya, masih banyak orang di India yang tidak bisa memperoleh perumahan yang seharusnya bisa mereka dapatkan.

Kekurangan perumahan telah menjadi isu serius bagi sebagian besar masyarakat di India. Salah satu pilihan bagi mereka yang belum memiliki rumah adalah menyewa properti, seperti rumah atau apartemen. Fenomena penyewaan properti ini juga mencerminkan tren ekonomi berbagi yang semakin berkembang pesat di berbagai belahan dunia. Ekonomi berbagi merupakan suatu tindakan modernisasi yang menggunakan platform online untuk memfasilitasi dan menurunkan biaya transaksi nirlaba untuk memberikan akses sementara tanpa transfer kepemilikan pada sumber daya konsumen yang menganggur [2]. Dengan kata lain, seseorang atau sekelompok orang dapat memanfaatkan properti (dalam kasus ini, properti tempat tinggal) milik orang lain untuk memenuhi kebutuhan mereka.

Dalam konteks India, tantangan kekurangan perumahan dan model ekonomi berbagi ini memiliki implikasi sosial, ekonomi, dan kebijakan yang kompleks. Oleh karena itu, langkah-langkah solutif yang holistik dan berkelanjutan diperlukan untuk mengatasi masalah ini dan memastikan bahwa setiap warga negara di India memiliki akses terhadap perumahan yang layak dan memadai.

# **_Business Understanding_**

Penelitian ini bertujuan untuk menganalisis faktor apa saja yang dapat mempengaruhi pemilihan penyewaan rumah atau tempat tinggal. Dengan begitu, perusahaan atau pemilik properti yang hendak menyewakan properti miliknya dapat menentukan target penyewa dengan lebih tepat dan sesuai dengan kondisi properti yang ada.

*   _Problem Statements_
    
    Berdasarkan uraian latar belakang masalah yang telah dijelaskan pada bagian sebelumnya, berikut ini merupakan rumusan masalah dari penelitian ini :

    a.   Apa saja faktor yang mempengaruhi pengambilan keputusan untuk menyewa suatu rumah ?
    
    b.   Apa algoritma yang mampu memprediksi pilihan terbaik untuk menyewa suatu rumah ?

*   _Goals_
  
    Berikut ini merupakan uraian tujuan dari rumusan masalah yang telah dijelaskan :
    
    a.   Menentukan faktor yang mempengaruhi pengambilan keputusan untuk menyewa suatu rumah.
    
    b.   Menentukan algoritma yang mampu memprediksi pilihan terbaik untuk menyewa suatu rumah

*   _Solution Statements_
  
    Untuk memenuhi tujuan dari penelitian ini, berikut merupakan solusi yang dapat penulis ajukan :
    
    a.   Untuk mengetahui algoritma yang terbaik dalam menentukan pilihan penyewaan rumah, akan dilakukan komparasi terhadap tiga jenis algoritma, yaitu _K-Nearest Neighbour_ (KNN), _Random Forest_ dan AdaBoost.
    
    b.   Setelah ketiga jenis algoritma tersebut berhasil dijalankan, akan dilakukan evaluasi untuk mengukur nilai akurasi pada masing-masing algoritma.

# **_Data Understanding_**

* Penelitian ini menggunakan dataset yang berjudul 'House Rent Prediction' yang dibuat dari _website_ https://www.magicbricks.com/. Namun, penulis mengambil dataset ini dari Kaggle dengan link [dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset).


* Dataset ini memiliki format CSV (*comma separated value*) yang berjumlah 4.746 data dengan 12 fitur, dimana 8 fitur bertipe *object* sedangkan 4 fitur sisanya bertipe *int64*.


* Variabel-variabel yang terdapat pada dataset 'House Rent Prediction' ini adalah sebagai berikut :
  1.  'Posted On' : Tanggal data di-_posting_.
  2.  'BHK' : Jumlah dari kamar tidur, aula, dan dapur.
  3.  'Rent' : Harga sewa dari rumah/apartemen.
  4.  'Size' : Ukuran dari rumah/apartemen dalam _square feet_ (sqft).
  5.  'Floor' : Letak lantai dari apartemen/rumah susun yang disewakan dan jumlah lantai dari bangunan rumah/apartemen tersebut.
  6.  'Area Type' : Ukuran dari rumah dalam kategori 'Super Area', 'Carpet Area' atau 'Build Area'.
  7.  'Area Locality' : Lokasi rumah/apartemen.
  8.  'City' : Kota dimana rumah/apartemen berada.
  9.  'Furnishing Status' : Status perabotan rumah/apartemen, baik 'Furnished', 'Semi-Furnished' atau 'Unfurnished'.
  10. 'Tenant Preferred' : Jenis penyewa yang diinginkan oleh pemilik atau agen.
  11. 'Bathroom' : Jumlah kamar mandi.
  12. 'Point of Contact' : Kontak yang harus dihubungi untuk informasi lebih lanjut mengenai rumah/apartemen yang disewakan.
      
  Dari kedua belas fitur tersebut, fitur 'Posted On' merupakan fitur yang tidak begitu mempengaruhi harga sewa rumah, sehingga fitur 'Posted On' bisa langsung dihapus.   


* _Explotary Data Analysis_
  *   _Univariate Analysis_
    
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/a5fefd6c-ca66-4a30-aaa5-8b0bde5bc751)

      Gambar 1. Analisis univariat

      Gambar di atas merupakan grafik sebaran analisis univariat untuk setiap fitur numerik yang direpresentasikan secara terpisah. Dari grafik tersebut, informasi yang dapat diambil adalah sebagai berikut :
      1. Rumah yang disewakan memiliki 1 hingga 3 BHK (Bedroom, Hall, Kitchen), dimana jumlah BHK terbanyak adalah 2.
      2. Kebanyakan rumah yang disewakan memiliki ukuran atau luas bangunan di bawah 2000 square feet.
      3. Rumah yang disewakan memiliki 1 hingga 3 kamar mandi, dimana jumlah kamar mandi terbanyak adalah 2.
      4. Harga sewa rumah rata-rata di bawah 30.000.

  *   _Multivariate Analysis_
    
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/887d7a47-5474-4b57-8668-bd4061d93797)
 
      Gambar 2. Analisis multivariat

      Gambar di atas merupakan grafik sebaran analisis multivariat yang menunjukkan hubungan antara dua atau lebih fitur dalam data numerik. Selain itu, hubungan atau korelasi antar fitur data numerik ini dapat dilihat dari matriks _heatmap_ pada Gambar 3.

      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/e2776c15-7d54-4c31-a620-2007bc4c5232)
 
      Gambar 3. Matriks _heatmap_ yang menyatakan korelasi antar fitur data numerik
      
      Dari Gambar 3, semakin terlihat bahwa fitur 'BHK', 'Size' dan 'Bathroom' kurang berkorelasi dengan fitur target, yaitu 'Rent'. Hal ini diduga disebabkan karena kurangnya data dalam penelitian dan diduga pula akan mempengaruhi akurasi dari model yang akan dijalankan. Sedangkan, fitur yang memiliki korelasi tinggi justru terjadi pada fitur 'BHK' dengan fitur 'Bathroom' yang mencapai korelasi 0.73.

  *   Korelasi Antara Fitur Kategorik dengan Fitur Target ('Rent')
    
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/740c0cbb-e783-444c-97b2-375d8584698e)
 
      Gambar 4. Korelasi antara fitur target ('Rent') dengan fitur 'Area Type'
      
      Grafik yang terlihat pada Gambar 4 menunjukan korelasi antara fitur target ('Rent') dengan fitur 'Area Type', dimana tipe area 'Carpet Area' memiliki korelasi yang lebih tinggi dengan fitur 'Rent' jika dibandingkan dengan 'Super Area'.
      
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/057b1ed4-0207-47d4-8ba3-78a3790727f0)

      Gambar 5. Korelasi antara fitur target ('Rent') dengan fitur 'City'
      
      Grafik yang terlihat pada Gambar 5 menunjukan korelasi antara fitur target ('Rent') dengan fitur 'City', dimana kota Mumbai merupakan kota yang paling banyak memiliki rumah yang disewakan. Dengan alasan ini, mendukung pernyataan bahwa korelasi tertinggi antara fitur target ('Rent') dengan fitur 'City' terjadi di kota Mumbai.
 
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/c3ac80ba-80c0-473d-9243-de4ba6cfe824)

      Gambar 6. Korelasi antara fitur target ('Rent') dengan fitur 'Furnishing Status'
      
      Grafik yang terlihat pada Gambar 6 menunjukan korelasi antara fitur target ('Rent') dengan fitur 'Furnishing Status', dimana korelasi tertinggi ditunjukkan oleh status 'Furnished' atau dengan kata lain rumah yang kondisinya disewakan beserta dengan perabotannya akan memiliki harga sewa yang lebih tinggi.
      
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/81a6aeed-e37b-47b4-ba9d-9ff1285e6d50)
 
      Gambar 7. Korelasi antara fitur target ('Rent') dengan fitur 'Tenant Preferred'
      
      Grafik yang terlihat pada Gambar 7 menunjukan korelasi antara fitur target ('Rent') dengan fitur 'Tenant Preferred', dimana korelasi tertinggi ditunjukkan oleh 'Family' atau dengan kata lain rumah yang disewakan untuk sebuah keluarga akan memiliki harga sewa yang lebih tinggi dibandingkan dengan tipe penyewa yang lain.
      
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/97512015-14b7-4f47-a34b-ec0161608e40)

      Gambar 8. Korelasi antara fitur target ('Rent') dengan fitur 'Point of Contact'
      
      Grafik yang terlihat pada Gambar 8 menunjukan korelasi antara fitur target ('Rent') dengan fitur 'Point of Contact', dimana korelasi tertinggi ditunjukkan oleh 'Contact Agent' atau dengan kata lain penyewaan rumah yang membutuhkan pihak ketiga (agen) dalam melancarkan proses transaksinya akan memiliki harga sewa yang lebih tinggi.

# **_Data Preparation_**

Berikut ini merupakan tahapan-tahapan yang dilakukan dalam mempersiapkan data sebelum dilakukan pemodelan.

*   _One Hot Encoding_
  
    _One hot encoding_ adalah sebuah proses yang biasanya dilakukan pada bagian _pre-processing_ yang bertujuan untuk mengubah data kategorik menjadi data numerik dimana setiap kategori unik akan diubah menjadi kolom/parameter baru dengan nilai 0 atau 1 [3]. Pada penelitian ini, fitur yang akan diubah menjadi data numerik adalah fitur 'Area Type', 'City', 'Furnishing Status', 'Tenant Preferred' dan 'Point of Contact'.

*   Pembagian Data Latih dan Data Uji (_Train Test Split_)
  
    _Train test split_ adalah proses penting yang umumnya dilakukan dalam pembelajaran mesin yang digunakan untuk membagi data menjadi data latih dan data uji [4]. Pada penelitian ini, dataset yang ada akan dibagi menjadi 2 bagian yaitu data latih dan data uji dengan rasio 85:15. Sehingga, sebanyak 3508 data latih akan digunakan untuk membangun model, sedangkan 620 data akan digunakan sebagai data uji untuk menguji performa model yang akan dibuat. Proses pembagian data ini dilakukan dengan menggunakan modul train_test_split dari _library_ scikit-learn.
     
*   Normalisasi Data
  
    Algoritma pada pembelajaran mesin akan memiliki performa lebih baik dan bekerja lebih cepat jika dimodelkan dengan data yang seragam. Data seragam yang dimaksud adalah data yang memiliki skala relatif sama. Pada penelitian ini, proses normalisasi data dilakukan dengan menggunakan StandardScaler dari _library_ sklearn.preprocessing.

# **_Modeling_**

Seperti yang telah dijelaskan pada bagian sebelumnya, pada penelitian ini akan dilakukan pemodelan dengan menggunakan 3 algoritma yang berbeda, yaitu _K-Nearest Neighbour_ (KNN), _Random Forest_ dan AdaBoost.

*  _K-Nearest Neighbour_ (KNN)
  
   KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif) yang biasa digunakan untuk kasus klasifikasi dan regresi [5]. Data baru akan diberikan label klasifikasi yang sama dengan mayoritas tetangga terdekatnya jika algoritma digunakan untuk klasifikasi. Jika KNN digunakan untuk regresi, data baru akan diberikan nilai target yang merupakan rata-rata dari nilai target tetangga terdekatnya.

   Kelebihan KNN adalah sederhana dalam konsep, mudah diimplementasikan, dan cocok untuk data yang memiliki pola non-linear [9]. Namun, KNN cenderung lambat dalam mengklasifikasikan data yang besar dan memiliki beberapa kelemahan, seperti sensitif terhadap skala data dan rentan terhadap _outlier_ [9]. 

   Pada penelitian ini, akan digunakan _library_ sklearn.neighbors untuk bisa menjalankan algoritma KNeighborsRegressor. Tahap pertama yang dilakukan adalah menentukan parameter n_neighbors, dimana penulis menggunakan n_neighbors = 14 untuk mendapatkan akurasi yang optimal. Parameter n_neighbors sendiri merupakan jumlah k tetangga tedekat yang merupakan parameter terpenting dalam algoritma KNN. Selanjutnya, untuk membangun model dijalankan perintah
  ```
  knn.fit(X_train, y_train)
  ```

*  _Random Forest_
  
   _Random Forest_ adalah salah satu algoritma _supervised learning_ yang termasuk ke dalam kelompok model _ensemble_ (group) yang disusun dari banyak algoritma pohon (_decision tree_) yang pembagian data dan fiturnya dipilih secara acak [5]. Selama tahap prediksi, setiap pohon memberikan prediksi dan hasil akhir diambil dengan mengambil mayoritas prediksi dari semua pohon (untuk klasifikasi) atau rata-rata prediksi dari semua pohon (untuk regresi).

   Kelebihan dari menggunakan algoritma ini yaitu dapat mengatasi _noise_ dan _missing value_, dapat mengatasi data dalam jumlah yang besar, tidak rentan terhadap _overfitting_, dan dapat memberikan informasi mengenai pentingnya fitur dalam prediksinya [6]. Adapun kekurangan pada algoritma _Random Forest_ yaitu interpretasi yang sulit karena gabungan dari banyak pohon keputusan dan membutuhkan _tuning_ model yang tepat untuk data [6]. 

   Pada penelitian ini, akan digunakan _library_ sklearn.ensemble untuk bisa menjalankan algoritma RandomForestRegressor. Tahap pertama yang dilakukan adalah menentukan parameter n_estimators, max_depth, random_state dan n_jobs.
   
   *  Parameter n_estimators merupakan jumlah trees (pohon) di forest dan penulis menggunakan n_estimator = 50.
   *  Parameter max_depth adalah kedalaman maksimum setiap pohon dimana penulis menggunakan max_depth = 10.
   *  Parameter random_state digunakan untuk mengontrol _random number generator_ yang digunakan dan penulis menggunakan random_state = 40.
   *  Parameter n_jobs adalah jumlah _job_ (pekerjaan) yang digunakan secara paralel. Penulis menggunakan n_jobs = -1 yang artinya semua proses berjalan secara paralel.

   Selanjutnya, setelah seluruh parameter selesai diatur, untuk membangun model _Random Forest_ akan dijalankan perintah
  ```
  rf.fit(X_train, y_train)
  ```

*  AdaBoost
  
   Algoritma _boosting_ bekerja dengan membangun model dari data latih yang kemudian membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama, dimana model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan [5]. Pada awalnya, AdaBoost akan memberikan bobot yang sama pada semua data latih. Kemudian, algoritma akan membangun model lemah pertama dan memberikan bobot yang lebih tinggi pada data yang salah terklasifikasi. Model berikutnya akan difokuskan pada data yang memiliki bobot tinggi, dan proses ini diulang untuk beberapa iterasi atau hingga mencapai batas kesalahan yang diinginkan. Selama tahap prediksi, setiap model lemah akan memberikan prediksi dan bobot yang lebih tinggi diberikan pada model yang memiliki performa lebih baik. Hasil akhir dari algoritma ini adalah hasil prediksi yang diambil dengan bobot terhadap setiap model lemah.

   Kelebihan dari AdaBoost adalah kemampuannya untuk meningkatkan akurasi prediksi, mengurangi _overfitting_, dan dapat digunakan dengan berbagai jenis model lemah [10]. Algoritma ini juga efektif dalam menangani data yang tidak seimbang (_imbalanced data_). Namun, AdaBoost rentan terhadap _noise_ atau _outlier_ [10].

   Pada penelitian ini, akan digunakan _library_ sklearn.ensemble untuk bisa menjalankan algoritma AdaBoostRegressor. Tahap pertama yang dilakukan adalah menentukan parameter n_estimators, max_depth, random_state dan n_jobs.
   
   *  Parameter n_estimators merupakan jumlah maksimum estimator di mana _boosting_ dihentikan dan penulis menggunakan n_estimator = 40.
   *  Parameter learning_rate adalah bobot yang diterapkan pada setiap _regressor_ di masing-masing proses iterasi _boosting_ dimana penulis menggunakan learning_rate = 0.05.
   *  Parameter random_state digunakan untuk mengontrol _random number generator_ yang digunakan dan penulis menggunakan random_state = 5.

   Selanjutnya, setelah seluruh parameter berhasil diatur, untuk membangun model _AdaBoost_ akan dijalankan perintah
  ```
  boosting.fit(X_train, y_train)
  ```

*  Alasan Mengapa Algoritma-algoritma tersebut Dipilih :

   *  KNN : Algoritma KNN dipilih karena kesederhanaan konsepnya, cocok untuk data non-linear, dan tidak memerlukan proses pembelajaran yang kompleks.
   *  _Random Forest_ : _Random Forest_ dipilih karena mampu menangani data yang kompleks dan berdimensi tinggi, mengurangi varians prediksi, dan memiliki kemampuan untuk memberikan informasi pentingnya fitur.
   *  AdaBoost : AdaBoost dipilih karena efektivitasnya dalam meningkatkan performa prediksi, mengurangi _overfitting_, dan kemampuannya dalam menangani data yang tidak seimbang.

# **_Evaluation_**

Pada penelitian ini, proses evaluasi dilakukan dengan menggunakan metrik evaluasi untuk menghitung serta menampilkan hasil akurasi dan mean squared error (MSE) dari model pada masing-masing algoritma yang telah dijalankan. Akurasi adalah ukuran yang menentukan tingkat kemiripan antara hasil prediksi dengan nilai yang sebenarnya (y_test) [7]. Sedangkan _Mean Squared Error_ (MSE) adalah alat ukur untuk mengukur tingkat _error_ yang terjadi dalam model statistik dengan cara menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi [5]. MSE didefinisikan dalam persamaan berikut :

$$ MSE = { \frac {1} {N} \displaystyle\sum_{i=1}^{N} (y_i - ypred_i)^2 } $$

Keterangan:

  N = jumlah dataset

  $$ {y_i} = nilai sebenarnya $$ 
  
  $$ {ypred_i} = nilai prediksi $$ 

* Akurasi yang dihasilkan dari masing-masing algoritma yang telah dijalankan adalah sebagai berikut :
  
    |     KNN    |     RF     |  Boosting  |
    |------------|------------|------------|
    |  0.700835  |  0.762047  |  0.655286  |

    Tabel 1. Tabel akurasi yang dihasilkan dari masing-masing algoritma 

    Dari Tabel 1, dapat dilihat bahwa algoritma KNN memiliki tingkat akurasi sebesar 70.08%, algoritma _Random Forest_ memiliki tingkat akurasi sebesar 76.21% dan algoritma _Boosting_ (AdaBoost) memiliki tingkat akurasi sebesar 65.53%.

* Sedangkan untuk hasil perhitungan MSE pada data latih dan data uji dari masing-masing algoritma akan ditampilkan pada Tabel 2.
  
    |            |     Train     |      Test      |
    |------------|---------------|----------------|
    |     KNN    |  48503.16097  |  56972.672536  |
    |     RF     |  21371.35881  |  45315.587228  |
    |  Boosting  |  58512.40393  |  65647.005189  |

    Tabel 2. Tabel perhitungan MSE pada data latih dan data uji dari masing-masing algoritma

    ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/b9381d31-2989-4dbe-8953-e6c8a5c6bd5e)

    Gambar 9. Grafik perbandingan MSE antara data latih dan data uji pada masing-masing algoritma

    Dari Tabel 2 dan Gambar 9, dapat dilihat bahwa algoritma _Random Forest_ memiliki tingkat _error_ yang lebih rendah jika dibandingkan dengan algoritma lainnya, dengan tingkat _error_ pada data latih sebesar 21371.35881 dan tingkat _error_ pada data uji sebesar 45315.587228.

*  Hasil pengujian prediksi dari masing-masing model
  
    |            |     y_true    |  prediksi_KNN  |   prediksi_RF   |  prediksi_Boosting  |
    |------------|---------------|----------------|-----------------|---------------------|
    |    2735    |     13500     |     21785.7    |     12756.4     |        19640.2      |

    Tabel 3. Hasil pengujian prediksi dari masing-masing model

    Dari Tabel 3, dapat dilihat bahwa hasil prediksi menggunakan algoritma _Random Forest_ adalah hasil yang paling mendekati nilai sebenarnya, walaupun hasil prediksi ini tidak begitu akurat dengan nilai sebenarnya dikarenakan akurasinya yang belum begitu tinggi. 

   Dari data yang telah disajikan, terlihat bahwa algoritma _Random Forest_ memiliki akurasi tertinggi sebesar 76.21% dan tingkat _error_ yang lebih rendah dibandingkan dengan algoritma lainnya pada data latih dan data uji. Hal ini menunjukkan bahwa _Random Forest_ memiliki performa yang lebih baik dalam memprediksi harga sewa rumah di India dibandingkan dengan algoritma-algoritma lain yang digunakan dalam penelitian ini. Meskipun hasil prediksi _Random Forest_ belum sepenuhnya akurat, hasilnya masih lebih mendekati nilai sebenarnya dibandingkan dengan algoritma lainnya. Sebagai hasilnya, algoritma _Random Forest_ dipilih sebagai model utama untuk memprediksi harga sewa rumah di India.

   Dalam analisis komparatif, perlu diperhatikan bahwa setiap algoritma memiliki kelebihan dan kelemahan masing-masing. Misalnya, KNN bisa menjadi pilihan yang baik untuk data non-linear dan sederhana dalam konsepnya. Namun, _Random Forest_ menonjol dalam mengatasi data yang kompleks dan berdimensi tinggi serta mengurangi varians kesalahan prediksi. Di sisi lain, AdaBoost efektif dalam meningkatkan performa prediksi dengan menggabungkan model-model lemah menjadi model yang kuat. Jika interpretasi model menjadi prioritas, KNN bisa menjadi pilihan karena modelnya mudah diinterpretasi. Namun, jika fokus utamanya adalah mendapatkan akurasi dan prediksi terbaik yang mendekati nilai sebenarnya, _Random Forest_ bisa menjadi pilihan yang lebih baik.

# **Kesimpulan**

Penelitian ini bertujuan untuk menganalisis faktor-faktor yang mempengaruhi pemilihan penyewaan rumah dan memprediksi pilihan terbaik penyewaan rumah dengan menggunakan algoritma KNN, _Random Forest_, dan AdaBoost. Dari analisis ini, berhasil diidentifikasi faktor-faktor yang memengaruhi keputusan penyewaan rumah, dan algoritma-algoritma yang diterapkan memberikan prediksi yang memadai. Algoritma _Random Forest_ menunjukkan performa yang paling mendekati nilai sebenarnya dalam memprediksi pilihan terbaik untuk menyewa rumah. 

Meskipun tujuan utama penelitian ini telah tercapai, untuk optimalisasi lebih lanjut, beberapa improvisasi pada model dapat dilakukan untuk meningkatkan kualitas prediksi dan akurasi sehingga dapat memberikan wawasan yang lebih akurat dan relevan bagi perusahaan atau pemilik properti dalam menentukan target penyewa dengan lebih tepat dan efisien.

# **Referensi**

[1]    Suparwoko, Woko. (2013). BAB 3 KEBIJAKAN DAN PRAKTEK PEMBANGUNAN PERUMAHAN SEJUMLAH NEGARA DI ASIA-PASIFIK. 10.13140/2.1.2263.8880. 

[2]    M. Ranjbari, G. Morales-Alonso, and R. Carrasco-Gallego, “Conceptualizing the Sharing Economy through Presenting a Comprehensive Framework,” _Sustainability_, vol. 10, no. 7, p. 2336, Jul. 2018, doi: 10.3390/su10072336. [Online]. Tersedia: [tautan](http://dx.doi.org/10.3390/su10072336). 

[3]    HaloRyan. "One Hot Encoding Pada Python". Tersedia: [tautan](https://haloryan.com/blog/one-hot-encoding-pada-python). Diakses pada 21 Juli 2023.

[4]    QuickTran. "Cara Melakukan Train Test Split dalam Machine Learning". Tersedia: [tautan](https://www.quicktable.io/apps/id/train-test-split/). Diakses pada 21 Juli 2023.

[5]    dicoding. "Rangkuman Studi Kasus Pertama: Predictive Analytics". Tersedia: [tautan](https://www.dicoding.com/academies/319/tutorials/18600). Diakses pada 21 Juli 2023.

[6]    Jurnal UMM. Tersedia: [tautan](https://eprints.umm.ac.id/39299/3/BAB%202.pdf). Diakses pada 21 Juli 2023.

[7]    Santoso, Didik R. (2017). Tim UB Press, Tim UB Press, ed. Pengukuran Stress Mekanik Berbasis Sensor Piezoelektrik: Prinsip Desain dan Implementasi. Malang: UB Press. hlm. 8. ISBN 978-602-432-089-8.

[8]    HRMI Rights Tracker India. "Quality of Life, Economic and Social Rights". Tersedia: [tautan](https://rightstracker.org/country/IND). Diakses pada 24 Juli 2023.

[9]    Medium. "Klasifikasi menggunakan Metode KNN (K-Nearest Neighbor) dalam Python". Tersedia: [tautan](https://medium.com/@16611130/klasifikasi-menggunakan-metode-knn-k-nearest-neighbor-dalam-python-a40e79a74101). Diakses pada 24 Juli 2023.

[10]   Dataaspirant. "Adaboost Algorithm: Boosting Your ML Models to the Next Level". Tersedia: [tautan](https://medium.com/@16611130/klasifikasi-menggunakan-metode-knn-k-nearest-neighbor-dalam-python-a40e79a74101). Diakses pada 24 Juli 2023.
