# **Laporan Proyek Machine Learning Terapan (MLT4) - Submission 1 Predictive Analytics**

Nama : Adita Putri Puspaningrum

---

# **PREDIKSI HARGA RUMAH YANG TERSEDIA UNTUK DISEWAKAN**

# **Domain proyek**

Perumahan di India memiliki beragam jenis kategori, mulai dari istana milik mantan maharaja yang mewah, hingga gedung apartemen modern di kota-kota besar, bahkan gubuk-gubuk di desa-desa terpencil. Tingginya  angka  pertumbuhan  penduduk, adanya urbanisasi berkelanjutan, dan  masih  lemahnya kondisi ekonomi penduduk menyebabkan kesenjangan pemenuhan kebutuhan perumahan di  India meningkat (Suparwoko, 2013). Sehingga masih banyak orang di India yang belum memiliki akses terhadap perumahan yang layak.

Menurut Human Rights Measurement Initiative, India baru mencapai 60,9% dari potensi hak atas perumahan yang semestinya dapat terpenuhi berdasarkan tingkat pendapatan negara tersebut. Artinya, masih banyak orang di India yang tidak bisa memperoleh perumahan yang seharusnya bisa mereka dapatkan.

Salah satu pilihan bagi orang-orang yang belum memiliki rumah adalah menyewa properti, seperti rumah atau toko. Ketika seseorang menyewa, mereka membayar sejumlah uang sebagai imbalan untuk menggunakan properti tersebut sementara waktu. Jenis penyewaan yang ada juga berbeda-beda. Ada yang menyebutnya "sewa kotor" dimana penyewa membayar jumlah sewa tetap, sementara pemilik properti bertanggung jawab atas biaya-biaya lain seperti pajak dan perawatan.

Penyewaan properti ini juga termasuk dalam contoh ekonomi berbagi. Ekonomi berbagi merupakan suatu tindakan modernisasi dari konsumsi kolaboratif di mana orang dapat memanfaatkan properti (dalam kasus ini properti tempat tinggal) milik orang lain untuk memenuhi kebutuhan mereka (Ibnu, 2021).

# **Business Understanding**

Penelitian ini bertujuan untuk menganalisis faktor apa saja yang dapat mempengaruhi pemilihan penyewaan rumah atau tempat tinggal.

*   Problem Statements
    
    Berdasarkan uraian latar belakang masalah yang telah dijelaskan pada bagian sebelumnya, berikut ini merupakan rumusan masalah dari penelitian ini :

    a.   Apa saja faktor yang mempengaruhi pengambilan keputusan untuk menyewa suatu rumah ?
    
    b.   Apa algoritma yang mampu memprediksi pilihan terbaik untuk menyewa suatu rumah ?

*   Goals
  
    Berikut ini merupakan uraian tujuan dari rumusan masalah yang telah dijelaskan :
    
    a.   Menentukan faktor yang mempengaruhi pengambilan keputusan untuk menyewa suatu rumah.
    
    b.   Menentukan algoritma yang mampu memprediksi pilihan terbaik untuk menyewa suatu rumah

*   Solution Statements
  
    Untuk memenuhi tujuan dari penelitian ini, berikut merupakan solusi yang dapat penulis ajukan :
    
    a.   Untuk mengetahui algoritma yang terbaik dalam menentukan pilihan penyewaan rumah, akan dilakukan komparasi terhadap tiga jenis algoritma, yaitu KNN, Random Forest dan AdaBoost.
    
    b.   Setelah ketiga jenis algoritma tersebut berhasil dijalankan, akan dilakukan evaluasi untuk mengukur nilai akurasi pada masing-masing algoritma.

# **Data Understanding**

* Penelitian ini menggunakan dataset yang berjudul House Rent Prediction yang dibuat dari website https://www.magicbricks.com/. Namun, penulis mengambil dataset ini dari Kaggle dengan link : https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset.


* Dataset ini memiliki format CSV (*comma separated value*) yang berjumlah 4.746 data dengan 12 fitur, dimana 8 fitur bertipe *object* sedangkan 4 fitur sisanya bertipe *int64*.


* Variabel-variabel yang terdapat pada dataset 'House Rent Prediction' ini adalah sebagai berikut :
  1.  Posted On : Tanggal data diposting.
  2.  BHK : Jumlah dari kamar tidur, aula, dan dapur.
  3.  Rent : Harga sewa dari rumah/apartemen.
  4.  Size : Ukuran dari rumah/apartemen dalam square feet (sqft).
  5.  Floor : Letak lantai dari apartemen/rumah susun yang disewakan dan jumlah lantai dari bangunan rumah/apartemen tersebut.
  6.  Area Type : Ukuran dari rumah dalam kategori Super Area, Carpet Area atau Build Area.
  7.  Area Locality : Lokasi rumah/apartemen.
  8.  City : Kota dimana rumah/apartemen berada.
  9.  Furnishing Status : Status perabotan rumah/apartemen, baik Furnished, Semi-Furnished atau Unfurnished.
  10. Tenant Preferred : Jenis penyewa yang diinginkan oleh pemilik atau agen.
  11. Bathroom : Jumlah kamar mandi.
  12. Point of Contact : Kontak yang harus dihubungi untuk informasi lebih lanjut mengenai rumah/apartemen yang disewakan.
  Dari kedua belas fitur tersebut, fitur Posted On merupakan fitur yang tidak begitu mempengaruhi harga sewa rumah, sehingga fitur Posted On bisa langsung dihapus.   


* Explotary Data Analysis
  *   Univariate Analysis
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/a5fefd6c-ca66-4a30-aaa5-8b0bde5bc751)

      Gambar di atas merupakan grafik sebaran analisis univariat untuk setiap fitur numerik yang direpresentasikan secara terpisah. Dari grafik tersebut, kita bisa mengambil data bahwa :
      1. Rumah yang disewakan memiliki 1 hingga 3 BHK (Bedroom, Hall, Kitchen), dimana jumlah BHK terbanyak adalah 2.
      2. Kebanyakan rumah yang disewakan memiliki ukuran atau luas bangunan di bawah 2000 square feet.
      3. Rumah yang disewakan memiliki 1 hingga 3 kamar mandi, dimana jumlah kamar mandi terbanyak adalah 2.
      4. Harga sewa rumah rata-rata di bawah 30.000.

  *   Multivariate Analysis
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/887d7a47-5474-4b57-8668-bd4061d93797)

      Gambar di atas merupakan grafik sebaran analisis multivariat yang menunjukkan hubungan antara dua atau lebih fitur dalam data numerik. Selain itu, hubungan atau korelasi antar fitur data numerik ini juga bisa dilihat dari matriks heatmap seperti gambar di bawah ini.

      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/e2776c15-7d54-4c31-a620-2007bc4c5232)
      
      Dari matriks heatmap tersebut, semakin terlihat bahwa fitur BHK, Size dan Bathroom kurang berkorelasi dengan fitur target, yaitu Rent. Hal ini diduga disebabkan karena kurangnya data dalam penelitian dan diduga pula akan mempengaruhi akurasi dari model yang akan dijalankan. Sedangkan, fitur yang memiliki korelasi tinggi justru terjadi pada fitur BHK dengan fitur Bathroom yang mencapai korelasi 0.73.

  *   Korelasi Antara Fitur Kategorik dengan Fitur Target (Rent)
    
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/740c0cbb-e783-444c-97b2-375d8584698e)
      
      Grafik di atas menunjukan korelasi antara fitur target (Rent) dengan fitur Area Type, dimana tipe area 'Carpet Area' memiliki korelasi yang lebih tinggi dengan fitur Rent jika dibandingkan dengan 'Super Area'.
      
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/057b1ed4-0207-47d4-8ba3-78a3790727f0)
      
      Grafik di atas menunjukan korelasi antara fitur target (Rent) dengan fitur City, dimana kota Mumbai merupakan kota yang paling banyak memiliki rumah yang disewakan. Dengan alasan ini, mendukung pernyataan bahwa korelasi tertinggi antara fitur target (Rent) dengan fitur City terjadi di kota Mumbai.
 
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/c3ac80ba-80c0-473d-9243-de4ba6cfe824)
      
      Grafik di atas menunjukan korelasi antara fitur target (Rent) dengan fitur Furnishing Status, dimana korelasi tertinggi ditunjukkan oleh status 'Furnished' atau dengan kata lain rumah yang kondisinya disewakan beserta dengan perabotannya akan memiliki harga sewa yang lebih tinggi.
      
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/81a6aeed-e37b-47b4-ba9d-9ff1285e6d50)
      
      Grafik di atas menunjukan korelasi antara fitur target (Rent) dengan fitur Tenant Preferred, dimana korelasi tertinggi ditunjukkan oleh 'Family' atau dengan kata lain rumah yang disewakan untuk sebuah keluarga akan memiliki harga sewa yang lebih tinggi dibandingkan dengan tipe penyewa yang lain.
      
      ![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/97512015-14b7-4f47-a34b-ec0161608e40)
      
      Grafik di atas menunjukan korelasi antara fitur target (Rent) dengan fitur Point of Contact, dimana korelasi tertinggi ditunjukkan oleh 'Contact Agent' atau dengan kata lain penyewaan rumah yang membutuhkan pihak ketiga (agen) dalam melancarkan proses transaksinya akan memiliki harga sewa yang lebih tinggi.

# **Data Preparation**
Berikut ini merupakan tahapan-tahapan yang dilakukan dalam mempersiapkan data sebelum dilakukan pemodelan.

*   One Hot Encoding
    One hot encoding adalah sebuah proses yang biasanya dilakukan pada bagian pre-processing yang bertujuan untuk mengubah data kategorik menjadi data numerik dimana setiap kategori unik akan diubah menjadi kolom/parameter baru dengan nilai 0 atau 1 (Ryan, 2021). Pada penelitian ini, fitur yang akan diubah menjadi data numerik adalah fitur Area Type, City, Furnishing Status, Tenant Preferred dan Point of Contact.

*   Pembagian Data Latih dan Data Uji (Train Test Split)
    Train test split adalah proses penting yang umumnya dilakukan dalam pembelajaran mesin yang digunakan untuk membagi data menjadi data latih dan data uji (TridentData, 2022). Pada penelitian ini, dataset yang ada akan dibagi menjadi 2 bagian yaitu data latih dan data uji dengan rasio 85:15. Sehingga, sebanyak 3508 data latih akan digunakan untuk membangun model, sedangkan 620 data akan digunakan sebagai data uji untuk menguji performa model yang akan dibuat. Proses pembagian data ini dilakukan dengan menggunakan modul train_test_split dari library scikit-learn.
     
*   Normalisasi Data
    Algoritma pada pembelajaran mesin akan memiliki performa lebih baik dan bekerja lebih cepat jika dimodelkan dengan data yang seragam. Data seragam yang dimaksud adalah data yang memiliki skala relatif sama. Pada penelitian ini, proses normalisasi data dilakukan dengan menggunakan StandardScaler dari library sklearn.preprocessing.

# **Modeling**

Seperti yang telah dijelaskan pada bagian sebelumnya, pada penelitian ini akan dilakukan pemodelan dengan menggunakan 3 algoritma yang berbeda, yaitu K-Nearest Neighbour (KNN), Random Forest dan AdaBoost.

*  K-Nearest Neighbour (KNN)
   KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif) yang biasa digunakan untuk kasus klasifikasi dan regresi (Dicoding, 2023). Pada penelitian ini, akan digunakan library sklearn.neighbors untuk bisa menjalankan algoritma KNeighborsRegressor. Tahap pertama yang dilakukan adalah menentukan parameter n_neighbors, dimana penulis menggunakan n_neighbors = 14 untuk mendapatkan akurasi yang optimal. Parameter n_neighbors sendiri merupakan jumlah k tetangga tedekat yang merupakan parameter terpenting dalam algoritma KNN. Selanjutnya, untuk membangun model dijalankan perintah
  ```
  knn.fit(X_train, y_train)
  ```

*  Random Forest
   Random forest adalah salah satu algoritma supervised learning yang termasuk ke dalam kelompok model ensemble (group) yang disusun dari banyak algoritma pohon (decision tree) yang pembagian data dan fiturnya dipilih secara acak (Dicoding, 2023). Kelebihan dari menggunakan algoritma ini yaitu dapat mengatasi noise dan missing value serta dapat mengatasi data dalam jumlah yang besar, adapun kekurangan pada algoritma Random Forest yaitu interpretasi yang sulit dan membutuhkan tuning model yang tepat untuk data (UMM, 2023). Pada penelitian ini, akan digunakan library sklearn.ensemble untuk bisa menjalankan algoritma RandomForestRegressor. Tahap pertama yang dilakukan adalah menentukan parameter n_estimators, max_depth, random_state dan n_jobs.
   *  Parameter n_estimators merupakan jumlah trees (pohon) di forest dan penulis menggunakan n_estimator = 50.
   *  Parameter max_depth adalah kedalaman maksimum setiap tree dimana penulis menggunakan max_depth = 10.
   *  Parameter random_state digunakan untuk mengontrol random number generator yang digunakan dan penulis menggunakan random_state = 40.
   *  Parameter n_jobs adalah jumlah job (pekerjaan) yang digunakan secara paralel. Penulis menggunakan n_jobs = -1 yang artinya semua proses berjalan secara paralel.

   Selanjutnya, setelah seluruh parameter di-set, untuk membangun model random forest akan dijalankan perintah
  ```
  rf.fit(X_train, y_train)
  ```

*  AdaBoost
   Algoritma boosting bekerja dengan membangun model dari data latih yang kemudian membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama, dimana model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan (Dicoding, 2023). Pada penelitian ini, akan digunakan library sklearn.ensemble untuk bisa menjalankan algoritma AdaBoostRegressor. Tahap pertama yang dilakukan adalah menentukan parameter n_estimators, max_depth, random_state dan n_jobs.
   *  Parameter n_estimators merupakan jumlah maksimum estimator di mana boosting dihentikan dan penulis menggunakan n_estimator = 40.
   *  Parameter learning_rate adalah bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi boosting dimana penulis menggunakan learning_rate = 0.05.
   *  Parameter random_state digunakan untuk mengontrol random number generator yang digunakan dan penulis menggunakan random_state = 5.

   Selanjutnya, setelah seluruh parameter di-set, untuk membangun model AdaBoost akan dijalankan perintah
  ```
  boosting.fit(X_train, y_train)
  ```

# **Evaluation**

Pada penelitian ini, proses evaluasi dilakukan dengan menggunakan metrik evaluasi untuk menghitung serta menampilkan hasil akurasi dan mean squared error (MSE) dari model pada masing-masing algoritma yang telah dijalankan. Akurasi adalah ukuran yang menentukan tingkat kemiripan antara hasil prediksi dengan nilai yang sebenarnya (y_test) (Wikipedia, 2022). Sedangkan Mean squared error (MSE) adalah alat ukur untuk mengukur tingkat error yang terjadi dalam model statistik dengan cara menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi (Dicoding, 2023). MSE didefinisikan dalam persamaan berikut :
![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/fc2ab7d7-fdc7-4a59-9b27-eb6eb55e20b4)

Keterangan:
  N = jumlah dataset
  yi = nilai sebenarnya
  y_pred = nilai prediksi

* Akurasi yang dihasilkan dari masing-masing algoritma yang telah dijalankan adalah sebagai berikut :
![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/bb2907f6-89a8-47fa-9587-3f5e29f3a462)

Dengan akurasi tertinggi dihasilkan oleh algoritma Random Forest dengan tingkat akurasi sebesar 76.2%.

* Sedangkan untuk hasil perhitungan MSE akan ditampilkan pada gambar di bawah ini :
![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/985e1d60-60a9-4f9a-b9e2-32598a70a0a2)

![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/b9381d31-2989-4dbe-8953-e6c8a5c6bd5e)

Dapat dilihat bahwa algoritma Random Forest memiliki tingkat error yang lebih rendah jika dibandingkan dengan algoritma lainnya, dengan tingkat error pada data latih sebesar 21371.358809 dan tingkat error pada data uji sebesar 45315.587228.

*  Hasil pengujian prediksi dari masing-masing model
![image](https://github.com/racheladita/Laporan-Proyek-Machine-Learning-Terapan-MLT4---Submission-1-Predictive-Analytics/assets/77524477/0f33218d-d35b-4403-8081-f34284ab32be)

Dapat dilihat bahwa hasil prediksi menggunakan algoritma Random Forest adalah hasil yang paling mendekati nilai sebenarnya meskipun hasil prediksi ini tidak begitu akurat dengan nilai sebenarnya dikarenakan akurasinya yang belum begitu tinggi. Oleh karena itu, algoritma Random Forest dipilih sebagai model utama yang digunakan untuk memprediksi harga sewa rumah di India.

# **Referensi**

accurate.id. (2021, 11 Januari). Sharing Economy: Pengertian, Konsep, Kelebihan dan Kekurangannya. Diakses pada 20 Juli 2023, dari https://accurate.id/ekonomi-keuangan/sharing-economy/

dicoding.com. (2023). Rangkuman Studi Kasus Pertama: Predictive Analytics. Diakses pada 21 Juli 2023, dari https://www.dicoding.com/academies/319/tutorials/18600

haloryan.com. (2021, 14 Desember). One Hot Encoding Pada Python. Diakses pada 21 Juli 2023, dari https://haloryan.com/blog/one-hot-encoding-pada-python

id.wikipedia.org. (2022, 25 Januari). Akurasi. Diakses pada 21 Juli 2023, dari https://id.wikipedia.org/wiki/

quicktable.io. (2022). Cara Melakukan Train Test Split dalam Machine Learning. Diakses pada 21 Juli 2023, dari https://www.quicktable.io/apps/id/train-test-split/

Suparwoko, Woko. 2013. PENINGKATAN KAPASITAS PERUMAHAN SWADAYA DI INDONESIA. Jurnal Universitas Islam Indonesia. 56-52. https://www.researchgate.net/publication/272357548_BAB_3_KEBIJAKAN_DAN_PRAKTEK_PEMBANGUNAN_PERUMAHAN_SEJUMLAH_NEGARA_DI_ASIA-PASIFIK

Jurnal UMM, 2023. https://eprints.umm.ac.id/39299/3/BAB%202.pdf
