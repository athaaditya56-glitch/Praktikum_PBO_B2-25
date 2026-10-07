
# SUPERCLASS

class LayananPerawatan:

    # Atribut kelas
    nama_usaha = "ShoeCare"
    total_layanan = 0

    def __init__(self, nama_layanan, harga, estimasi_hari):

        # Atribut protected
        self._nama_layanan = nama_layanan
        self._harga = harga

        # Atribut public
        self.estimasi_hari = estimasi_hari

        # Atribut private
        self.__kode_layanan = "SC-" + str(
            LayananPerawatan.total_layanan + 1
        )

        LayananPerawatan.total_layanan += 1

    # Getter harga
    @property
    def harga(self):
        return self._harga

    # Setter harga
    @harga.setter
    def harga(self, harga_baru):

        if not isinstance(harga_baru, (int, float)):
            raise ValueError("Harga harus berupa angka.")

        if harga_baru < 0:
            raise ValueError("Harga tidak boleh negatif.")

        self._harga = harga_baru

    # Method superclass
    def tampilkan_info(self):

        print("Nama Layanan :", self._nama_layanan)
        print(f"Harga        : Rp{self._harga:,.0f}")
        print("Estimasi     :", self.estimasi_hari, "hari")

    # Method override
    def hitung_harga(self, jumlah):

        return self._harga * jumlah

    # Static method
    @staticmethod
    def validasi_harga(harga):

        return isinstance(harga, (int, float)) and harga >= 0

# SUBCLASS 1
class DeepCleaning(LayananPerawatan):

    def __init__(
        self,
        nama_layanan,
        harga,
        estimasi_hari,
        jenis_cairan
    ):

        super().__init__(
            nama_layanan,
            harga,
            estimasi_hari
        )

        # Atribut unik subclass
        self.jenis_cairan = jenis_cairan

    def tampilkan_info(self):

        print("Jenis Layanan :", "Deep Cleaning")
        print("Nama Layanan  :", self._nama_layanan)
        print(f"Harga         : Rp{self._harga:,.0f}")
        print("Estimasi      :", self.estimasi_hari, "hari")
        print("Jenis Cairan  :", self.jenis_cairan)

# SUBCLASS 2
class Repaint(LayananPerawatan):

    def __init__(
        self,
        nama_layanan,
        harga,
        estimasi_hari,
        warna_baru
    ):

        super().__init__(
            nama_layanan,
            harga,
            estimasi_hari
        )

        # Atribut unik subclass
        self.warna_baru = warna_baru

    # METHOD OVERRIDING
    def hitung_harga(self, jumlah):

        harga_dasar = super().hitung_harga(jumlah)

        biaya_cat = 20000

        return harga_dasar + biaya_cat

    def tampilkan_info(self):

        print("Jenis Layanan :", "Repaint")
        print("Nama Layanan  :", self._nama_layanan)
        print(f"Harga Dasar   : Rp{self._harga:,.0f}")
        print("Estimasi      :", self.estimasi_hari, "hari")
        print("Warna Baru    :", self.warna_baru)

# CLASS PELANGGAN
class Pelanggan:

    # Atribut kelas
    nama_sistem = "Sistem ShoeCare"
    total_pelanggan = 0

    def __init__(self, nama, nomor_hp, alamat):

        # Atribut public
        self.nama = nama
        self.alamat = alamat

        # Atribut private
        self.__nomor_hp = nomor_hp

        # AGREGASI
        self.daftar_pesanan = []

        Pelanggan.total_pelanggan += 1

    # Getter
    @property
    def nomor_hp(self):
        return self.__nomor_hp

    # Setter
    @nomor_hp.setter
    def nomor_hp(self, nomor_baru):

        if not Pelanggan.validasi_nomor_hp(nomor_baru):
            raise ValueError(
                "Nomor HP harus 10-13 digit."
            )

        self.__nomor_hp = nomor_baru

    # ASOSIASI

    def pilih_layanan(self, layanan):

        print(
            self.nama,
            "memilih layanan",
            layanan._nama_layanan
        )

    # AGREGASI
    def tambah_pesanan(self, pesanan):

        self.daftar_pesanan.append(pesanan)

    def tampilkan_data(self):

        print("Nama     :", self.nama)
        print("Nomor HP :", self.nomor_hp)
        print("Alamat   :", self.alamat)

    # Static method
    @staticmethod
    def validasi_nomor_hp(nomor):

        return (
            isinstance(nomor, str)
            and nomor.isdigit()
            and 10 <= len(nomor) <= 13
        )

# CLASS PEMBAYARAN
class Pembayaran:

    def __init__(self, metode, nominal):

        self.metode = metode
        self.nominal = nominal
        self.status = "Belum Dibayar"

    def proses_pembayaran(self):

        self.status = "Lunas"

        print(
            f"Pembayaran Rp{self.nominal:,.0f} "
            f"melalui {self.metode} berhasil."
        )

    def tampilkan_pembayaran(self):

        print("Metode Pembayaran :", self.metode)
        print(f"Nominal           : Rp{self.nominal:,.0f}")
        print("Status             :", self.status)

# CLASS PESANAN
class Pesanan:

    # Atribut kelas
    total_pesanan = 0
    status_awal = "Menunggu"

    def __init__(
        self,
        id_pesanan,
        pelanggan,
        layanan,
        jumlah,
        metode_pembayaran
    ):

        self.id_pesanan = id_pesanan
        self.pelanggan = pelanggan
        self.layanan = layanan
        self.jumlah = jumlah
        self.status = Pesanan.status_awal

        # KOMPOSISI
        total = layanan.hitung_harga(jumlah)

        self.pembayaran = Pembayaran(
            metode_pembayaran,
            total
        )

        Pesanan.total_pesanan += 1

    # Method hitung total
    def hitung_total(self):

        return self.layanan.hitung_harga(
            self.jumlah
        )

    # Method ubah status
    def ubah_status(self, status_baru):

        status_valid = [
            "Menunggu",
            "Diproses",
            "Selesai",
            "Diambil"
        ]

        if status_baru not in status_valid:

            print("Status tidak valid.")

            return

        self.status = status_baru

    # Tampilkan pesanan
    def tampilkan_pesanan(self):

        print("\nID Pesanan :", self.id_pesanan)
        print("Pelanggan  :", self.pelanggan.nama)
        print("Layanan    :", self.layanan._nama_layanan)
        print("Jumlah     :", self.jumlah)
        print("Status     :", self.status)

        print(
            f"Total      : Rp{self.hitung_total():,.0f}"
        )

        print("\nData Pembayaran")
        self.pembayaran.tampilkan_pembayaran()


# MAIN PROGRAM
if __name__ == "__main__":

    print("=" * 60)
    print("     SISTEM PENGELOLAAN PELAYANAN PERAWATAN SEPATU")
    print("=" * 60)

    # 1. Membuat objek subclass
    deep_cleaning = DeepCleaning(
        "Deep Cleaning",
        50000,
        2,
        "Foam Cleaner"
    )

    repaint = Repaint(
        "Repaint",
        75000,
        4,
        "Hitam"
    )

    # 2. Membuat objek Pelanggan
    pelanggan1 = Pelanggan(
        "Aditya",
        "081234567890",
        "Samarinda"
    )

    pelanggan2 = Pelanggan(
        "Budi",
        "082345678901",
        "Tenggarong"
    )

    # 3. INHERITANCE
    print("\n[1] INHERITANCE")
    print("-" * 60)

    print("\nInformasi Deep Cleaning")
    deep_cleaning.tampilkan_info()

    print("\nInformasi Repaint")
    repaint.tampilkan_info()

    # 4. ASOSIASI
    print("\n[2] ASOSIASI")
    print("-" * 60)

    pelanggan1.pilih_layanan(deep_cleaning)
    pelanggan2.pilih_layanan(repaint)

    # 5. Membuat pesanan

    pesanan1 = Pesanan(
        "P001",
        pelanggan1,
        deep_cleaning,
        2,
        "QRIS"
    )

    pesanan2 = Pesanan(
        "P002",
        pelanggan2,
        repaint,
        1,
        "Transfer"
    )

    # 6. AGREGASI
    print("\n[3] AGREGASI")
    print("-" * 60)

    pelanggan1.tambah_pesanan(pesanan1)
    pelanggan2.tambah_pesanan(pesanan2)

    print(
        "Jumlah pesanan",
        pelanggan1.nama,
        ":",
        len(pelanggan1.daftar_pesanan)
    )

    print(
        "Jumlah pesanan",
        pelanggan2.nama,
        ":",
        len(pelanggan2.daftar_pesanan)
    )

    # 7. KOMPOSISI
    print("\n[4] KOMPOSISI")
    print("-" * 60)

    pesanan1.tampilkan_pesanan()

    pesanan2.tampilkan_pesanan()

    # 8. METHOD OVERRIDING
    print("\n[5] METHOD OVERRIDING")
    print("-" * 60)

    print(
        "Harga Deep Cleaning 2 sepatu :",
        f"Rp{deep_cleaning.hitung_harga(2):,.0f}"
    )

    print(
        "Harga Repaint 1 sepatu       :",
        f"Rp{repaint.hitung_harga(1):,.0f}"
    )

    # 9. super()
    print("\n[6] SUPER()")
    print("-" * 60)

    print(
        "Repaint menggunakan konstruktor",
        "LayananPerawatan melalui super().__init__()"
    )

    print(
        "Repaint juga menggunakan",
        "super().hitung_harga() pada overriding."
    )

    # 10. PROTECTED
    print("\n[7] PROTECTED")
    print("-" * 60)

    print(
        "Nama layanan :",
        deep_cleaning._nama_layanan
    )

    print(
        "Harga layanan :",
        f"Rp{deep_cleaning._harga:,.0f}"
    )


    # 11. PRIVATE
    print("\n[8] PRIVATE")
    print("-" * 60)

    print(
        "Nomor HP pelanggan :",
        pelanggan1.nomor_hp
    )

    print(
        "Kode layanan menggunakan atribut private",
        "__kode_layanan"
    )

    # 12. Getter dan Setter
    print("\n[9] GETTER & SETTER")
    print("-" * 60)

    print(
        "Harga awal :",
        f"Rp{deep_cleaning.harga:,.0f}"
    )

    deep_cleaning.harga = 55000

    print(
        "Harga setelah setter :",
        f"Rp{deep_cleaning.harga:,.0f}"
    )

    # 13. Pembayaran
    print("\n[10] PEMBAYARAN")
    print("-" * 60)

    pesanan1.pembayaran.proses_pembayaran()

    pesanan1.ubah_status("Diproses")

    print(
        "Status Pesanan 1 :",
        pesanan1.status
    )

    # 14. CEK INHERITANCE
    print("\n[11] CEK INHERITANCE")
    print("-" * 60)

    print(
        "DeepCleaning adalah LayananPerawatan :",
        isinstance(
            deep_cleaning,
            LayananPerawatan
        )
    )

    print(
        "Repaint adalah LayananPerawatan       :",
        isinstance(
            repaint,
            LayananPerawatan
        )
    )

    print(
        "DeepCleaning subclass LayananPerawatan:",
        issubclass(
            DeepCleaning,
            LayananPerawatan
        )
    )

    print(
        "Repaint subclass LayananPerawatan     :",
        issubclass(
            Repaint,
            LayananPerawatan
        )
    )

    # 15. ATRIBUT KELAS    

    print("\n[12] ATRIBUT KELAS")
    print("-" * 60)

    print(
        "Nama Usaha       :",
        LayananPerawatan.nama_usaha
    )

    print(
        "Total Layanan    :",
        LayananPerawatan.total_layanan
    )

    print(
        "Total Pelanggan  :",
        Pelanggan.total_pelanggan
    )

    print(
        "Total Pesanan    :",
        Pesanan.total_pesanan
    )


    print("\n" + "=" * 60)
    print("                 PROGRAM SELESAI")
    print("=" * 60)