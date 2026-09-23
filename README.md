# Praktikum_PBO_B2-25

Sistem Pengelolaan Layanan Perawatan Sepatu
1. Deskripsi Program

Program Sistem Pengelolaan Layanan Perawatan Sepatu (ShoeCare) merupakan program berbasis Python yang dibuat untuk mengelola data layanan perawatan sepatu, pelanggan, dan pesanan.

Program ini menerapkan konsep Pemrograman Berorientasi Objek (PBO) dengan menggunakan beberapa class yang saling berhubungan, yaitu LayananPerawatan, Pelanggan, dan Pesanan.

Program dapat digunakan untuk membuat data layanan, menyimpan data pelanggan, membuat pesanan, menghitung total biaya, mengubah status pesanan, serta melakukan validasi data.

2. Tujuan Program

Program ini dibuat untuk:

Menerapkan konsep Pemrograman Berorientasi Objek menggunakan Python.
Menggunakan class, object, attribute, dan method.
Menerapkan encapsulation menggunakan private attribute.
Menerapkan getter dan setter.
Menerapkan class method dan static method.
Melakukan validasi terhadap data yang dimasukkan.
Mengelola layanan, pelanggan, dan pesanan secara terstruktur.
3. Struktur Class

Program memiliki 3 class utama:

ShoeCare
│
├── LayananPerawatan
│   ├── Attribute
│   ├── Getter & Setter
│   ├── Instance Method
│   ├── Class Method
│   └── Static Method
│
├── Pelanggan
│   ├── Attribute
│   ├── Getter & Setter
│   ├── Instance Method
│   ├── Class Method
│   └── Static Method
│
└── Pesanan
    ├── Attribute
    ├── Getter & Setter
    ├── Instance Method
    ├── Class Method
    └── Static Method
4. Penjelasan Class
A. Class LayananPerawatan

Class LayananPerawatan digunakan untuk menyimpan dan mengelola informasi layanan perawatan sepatu.

Data yang digunakan meliputi nama layanan, harga, dan estimasi waktu pengerjaan.

Class ini juga memiliki validasi harga agar harga tidak bernilai negatif.

Contoh layanan yang digunakan:

Deep Cleaning
Repaint
B. Class Pelanggan

Class Pelanggan digunakan untuk menyimpan data pelanggan ShoeCare.

Data pelanggan terdiri dari nama, nomor HP, dan alamat.

Nomor HP menggunakan private attribute dan memiliki validasi agar nomor yang dimasukkan berupa angka dengan panjang 10–13 digit.

Contoh data pelanggan:

Aditya
Budi
C. Class Pesanan

Class Pesanan digunakan untuk mengelola transaksi atau pesanan pelanggan.

Class ini menghubungkan data pelanggan dengan layanan yang dipilih.

Fungsi yang terdapat pada class ini antara lain:

Membuat pesanan.
Menentukan jumlah layanan.
Menghitung total biaya.
Mengubah status pesanan.
Menampilkan informasi pesanan.

Status pesanan yang tersedia:

Menunggu
Diproses
Selesai
Diambil
5. Konsep PBO yang Digunakan
Encapsulation

Encapsulation digunakan untuk membatasi akses langsung terhadap data tertentu.

Contohnya:

self.__harga
self.__nomor_hp
self.__jumlah

Data tersebut diakses melalui getter dan diubah melalui setter.

Getter dan Setter

Getter digunakan untuk mengambil nilai attribute, sedangkan setter digunakan untuk mengubah nilai attribute sekaligus melakukan validasi.

Contohnya:

layanan1.harga
layanan1.harga = 55000
Instance Method

Instance method digunakan untuk menjalankan fungsi yang berhubungan dengan object.

Contohnya:

tampilkan_info()
tampilkan_data()
hitung_total()
tampilkan_pesanan()
Class Method

Class method digunakan untuk membuat object dari data tertentu atau mengakses informasi yang berhubungan dengan class.

Contohnya:

LayananPerawatan.dari_dict()
Pelanggan.dari_dict()
Pesanan.buat_pesanan()
Static Method

Static method digunakan untuk melakukan validasi yang tidak bergantung pada object tertentu.

Contohnya:

LayananPerawatan.validasi_harga()
Pelanggan.validasi_nomor_hp()
Pesanan.validasi_status()

6. Cara Menjalankan Program

Masuk ke folder program:

cd posttest1_PBO

Kemudian jalankan:

python main.py

7. Panduan Pengujian

Program dapat diuji dengan beberapa bagian berikut.

1. Pengujian Object

Program membuat object dari masing-masing class:

layanan1 = LayananPerawatan(...)
pelanggan1 = Pelanggan(...)
pesanan1 = Pesanan(...)

Tujuannya untuk memastikan object berhasil dibuat.

2. Pengujian Getter

Getter digunakan untuk mengambil data private attribute.

Contohnya:

print(layanan1.harga)
print(pelanggan1.nomor_hp)
print(pesanan1.jumlah)
3. Pengujian Setter Valid

Program mengubah data menggunakan nilai yang benar.

Contohnya:

layanan1.harga = 55000
pelanggan1.nomor_hp = "081298765432"
pesanan1.jumlah = 2

Data berhasil diubah karena memenuhi validasi.

4. Pengujian Setter Tidak Valid

Program juga menguji data yang tidak sesuai.

Contohnya:

layanan1.harga = -5000
pelanggan1.nomor_hp = "123"
pesanan1.jumlah = 0

Program akan menghasilkan ValueError karena data tidak memenuhi ketentuan.

5. Pengujian Status Pesanan

Status pesanan diuji dengan status yang tersedia:

pesanan1.ubah_status("Diproses")

Status berhasil berubah dari Menunggu menjadi Diproses.

6. Pengujian Perhitungan Total

Program menghitung total berdasarkan:

Harga layanan × Jumlah

Contohnya:

Rp55.000 × 2 = Rp110.000