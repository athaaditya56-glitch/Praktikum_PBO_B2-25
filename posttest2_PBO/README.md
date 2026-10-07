
 POSTTEST 2 


 1. Deskripsi Program

Program ini merupakan **Sistem Pengelolaan Pelayanan Perawatan Sepatu** dengan tema **ShoeCare**. Program digunakan untuk menggambarkan proses pemilihan layanan perawatan sepatu, pengelolaan pelanggan, pembuatan pesanan, dan pembayaran.

Pada Posttest 2, program difokuskan pada materi **Inheritance** dan penerapan tiga relasi UML yang telah dipelajari, yaitu:

- Asosiasi
- Agregasi
- Komposisi

Program juga menerapkan konsep **Superclass dan Subclass**, penggunaan `super().__init__()`, atribut protected dan private, atribut khusus pada subclass, serta **method overriding**.

---

2. Tujuan Program

Tujuan pembuatan program ini adalah:

1. Menerapkan konsep **inheritance** pada Python.
2. Membuat satu superclass dan minimal dua subclass.
3. Menggunakan `super().__init__()` pada constructor subclass.
4. Menerapkan atribut **protected (`_nama`)** dan **private (`__nama`)**.
5. Menerapkan **method overriding** pada subclass.
6. Menerapkan relasi **asosiasi, agregasi, dan komposisi**.
7. Menunjukkan hasil pengujian konsep OOP melalui program utama.

---

3. Struktur Class

Program terdiri dari enam class utama:

```text
LayananPerawatan
├── DeepCleaning
└── Repaint

Pelanggan
Pesanan
Pembayaran
```

Daftar Class

| Class | Peran |
|---|---|
| `LayananPerawatan` | Superclass yang menyimpan atribut dan method dasar layanan |
| `DeepCleaning` | Subclass untuk layanan deep cleaning |
| `Repaint` | Subclass untuk layanan repaint |
| `Pelanggan` | Menyimpan data pelanggan dan daftar pesanan |
| `Pesanan` | Mengelola pesanan pelanggan dan perhitungan total |
| `Pembayaran` | Mengelola metode, nominal, dan status pembayaran |

---

 4. Penjelasan Inheritance

 4.1 Superclass

Superclass yang digunakan adalah `LayananPerawatan`.

```python
class LayananPerawatan:
```

Class ini menjadi class induk yang memiliki atribut dan method dasar yang dapat diwariskan kepada subclass.

Atribut utama pada superclass yaitu:

```python
self._nama_layanan
self._harga
self.estimasi_hari
self.__kode_layanan
```

Method utama pada superclass yaitu:

```python
harga
hitung_harga()
tampilkan_info()
validasi_harga()
```

---

 4.2 Subclass DeepCleaning

`DeepCleaning` merupakan subclass dari `LayananPerawatan`.

```python
class DeepCleaning(LayananPerawatan):
```

Hubungannya adalah:

> **DeepCleaning adalah jenis LayananPerawatan.**

Subclass menggunakan constructor superclass dengan:

```python
super().__init__(
    nama_layanan,
    harga,
    estimasi_hari
)
```

Subclass juga memiliki atribut khusus:

```python
self.jenis_cairan = jenis_cairan
```

Atribut tersebut membedakan `DeepCleaning` dari superclass dan subclass lainnya.

---

 4.3 Subclass Repaint

`Repaint` juga merupakan subclass dari `LayananPerawatan`.

```python
class Repaint(LayananPerawatan):
```

Hubungannya adalah:

> **Repaint adalah jenis LayananPerawatan.**

Constructor subclass memanggil constructor superclass menggunakan:

```python
super().__init__(
    nama_layanan,
    harga,
    estimasi_hari
)
```

Subclass memiliki atribut khusus:

```python
self.warna_baru = warna_baru
```

Atribut ini menunjukkan warna baru yang dipilih untuk layanan repaint.

---

 5. Penggunaan `super()`

Program menggunakan `super()` pada subclass untuk memanggil constructor milik superclass.

Contoh pada `DeepCleaning`:

```python
super().__init__(
    nama_layanan,
    harga,
    estimasi_hari
)
```

Contoh pada `Repaint`:

```python
super().__init__(
    nama_layanan,
    harga,
    estimasi_hari
)
```

Selain constructor, `Repaint` juga menggunakan:

```python
harga_dasar = super().hitung_harga(jumlah)
```

Hal ini digunakan agar perhitungan dasar dari superclass tetap digunakan sebelum ditambahkan biaya khusus repaint.

---

 6. Method Overriding

Superclass memiliki method:

```python
def hitung_harga(self, jumlah):
    return self._harga * jumlah
```

Method tersebut kemudian di-override pada `Repaint`:

```python
def hitung_harga(self, jumlah):
    harga_dasar = super().hitung_harga(jumlah)
    biaya_cat = 20000
    return harga_dasar + biaya_cat
```

Pada layanan `Repaint`, harga dihitung dari harga dasar dikali jumlah sepatu kemudian ditambah biaya cat sebesar Rp20.000.

Dengan demikian, method yang memiliki nama sama dapat menghasilkan perilaku yang berbeda sesuai subclass yang digunakan.

---

 7. Protected dan Private

 7.1 Protected

Program menggunakan atribut protected pada `LayananPerawatan`:

```python
self._nama_layanan
self._harga
```

Atribut tersebut digunakan oleh subclass, misalnya:

```python
self._nama_layanan
self._harga
```

Protected dipilih karena data tersebut masih dibutuhkan oleh subclass.

 7.2 Private

Program menggunakan atribut private:

```python
self.__kode_layanan
```

Atribut private digunakan untuk data yang bersifat internal pada superclass.

Pada class `Pelanggan` juga terdapat:

```python
self.__nomor_hp
```

yang diakses melalui getter dan setter:

```python
@property
def nomor_hp(self):
    return self.__nomor_hp
```

dan:

```python
@nomor_hp.setter
def nomor_hp(self, nomor_baru):
```

---

 8. Relasi UML

 8.1 Asosiasi

Asosiasi digunakan pada hubungan **Pelanggan dengan LayananPerawatan**.

Hubungannya adalah:

> **Pelanggan menggunakan LayananPerawatan.**

Implementasi pada program:

```python
def pilih_layanan(self, layanan):
    print(
        self.nama,
        "memilih layanan",
        layanan._nama_layanan
    )
```

Contoh penggunaan:

```python
pelanggan1.pilih_layanan(deep_cleaning)
pelanggan2.pilih_layanan(repaint)
```

Objek layanan diberikan melalui parameter method. Artinya `Pelanggan` hanya menggunakan objek layanan tersebut.

Notasi UML:

```text
Pelanggan ..> LayananPerawatan
```

---

 8.2 Agregasi

Agregasi digunakan pada hubungan **Pelanggan dengan Pesanan**.

Hubungannya adalah:

> **Pelanggan memiliki atau menampung Pesanan.**

Pada class `Pelanggan` terdapat:

```python
self.daftar_pesanan = []
```

Kemudian pesanan yang sudah dibuat di luar class dimasukkan menggunakan:

```python
def tambah_pesanan(self, pesanan):
    self.daftar_pesanan.append(pesanan)
```

Contoh:

```python
pelanggan1.tambah_pesanan(pesanan1)
pelanggan2.tambah_pesanan(pesanan2)
```

Notasi UML:

```text
Pelanggan O-- Pesanan
```

---

 8.3 Komposisi

Komposisi digunakan pada hubungan **Pesanan dengan Pembayaran**.

Hubungannya adalah:

> **Pesanan terdiri dari Pembayaran.**

Objek `Pembayaran` dibuat langsung di dalam constructor `Pesanan`:

```python
self.pembayaran = Pembayaran(
    metode_pembayaran,
    total
)
```

Karena `Pembayaran` dibuat sebagai bagian dari `Pesanan`, maka hubungan tersebut digunakan sebagai komposisi.

Notasi UML:

```text
Pesanan *-- Pembayaran
```

---

 9. Diagram Struktur Relasi

```text
                     LayananPerawatan
                            ▲
                   ┌────────┴────────┐
                   │                 │
             DeepCleaning          Repaint
             <<Subclass>>          <<Subclass>>


Pelanggan ..> LayananPerawatan
     Asosiasi / menggunakan


Pelanggan O-- Pesanan
     Agregasi / menampung


Pesanan *-- Pembayaran
     Komposisi / terdiri dari
```

Keterangan:

- `..>` = Asosiasi
- `O--` = Agregasi
- `*--` = Komposisi
- `▲` = arah pewarisan menuju superclass

---

 10. Fitur Program

Program memiliki beberapa fitur utama:

1. Menampilkan informasi layanan `DeepCleaning` dan `Repaint`.
2. Menampilkan data pelanggan.
3. Pelanggan dapat memilih layanan.
4. Membuat pesanan pelanggan.
5. Menghitung total harga berdasarkan jenis layanan.
6. Menambahkan biaya khusus pada layanan `Repaint`.
7. Mengelola data pembayaran.
8. Mengubah status pembayaran menjadi `Lunas`.
9. Mengubah status pesanan menjadi `Diproses`.
10. Menguji getter dan setter harga.
11. Menguji atribut protected dan private.
12. Menguji hubungan inheritance menggunakan `isinstance()` dan `issubclass()`.
13. Menampilkan atribut kelas seperti total layanan, total pelanggan, dan total pesanan.

---

 11. Panduan Pengujian Program

 11.1 Persiapan

Pastikan Python sudah terpasang pada komputer.

Simpan program dengan nama file, misalnya:

```text
main.py
```

---

 11.2 Menjalankan Program

Buka terminal atau PowerShell pada folder tempat file disimpan.

Jalankan perintah:

```bash
python main.py
```

Jika menggunakan perintah Python lain sesuai instalasi komputer, dapat menggunakan:

```bash
py main.py
```

---

 12. Pengujian Inheritance

Pada program utama terdapat pengujian:

```python
print(
    "DeepCleaning adalah LayananPerawatan :",
    isinstance(
        deep_cleaning,
        LayananPerawatan
    )
)
```

dan:

```python
print(
    "Repaint subclass LayananPerawatan     :",
    issubclass(
        Repaint,
        LayananPerawatan
    )
)
```

Hasil yang diharapkan:

```text
DeepCleaning adalah LayananPerawatan : True
Repaint adalah LayananPerawatan       : True
DeepCleaning subclass LayananPerawatan: True
Repaint subclass LayananPerawatan     : True
```

Hasil `True` menunjukkan bahwa kedua class tersebut merupakan subclass dari `LayananPerawatan`.

---

 13. Pengujian Method Overriding

Jalankan bagian:

```python
deep_cleaning.hitung_harga(2)
repaint.hitung_harga(1)
```

Dengan data:

```text
Deep Cleaning = Rp50.000
Repaint       = Rp75.000
Biaya cat     = Rp20.000
```

Hasil yang diharapkan:

```text
Harga Deep Cleaning 2 sepatu : Rp100.000
Harga Repaint 1 sepatu       : Rp95.000
```

Perbedaan hasil menunjukkan bahwa method `hitung_harga()` pada `Repaint` menjalankan perilaku yang berbeda dari superclass.

---

 14. Pengujian Asosiasi

Bagian yang diuji:

```python
pelanggan1.pilih_layanan(deep_cleaning)
pelanggan2.pilih_layanan(repaint)
```

Hasil yang diharapkan:

```text
Aditya memilih layanan Deep Cleaning
Budi memilih layanan Repaint
```

Hal tersebut menunjukkan bahwa objek `Pelanggan` berinteraksi dengan objek `LayananPerawatan`.

---

 15. Pengujian Agregasi

Bagian yang diuji:

```python
pelanggan1.tambah_pesanan(pesanan1)
pelanggan2.tambah_pesanan(pesanan2)
```

Hasil yang diharapkan:

```text
Jumlah pesanan Aditya : 1
Jumlah pesanan Budi : 1
```

Hal tersebut menunjukkan bahwa `Pelanggan` menampung objek `Pesanan` dalam `daftar_pesanan`.

---

 16. Pengujian Komposisi

Pada saat objek `Pesanan` dibuat, objek `Pembayaran` langsung dibuat di dalam constructor `Pesanan`.

```python
self.pembayaran = Pembayaran(
    metode_pembayaran,
    total
)
```

Kemudian pembayaran dapat ditampilkan dengan:

```python
pesanan1.pembayaran.tampilkan_pembayaran()
```

Hasil yang diharapkan sebelum pembayaran diproses:

```text
Metode Pembayaran : QRIS
Nominal           : Rp100.000
Status             : Belum Dibayar
```

Setelah menjalankan:

```python
pesanan1.pembayaran.proses_pembayaran()
```

Hasil menjadi:

```text
Pembayaran Rp100.000 melalui QRIS berhasil.
```

dan status berubah menjadi:

```text
Lunas
```

---

 17. Pengujian Getter dan Setter

Harga awal `DeepCleaning` adalah Rp50.000.

Getter diuji dengan:

```python
print(deep_cleaning.harga)
```

Kemudian setter diuji dengan:

```python
deep_cleaning.harga = 55000
```

Hasil yang diharapkan:

```text
Harga awal : Rp50.000
Harga setelah setter : Rp55.000
```

---

 18. Pengujian Protected dan Private

Protected diuji menggunakan atribut:

```python
deep_cleaning._nama_layanan
deep_cleaning._harga
```

Hasil menampilkan data layanan yang diwarisi dari superclass.

Private digunakan pada:

```python
self.__kode_layanan
```

dan:

```python
self.__nomor_hp
```

Atribut private tidak diakses secara langsung dari luar class, tetapi `nomor_hp` digunakan melalui getter dan setter.

---

 19. Pengujian Status Pesanan

Status awal pesanan adalah:

```text
Menunggu
```

Kemudian diuji dengan:

```python
pesanan1.ubah_status("Diproses")
```

Hasil yang diharapkan:

```text
Status Pesanan 1 : Diproses
```