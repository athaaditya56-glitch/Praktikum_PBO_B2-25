class LayananPerawatan:
    # Atribut kelas
    nama_usaha = "ShoeCare"
    total_layanan = 0
    diskon_member = 0.10

    def __init__(self, nama_layanan, harga, estimasi_hari):
        # Atribut instance public
        self.nama_layanan = nama_layanan
        self.estimasi_hari = estimasi_hari

        # Atribut instance private
        self.__harga = harga

        LayananPerawatan.total_layanan += 1

    # Getter
    @property
    def harga(self):
        return self.__harga

    # Setter
    @harga.setter
    def harga(self, harga_baru):
        if not isinstance(harga_baru, (int, float)):
            raise ValueError("Harga harus berupa angka.")

        if harga_baru < 0:
            raise ValueError("Harga tidak boleh negatif.")

        self.__harga = harga_baru

    # Instance method
    def tampilkan_info(self):
        print(f"Nama Layanan : {self.nama_layanan}")
        print(f"Harga        : Rp{self.harga:,.0f}")
        print(f"Estimasi     : {self.estimasi_hari} hari")

    # Class method
    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["nama_layanan"],
            data["harga"],
            data["estimasi_hari"]
        )

    # Static method
    @staticmethod
    def validasi_harga(harga):
        return isinstance(harga, (int, float)) and harga >= 0


class Pelanggan:
    # Atribut kelas
    nama_sistem = "Sistem ShoeCare"
    total_pelanggan = 0
    status_member_default = "Non-Member"

    def __init__(self, nama, nomor_hp, alamat):
        # Atribut instance public
        self.nama = nama
        self.alamat = alamat

        # Atribut instance private
        self.__nomor_hp = nomor_hp

        Pelanggan.total_pelanggan += 1

    # Getter
    @property
    def nomor_hp(self):
        return self.__nomor_hp

    # Setter + validasi
    @nomor_hp.setter
    def nomor_hp(self, nomor_baru):
        if not Pelanggan.validasi_nomor_hp(nomor_baru):
            raise ValueError(
                "Nomor HP harus berupa angka dengan panjang 10-13 digit."
            )

        self.__nomor_hp = nomor_baru

    # Instance method
    def tampilkan_data(self):
        print(f"Nama     : {self.nama}")
        print(f"Nomor HP : {self.nomor_hp}")
        print(f"Alamat   : {self.alamat}")

    # Class method
    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["nama"],
            data["nomor_hp"],
            data["alamat"]
        )

    # Static method
    @staticmethod
    def validasi_nomor_hp(nomor):
        return (
            isinstance(nomor, str)
            and nomor.isdigit()
            and 10 <= len(nomor) <= 13
        )


class Pesanan:
    # Atribut kelas
    total_pesanan = 0
    status_awal = "Menunggu"
    biaya_tambahan = 0

    def __init__(self, id_pesanan, pelanggan, layanan, jumlah):
        # Atribut instance public
        self.id_pesanan = id_pesanan
        self.pelanggan = pelanggan
        self.layanan = layanan
        self.status = Pesanan.status_awal

        # Atribut instance private
        self.__jumlah = jumlah

        Pesanan.total_pesanan += 1

    # Getter
    @property
    def jumlah(self):
        return self.__jumlah

    # Setter
    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if not isinstance(jumlah_baru, int):
            raise ValueError("Jumlah harus berupa bilangan bulat.")

        if jumlah_baru <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")

        self.__jumlah = jumlah_baru

    # Instance method
    def hitung_total(self):
        return self.layanan.harga * self.jumlah

    # Instance method
    def ubah_status(self, status_baru):
        if not Pesanan.validasi_status(status_baru):
            raise ValueError("Status pesanan tidak valid.")

        self.status = status_baru

    # Instance method
    def tampilkan_pesanan(self):
        print(f"ID Pesanan : {self.id_pesanan}")
        print(f"Pelanggan  : {self.pelanggan.nama}")
        print(f"Layanan    : {self.layanan.nama_layanan}")
        print(f"Harga      : Rp{self.layanan.harga:,.0f}")
        print(f"Jumlah     : {self.jumlah}")
        print(f"Status     : {self.status}")
        print(f"Total      : Rp{self.hitung_total():,.0f}")

    # Class method
    @classmethod
    def buat_pesanan(cls, id_pesanan, pelanggan, layanan, jumlah):
        return cls(id_pesanan, pelanggan, layanan, jumlah)

    # Static method
    @staticmethod
    def validasi_status(status):
        status_valid = [
            "Menunggu",
            "Diproses",
            "Selesai",
            "Diambil"
        ]

        return status in status_valid


# MAIN CODE
if __name__ == "__main__":

    print("=" * 55)
    print("      SISTEM PENGELOLAAN LAYANAN PERAWATAN SEPATU")
    print("=" * 55)

    # 1. Membuat minimal 2 objek class LayananPerawatan

    layanan1 = LayananPerawatan(
        "Deep Cleaning",
        50000,
        2
    )

    data_layanan = {
        "nama_layanan": "Repaint",
        "harga": 75000,
        "estimasi_hari": 4
    }

    layanan2 = LayananPerawatan.dari_dict(data_layanan)

    # 2. Membuat minimal 2 objek class Pelanggan

    pelanggan1 = Pelanggan(
        "Aditya",
        "081234567890",
        "Samarinda"
    )

    data_pelanggan = {
        "nama": "Budi",
        "nomor_hp": "082345678901",
        "alamat": "Tenggarong"
    }

    pelanggan2 = Pelanggan.dari_dict(data_pelanggan)


    # 3. Membuat minimal 2 objek class Pesanan

    pesanan1 = Pesanan(
        "P001",
        pelanggan1,
        layanan1,
        1
    )

    pesanan2 = Pesanan.buat_pesanan(
        "P002",
        pelanggan2,
        layanan2,
        2
    )

    # 4. Demonstrasi Instance Method

    print("\n[1] INSTANCE METHOD")
    print("-" * 55)

    print("\nData Layanan 1")
    layanan1.tampilkan_info()

    print("\nData Layanan 2")
    layanan2.tampilkan_info()

    print("\nData Pelanggan 1")
    pelanggan1.tampilkan_data()

    print("\nData Pelanggan 2")
    pelanggan2.tampilkan_data()

    print("\nData Pesanan 1")
    pesanan1.tampilkan_pesanan()

    print("\nData Pesanan 2")
    pesanan2.tampilkan_pesanan()

    print("\nMengubah status Pesanan 1...")
    pesanan1.ubah_status("Diproses")
    print("Status baru:", pesanan1.status)


    # 5. Demonstrasi Class Method

    print("\n[2] CLASS METHOD")
    print("-" * 55)

    print("Layanan 2 dibuat dengan class method dari_dict().")
    print("Pelanggan 2 dibuat dengan class method dari_dict().")
    print("Pesanan 2 dibuat dengan class method buat_pesanan().")

    # 6. Demonstrasi Static Method

    print("\n[3] STATIC METHOD")
    print("-" * 55)

    print(
        "Validasi harga Rp50.000 :",
        LayananPerawatan.validasi_harga(50000)
    )

    print(
        "Validasi harga -5.000 :",
        LayananPerawatan.validasi_harga(-5000)
    )

    print(
        "Validasi nomor HP benar :",
        Pelanggan.validasi_nomor_hp("081234567890")
    )

    print(
        "Validasi nomor HP salah :",
        Pelanggan.validasi_nomor_hp("123")
    )

    print(
        "Validasi status Diproses :",
        Pesanan.validasi_status("Diproses")
    )

    print(
        "Validasi status Random :",
        Pesanan.validasi_status("Random")
    )

    # 7. Demonstrasi Getter

    print("\n[4] GETTER")
    print("-" * 55)

    print("Harga layanan 1 :", layanan1.harga)
    print("Nomor HP pelanggan 1 :", pelanggan1.nomor_hp)
    print("Jumlah pesanan 1 :", pesanan1.jumlah)

    # 8. Demonstrasi Setter dengan data valid

    print("\n[5] SETTER - DATA VALID")
    print("-" * 55)

    try:
        layanan1.harga = 55000
        pelanggan1.nomor_hp = "081298765432"
        pesanan1.jumlah = 2

        print("Harga baru layanan 1 :", layanan1.harga)
        print("Nomor HP baru pelanggan 1 :", pelanggan1.nomor_hp)
        print("Jumlah baru pesanan 1 :", pesanan1.jumlah)

    except ValueError as e:
        print("Terjadi kesalahan:", e)

    # 9. Demonstrasi Setter dengan data tidak valid

    print("\n[6] SETTER - DATA TIDAK VALID")
    print("-" * 55)

    try:
        layanan1.harga = -5000
    except ValueError as e:
        print("Harga ditolak      :", e)

    try:
        pelanggan1.nomor_hp = "123"
    except ValueError as e:
        print("Nomor HP ditolak   :", e)

    try:
        pesanan1.jumlah = 0
    except ValueError as e:
        print("Jumlah ditolak     :", e)

    # 10. Demonstrasi atribut kelas

    print("\n[7] ATRIBUT KELAS")
    print("-" * 55)

    print(
        "Nama usaha              :",
        LayananPerawatan.nama_usaha
    )

    print(
        "Total layanan           :",
        LayananPerawatan.total_layanan
    )

    print(
        "Diskon member           :",
        LayananPerawatan.diskon_member * 100,
        "%"
    )

    print(
        "Nama sistem             :",
        Pelanggan.nama_sistem
    )

    print(
        "Total pelanggan         :",
        Pelanggan.total_pelanggan
    )

    print(
        "Status member default   :",
        Pelanggan.status_member_default
    )

    print(
        "Total pesanan           :",
        Pesanan.total_pesanan
    )

    print(
        "Status awal pesanan     :",
        Pesanan.status_awal
    )

    print(
        "Biaya tambahan          :",
        Pesanan.biaya_tambahan
    )

    # 11. Hasil akhir pesanan

    print("\n[8] HASIL AKHIR PESANAN")
    print("-" * 55)

    print("\nPesanan 1")
    pesanan1.tampilkan_pesanan()

    print("\nPesanan 2")
    pesanan2.tampilkan_pesanan()

    print("\n" + "=" * 55)
    print("                PROGRAM SELESAI")
    print("=" * 55)