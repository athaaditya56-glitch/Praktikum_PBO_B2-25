"""Sistem Pengelolaan Pelayanan Perawatan Sepatu."""
from abc import ABC, abstractmethod


def rupiah(nilai):
    return "Rp" + f"{nilai:,}".replace(",", ".")

# ABSTRAKSI: abstract class Layanan (2 @abstractmethod + 1 method konkret)
class Layanan(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.harga_dasar = harga_dasar

    @abstractmethod
    def hitung_biaya(self, sepatu):
        """Setiap jenis layanan menghitung biayanya sendiri."""

    @abstractmethod
    def langkah_kerja(self):
        """Setiap jenis layanan punya langkah kerja sendiri."""

    # Method konkret: dipakai bersama oleh semua subclass
    def jalankan(self, sepatu):
        print(f"[{self.nama}] {sepatu}")
        for no, langkah in enumerate(self.langkah_kerja(), start=1):
            print(f"   {no}. {langkah}")
        print(f"   Biaya: {rupiah(self.hitung_biaya(sepatu))}")

    # OPERATOR OVERLOADING
    def __str__(self):
        return f"{self.nama} (mulai {rupiah(self.harga_dasar)})"

    def __lt__(self, other):
        return self.harga_dasar < other.harga_dasar


# POLIMORFISME via pewarisan: method di-override dengan perilaku berbeda
class CuciBiasa(Layanan):
    def __init__(self):
        super().__init__("Cuci Biasa", 30000)

    def hitung_biaya(self, sepatu):
        return self.harga_dasar

    def langkah_kerja(self):
        return ["Lepas tali & insole", "Sikat bagian luar", "Bilas & keringkan"]


class DeepClean(Layanan):
    def __init__(self):
        super().__init__("Deep Clean", 50000)

    def hitung_biaya(self, sepatu):
        return self.harga_dasar + 10000 * sepatu.tingkat_kotor

    def langkah_kerja(self):
        return ["Lepas tali & insole", "Rendam cairan khusus",
                "Sikat detail midsole & upper", "Disinfeksi", "Keringkan"]


class Repaint(Layanan):
    def __init__(self):
        super().__init__("Repaint", 80000)

    def hitung_biaya(self, sepatu):
        return self.harga_dasar + 25000 * sepatu.bagian_rusak

    def langkah_kerja(self):
        return ["Bersihkan permukaan", "Hapus cat lama", "Cat ulang bagian rusak",
                "Finishing & coating"]

# Kelas domain
class Sepatu:
    def __init__(self, merek, jenis, tingkat_kotor=1, bagian_rusak=0):
        self.merek = merek
        self.jenis = jenis
        self.tingkat_kotor = tingkat_kotor    # 1 - 3
        self.bagian_rusak = bagian_rusak      

    def __str__(self):
        return f"{self.merek} {self.jenis}"


class Pelanggan:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.daftar_sepatu = []

    def tambah_sepatu(self, sepatu):
        # AGREGASI: Sepatu dibuat di luar, hanya dikumpulkan oleh Pelanggan
        self.daftar_sepatu.append(sepatu)

    def __str__(self):
        return f"{self.nama} ({self.no_hp})"


class ItemPesanan:
    def __init__(self, sepatu, layanan):
        self.sepatu = sepatu
        self.layanan = layanan

    def subtotal(self):
        return self.layanan.hitung_biaya(self.sepatu)


class Pesanan:
    def __init__(self, pelanggan, notifier):
        self.pelanggan = pelanggan   # ASOSIASI: Pesanan -> Pelanggan
        self.notifier = notifier     # DIP: dependensi disuntikkan dari luar
        self._items = []
        self.status = "Diterima"

    def tambah_item(self, sepatu, layanan):
        # KOMPOSISI: ItemPesanan dibuat & dimiliki Pesanan (hidup-mati bersama)
        self._items.append(ItemPesanan(sepatu, layanan))

    def total(self):
        return sum(item.subtotal() for item in self._items)

    def proses(self):
        self.status = "Diproses"
        for item in self._items:
            item.layanan.jalankan(item.sepatu)   # polimorfisme

    def selesai(self):
        self.status = "Selesai"
        self.notifier.kirim(
            f"Halo {self.pelanggan.nama}, {len(self)} sepatu Anda sudah selesai. "
            f"Total {rupiah(self.total())}."
        )

    # OPERATOR OVERLOADING
    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"Pesanan {self.pelanggan.nama} - {len(self)} item - {self.status}"


# DUCK TYPING: dua kelas tanpa pewarisan, sama-sama punya kirim()
class NotifikasiWhatsApp:
    def __init__(self, nomor):
        self.nomor = nomor

    def kirim(self, pesan):
        print(f"[WhatsApp ke {self.nomor}] {pesan}")


class NotifikasiEmail:
    def __init__(self, alamat):
        self.alamat = alamat

    def kirim(self, pesan):
        print(f"[Email ke {self.alamat}] {pesan}")


def kirim_notifikasi(pengirim, pesan):
    pengirim.kirim(pesan)   # tidak peduli tipe, asal punya kirim()


# main
def garis(judul):
    print(f"\n===== {judul} =====")


if __name__ == "__main__":
    garis("1. BUKTI ABSTRAKSI: Layanan tidak bisa diinstansiasi")
    try:
        Layanan("Layanan Abstrak", 0)
    except TypeError as e:
        print("TypeError:", e)

    garis("2. POLIMORFISME: satu loop, objek subclass berbeda")
    sepatu_a = Sepatu("Nike", "Air Force 1", tingkat_kotor=2)
    sepatu_b = Sepatu("Adidas", "Superstar", tingkat_kotor=3, bagian_rusak=2)
    daftar_layanan = [CuciBiasa(), DeepClean(), Repaint()]
    for layanan in daftar_layanan:
        layanan.jalankan(sepatu_b)

    garis("3. OPERATOR OVERLOADING: __lt__, __str__, __len__")
    for layanan in sorted(daftar_layanan, reverse=True):
        print(layanan)

    garis("4. DUCK TYPING: satu fungsi, dua kelas tak berhubungan")
    for pengirim in [NotifikasiWhatsApp("0812-3456-7890"), NotifikasiEmail("adit@mail.com")]:
        kirim_notifikasi(pengirim, "Terima kasih telah menggunakan layanan kami.")

    garis("5. ALUR PESANAN (Asosiasi, Agregasi, Komposisi)")
    adit = Pelanggan("Adit", "0812-3456-7890")
    adit.tambah_sepatu(sepatu_a)    # agregasi
    adit.tambah_sepatu(sepatu_b)
    pesanan = Pesanan(adit, NotifikasiWhatsApp(adit.no_hp))
    pesanan.tambah_item(sepatu_a, DeepClean())     # komposisi
    pesanan.tambah_item(sepatu_b, Repaint())
    print(pesanan)
    pesanan.proses()
    pesanan.selesai()
    print(pesanan)
