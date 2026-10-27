# POSTTEST 3

## 1. Deskripsi Program

Program ini merupakan **Sistem Pengelolaan Pelayanan Perawatan Sepatu** dengan tema **ShoeCare**. Program digunakan untuk menggambarkan proses pendataan pelanggan dan sepatu, pemilihan layanan perawatan, pembuatan pesanan, pemrosesan layanan, dan pengiriman notifikasi ketika pesanan selesai.

Pada Posttest 3, program difokuskan pada materi **Abstraksi** dan **Polimorfisme**, serta penerapan tiga relasi UML yang telah dipelajari, yaitu:

- Asosiasi
- Agregasi
- Komposisi

Program juga menerapkan **Abstract Base Class (ABC)**, **method overriding**, **duck typing**, **operator overloading**, dan prinsip **SOLID** (OCP dan DIP) sebagai poin plus.

---

## 2. Tujuan Program

Tujuan pembuatan program ini adalah:

1. Menggambarkan relasi antar class dalam bentuk **Class Diagram**.
2. Menerapkan relasi **asosiasi, agregasi, dan komposisi** yang benar-benar ada di kode program.
3. Membuat minimal satu **abstract class** dengan `ABC` dan minimal dua `@abstractmethod`.
4. Membuat minimal dua subclass yang mengimplementasikan seluruh abstract method.
5. Menunjukkan bahwa abstract class **tidak dapat diinstansiasi**.
6. Menerapkan **polimorfisme** melalui pewarisan, duck typing, dan operator overloading.
7. Menghindari anti-pattern berupa rantai `if/elif` yang mengecek `type()` atau string jenis.
8. Menerapkan minimal satu prinsip **SOLID**.

---

## 3. Struktur Class

Program terdiri dari sepuluh class:

```text
Layanan (abstract)
├── CuciBiasa
├── DeepClean
└── Repaint

Pelanggan
Sepatu
Pesanan
ItemPesanan

NotifikasiWhatsApp
NotifikasiEmail
```

### Daftar Class

| Class | Peran |
|---|---|
| `Layanan` | Abstract class yang mendefinisikan kontrak layanan perawatan |
| `CuciBiasa` | Subclass layanan cuci biasa |
| `DeepClean` | Subclass layanan deep clean (biaya naik sesuai tingkat kotor) |
| `Repaint` | Subclass layanan repaint (biaya naik sesuai jumlah bagian rusak) |
| `Pelanggan` | Menyimpan data pelanggan dan daftar sepatu miliknya |
| `Sepatu` | Menyimpan data sepatu (merek, jenis, tingkat kotor, bagian rusak) |
| `Pesanan` | Mengelola pesanan, menghitung total, dan memproses layanan |
| `ItemPesanan` | Satu baris pesanan yang berisi pasangan sepatu dan layanan |
| `NotifikasiWhatsApp` | Mengirim notifikasi lewat WhatsApp |
| `NotifikasiEmail` | Mengirim notifikasi lewat email |

---

## 4. Class Diagram

![Class Diagram](class_diagram.png)

Keterangan simbol:

| Simbol | Arti |
|---|---|
| Panah terbuka (→) | Asosiasi |
| Belah ketupat kosong (◇) | Agregasi |
| Belah ketupat hitam (◆) | Komposisi |
| Panah segitiga kosong (▷) | Pewarisan ke `Layanan` |
| Garis putus-putus | Penggunaan objek notifikasi (dependency injection) |

---

## 5. Penjelasan Relasi UML

### 5.1 Asosiasi

Asosiasi digunakan pada hubungan **Pesanan → Pelanggan**.

> **Pesanan dibuat oleh Pelanggan.**

Implementasi pada program:

```python
class Pesanan:
    def __init__(self, pelanggan, notifier):
        self.pelanggan = pelanggan   # ASOSIASI: Pesanan -> Pelanggan
```

`Pesanan` menyimpan referensi ke objek `Pelanggan` yang dibuat di luar. Keduanya objek yang berdiri sendiri: pelanggan tetap ada walaupun pesanan dihapus, sehingga hubungannya hanya asosiasi biasa. Asosiasi yang sama juga terdapat pada `ItemPesanan` ke `Sepatu` dan `Layanan`.

### 5.2 Agregasi

Agregasi digunakan pada hubungan **Pelanggan ◇— Sepatu**.

> **Pelanggan memiliki atau menampung Sepatu.**

Implementasi pada program:

```python
class Pelanggan:
    def __init__(self, nama, no_hp):
        self.daftar_sepatu = []

    def tambah_sepatu(self, sepatu):
        # AGREGASI: Sepatu dibuat di luar, hanya dikumpulkan oleh Pelanggan
        self.daftar_sepatu.append(sepatu)
```

Objek `Sepatu` dibuat di luar class `Pelanggan`, lalu dimasukkan lewat `tambah_sepatu()`. Dipilih **agregasi** karena `Sepatu` tetap bisa ada tanpa `Pelanggan` tersebut (misalnya sepatu yang sama dipakai di pesanan lain), sehingga hubungan "memiliki" ini longgar.

### 5.3 Komposisi

Komposisi digunakan pada hubungan **Pesanan ◆— ItemPesanan**.

> **Pesanan terdiri dari ItemPesanan.**

Implementasi pada program:

```python
def tambah_item(self, sepatu, layanan):
    # KOMPOSISI: ItemPesanan dibuat & dimiliki Pesanan (hidup-mati bersama)
    self._items.append(ItemPesanan(sepatu, layanan))
```

Objek `ItemPesanan` dibuat **langsung di dalam** `Pesanan`, bukan diberikan dari luar. Dipilih **komposisi** karena item tidak punya arti tanpa pesanannya: jika `Pesanan` dihapus, seluruh `ItemPesanan` ikut hilang.

### 5.4 Perbedaan Agregasi dan Komposisi

| Aspek | Agregasi (`Pelanggan` ◇— `Sepatu`) | Komposisi (`Pesanan` ◆— `ItemPesanan`) |
|---|---|---|
| Pembuatan objek bagian | Di luar class, lalu dimasukkan | Di dalam class pemilik |
| Ketergantungan hidup | Bagian tetap ada walau pemilik hilang | Bagian ikut hilang bersama pemilik |

### 5.5 Pewarisan

`CuciBiasa`, `DeepClean`, dan `Repaint` mewarisi `Layanan` (hubungan "is-a"). Relasi ini ditampilkan di diagram sebagai pelengkap dan mendukung abstraksi serta polimorfisme.

---

## 6. Penerapan Abstraksi

### 6.1 Abstract Class

Abstract class yang digunakan adalah `Layanan`, turunan dari `ABC`.

```python
class Layanan(ABC):
    @abstractmethod
    def hitung_biaya(self, sepatu): ...

    @abstractmethod
    def langkah_kerja(self): ...
```

Dua abstract method pada `Layanan`:

| Abstract method | Fungsi |
|---|---|
| `hitung_biaya(sepatu)` | Setiap jenis layanan menghitung biayanya sendiri |
| `langkah_kerja()` | Setiap jenis layanan punya daftar langkah kerja sendiri |

### 6.2 Implementasi pada Subclass

Subclass `CuciBiasa`, `DeepClean`, dan `Repaint` mengimplementasikan **kedua** abstract method di atas dengan perilaku masing-masing.

### 6.3 Method Konkret

`Layanan` memiliki method biasa yang dipakai bersama oleh semua subclass:

```python
def jalankan(self, sepatu):
    print(f"[{self.nama}] {sepatu}")
    for no, langkah in enumerate(self.langkah_kerja(), start=1):
        print(f"   {no}. {langkah}")
    print(f"   Biaya: {rupiah(self.hitung_biaya(sepatu))}")
```

Method `jalankan()` menyusun alur umum (tampilkan sepatu, langkah, biaya), sedangkan detailnya diserahkan ke abstract method milik masing-masing subclass.

### 6.4 Bukti Abstract Class Tidak Dapat Diinstansiasi

```python
try:
    Layanan("Layanan Abstrak", 0)
except TypeError as e:
    print("TypeError:", e)
```

Output:

```text
TypeError: Can't instantiate abstract class Layanan without an implementation for abstract methods 'hitung_biaya', 'langkah_kerja'
```

---

## 7. Penerapan Polimorfisme

### 7.1 Polimorfisme via Pewarisan

Method `hitung_biaya()` dan `langkah_kerja()` di-override oleh tiga subclass dengan perilaku berbeda:

| Subclass | Perhitungan `hitung_biaya()` |
|---|---|
| `CuciBiasa` | `harga_dasar` (Rp30.000) |
| `DeepClean` | `harga_dasar` + Rp10.000 × `tingkat_kotor` |
| `Repaint` | `harga_dasar` + Rp25.000 × `bagian_rusak` |

Pemanggilan dilakukan lewat **satu loop** yang berisi objek dari subclass berbeda:

```python
daftar_layanan = [CuciBiasa(), DeepClean(), Repaint()]
for layanan in daftar_layanan:
    layanan.jalankan(sepatu_b)
```

Pola yang sama dipakai di `Pesanan.proses()`, yang memanggil `item.layanan.jalankan(item.sepatu)` tanpa perlu tahu jenis layanannya.

### 7.2 Duck Typing

`NotifikasiWhatsApp` dan `NotifikasiEmail` **tidak berhubungan lewat pewarisan**, tetapi sama-sama memiliki method `kirim(pesan)`. Keduanya dipanggil lewat satu fungsi yang sama:

```python
def kirim_notifikasi(pengirim, pesan):
    pengirim.kirim(pesan)   # tidak peduli tipe, asal punya kirim()
```

### 7.3 Operator Overloading

| Magic method | Class | Kegunaan |
|---|---|---|
| `__lt__` | `Layanan` | Membandingkan layanan berdasarkan `harga_dasar`, sehingga bisa dipakai `sorted()` |
| `__str__` | `Layanan`, `Sepatu`, `Pelanggan`, `Pesanan` | Representasi teks objek saat `print()` |
| `__len__` | `Pesanan` | `len(pesanan)` mengembalikan jumlah item |

### 7.4 Tanpa Anti-Pattern

Program **tidak** membedakan perilaku objek dengan rantai `if/elif` yang mengecek `type()` atau string jenis. Setiap objek menentukan perilakunya sendiri lewat method.

---

## 8. Penerapan Prinsip SOLID (Nilai Plus)

| Prinsip | Bagian kode | Penjelasan |
|---|---|---|
| **OCP** (Open/Closed) | `Layanan` dan subclass-nya | Layanan baru (misalnya `Reglue`) cukup dibuat sebagai subclass baru dari `Layanan`. Class `Pesanan`, `ItemPesanan`, dan loop pemrosesan **tidak perlu diubah**. |
| **DIP** (Dependency Inversion) | `Pesanan.__init__(pelanggan, notifier)` | `Pesanan` menerima objek `notifier` lewat constructor (dependency injection), sehingga tidak bergantung langsung pada WhatsApp atau Email. Cukup objek yang memiliki method `kirim()`. |

Penerapan dibuat seperlunya dan tidak mengurangi syarat wajib poin 1 sampai 3.

---

## 9. Fitur Program

Program memiliki beberapa fitur utama:

1. Menampilkan bukti bahwa abstract class `Layanan` tidak dapat diinstansiasi.
2. Menjalankan tiga jenis layanan melalui satu loop (polimorfisme).
3. Menghitung biaya berbeda sesuai jenis layanan dan kondisi sepatu.
4. Mengurutkan layanan berdasarkan harga dasar memakai operator overloading.
5. Mengirim notifikasi lewat dua kelas tak berhubungan dengan satu fungsi (duck typing).
6. Mendata sepatu milik pelanggan (agregasi).
7. Membuat pesanan yang berisi beberapa item (komposisi).
8. Menghitung total pesanan.
9. Mengubah status pesanan: `Diterima` → `Diproses` → `Selesai`.
10. Mengirim notifikasi otomatis saat pesanan selesai.

---

## 10. Panduan Pengujian Program

### 10.1 Persiapan

Pastikan Python sudah terpasang pada komputer. Simpan program dengan nama file:

```text
main.py
```

### 10.2 Menjalankan Program

Buka terminal atau PowerShell pada folder tempat file disimpan, lalu jalankan:

```bash
python main.py
```

Jika menggunakan perintah Python lain sesuai instalasi komputer, dapat menggunakan:

```bash
py main.py
```

---

## 11. Pengujian Abstraksi

Bagian yang diuji:

```python
Layanan("Layanan Abstrak", 0)
```

Hasil yang diharapkan:

```text
TypeError: Can't instantiate abstract class Layanan without an implementation for abstract methods 'hitung_biaya', 'langkah_kerja'
```

Hal tersebut menunjukkan bahwa `Layanan` adalah abstract class dan hanya dapat dipakai lewat subclass.

---

## 12. Pengujian Polimorfisme via Pewarisan

Data pengujian: sepatu `Adidas Superstar` dengan `tingkat_kotor = 3` dan `bagian_rusak = 2`.

Hasil yang diharapkan:

```text
[Cuci Biasa] Adidas Superstar
   1. Lepas tali & insole
   2. Sikat bagian luar
   3. Bilas & keringkan
   Biaya: Rp30.000
[Deep Clean] Adidas Superstar
   1. Lepas tali & insole
   2. Rendam cairan khusus
   3. Sikat detail midsole & upper
   4. Disinfeksi
   5. Keringkan
   Biaya: Rp80.000
[Repaint] Adidas Superstar
   1. Bersihkan permukaan
   2. Hapus cat lama
   3. Cat ulang bagian rusak
   4. Finishing & coating
   Biaya: Rp130.000
```

Perbedaan langkah dan biaya untuk sepatu yang sama menunjukkan bahwa method yang namanya sama menghasilkan perilaku berbeda sesuai subclass.

---

## 13. Pengujian Operator Overloading

Bagian yang diuji:

```python
for layanan in sorted(daftar_layanan, reverse=True):
    print(layanan)
```

Hasil yang diharapkan:

```text
Repaint (mulai Rp80.000)
Deep Clean (mulai Rp50.000)
Cuci Biasa (mulai Rp30.000)
```

`sorted()` dapat berjalan karena `__lt__` diterapkan pada `Layanan`, dan `print()` menampilkan teks dari `__str__`.

---

## 14. Pengujian Duck Typing

Bagian yang diuji:

```python
for pengirim in [NotifikasiWhatsApp("0812-3456-7890"), NotifikasiEmail("adit@mail.com")]:
    kirim_notifikasi(pengirim, "Terima kasih telah menggunakan layanan kami.")
```

Hasil yang diharapkan:

```text
[WhatsApp ke 0812-3456-7890] Terima kasih telah menggunakan layanan kami.
[Email ke adit@mail.com] Terima kasih telah menggunakan layanan kami.
```

---

## 15. Pengujian Asosiasi, Agregasi, dan Komposisi

Bagian yang diuji:

```python
adit = Pelanggan("Adit", "0812-3456-7890")
adit.tambah_sepatu(sepatu_a)                 # agregasi
adit.tambah_sepatu(sepatu_b)
pesanan = Pesanan(adit, NotifikasiWhatsApp(adit.no_hp))   # asosiasi
pesanan.tambah_item(sepatu_a, DeepClean())   # komposisi
pesanan.tambah_item(sepatu_b, Repaint())
print(pesanan)
pesanan.proses()
pesanan.selesai()
print(pesanan)
```

Hasil yang diharapkan:

```text
Pesanan Adit - 2 item - Diterima
[Deep Clean] Nike Air Force 1
   1. Lepas tali & insole
   2. Rendam cairan khusus
   3. Sikat detail midsole & upper
   4. Disinfeksi
   5. Keringkan
   Biaya: Rp70.000
[Repaint] Adidas Superstar
   1. Bersihkan permukaan
   2. Hapus cat lama
   3. Cat ulang bagian rusak
   4. Finishing & coating
   Biaya: Rp130.000
[WhatsApp ke 0812-3456-7890] Halo Adit, 2 sepatu Anda sudah selesai. Total Rp200.000.
Pesanan Adit - 2 item - Selesai
```

Penjelasan hasil:

- Total Rp200.000 berasal dari Deep Clean Rp70.000 (Rp50.000 + 2 × Rp10.000) ditambah Repaint Rp130.000 (Rp80.000 + 2 × Rp25.000).
- Status pesanan berubah dari `Diterima` menjadi `Selesai`.
- `2 item` berasal dari `__len__` pada `Pesanan`.


## 16 Gambar class diagram 

![alt text](<class_diagram.drawio (1).png>)

## 17 Gambar screenshoot output program

![alt text](<Screenshot 2026-10-27 094824.png>)
