from person import Customer, Admin

class CustomerView:
    """
    Class untuk interface Customer.
    Setiap menu jadi sebuah metode tersendiri
    """

    def __init__(self):
        self.__customer = Customer()

    def start(self):
        print(f"Selamat Datang di Aplikasi Paket Wisata\n- Nikmati Pariwisata yang Komplit dan Enjoy"
              f"1. Login\n"
              f"2. Register\n"
              f"0. Keluar\n\n")
        choice = input("Masukkan pilihanmu [0/1/2]: ")

        if choice == '1':
            self.login_dialog()
        elif choice == '2':
            self.register_dialog()
        else:

    def login_dialog(self):
        email = input("Masukkan E-mail")
        password = input("Masukkan Password")
        self.__customer.login(email, password)
        pass

    def register_dialog(self):
        nama = input("Masukkan Nama Lengkap")
        noKtp = input("Massukan Nomor KTP")
        noHp = input("Masukkan Nomor HP")
        email = input("Masukkan E-mail")
        password = input("Masukkan Password")
        self.__customer.register(nama, noKtp, noHP, email, password)
        pass
    
    def beranda_dialog(self):
        print(f"Silahkan Pilih Menu Yang Ingin Dilakukan\n"
              f"1. Pesan Paket Wisata Sekarang\n"
              f"2. Riwayat Pesanan\n"
              f"3. Ajukan Pembatalan Transaksi\n"
              f"0. Keluar\n\n")
        choiceBeranda = input("Masukkan Pilihanmu [0/1/2/3]: ")

        if choiceBeranda == '1':
            self.pesan_dialog()
        elif choiceBeranda == '2':
            self.riwayat_dialog()
        elif choiceBeranda == '3':
            self.pembatalan_dialog()
        else:

    def pesan_dialog(self):
        print("Lebih Mudah! Cukup Pilih Paket Wisata yang Anda Inginkan\n")
        #Pilih Paket
        choicePesan = input("Pilih Paketmu :")
        self.tambahOrangPesan()
        kodePembayaran = #kodePembayaran 
        print("Silahkan Melakukan Pembayaran\n"
              f"Dengan Kode Pembayaran", kodePembayaran)
        print("Menunggu Konfirmasi Pembayaran")
        #Konfirmasi Admin
        kodeBooking = #kodeBooking
        print("Pesanan Anda Telah berhasil\nDengan Kode Booking", kodeBooking)
        pass        

    def tambahOrangPesan(self)
        nama = input("Masukkan Nama Lengkap")
        noIdentitas = input("Massukan Nomor KTP")
        self.__customer.register(nama, noIdentitas)

    def riwayat_dialog(self):
        #show riwayat transaksi
        pass

    def pembatalan_dialog(self):
        kodeBooking = input ("Silahkan Masukkan Kode Booking")
        #Kode Booking Benar, Admin Konfirmasi
        print("Menunggu Konfirmasi Pembatalan")
        #Konfirmasi Admin
        print("Transaksi Anda Berhasil Dibatalkan")

class AdminView:
    """
    Class untuk interface Admin.
    Setiap menu jadi sebuah metode tersendiri
    """

    def __init__(self):
        self.__admin = Admin()

    def login_dialog(self):
        email = input("Masukkan E-mail")
        password = input("Masukkan Password")
        self.__admin.login(email, password)
        pass

    def berandaAdmin_dialog(sefl):
        print(f"Selamat Datang, Admin\n"
              f"1. Konfirmasi Pembayaran\n"
              f"2. Konfirmasi Pembatalan GTransaksi\n")
              f"0. Keluar"
        choiceBerandaAdmin = int(input("Masukkan Pilihan [0/1/2]:"))

        if choiceBerandaAdmin == 1:
            self.konfirmasiPembayaran_dialog()
        elif choiceBerandaAdmin == 2:
            self.konfirmasiPembatalan_dialog()

    def konfirmasiPembayaran_dialog(self):
        #Lihat Transaksi & Pilih Transaksi
        choiceKonfirmasiPembayaran = input("Konfirmasi Pembayaran\n1. Iya\n2. Tidak [1/2] :")        

    def konfirmasiPembatalan_dialog(self):
        #Lihat Transaksi & Pilih Transaksi
        choiceKonfirmasiPembatalan = input("Konfirmasi Pembatalan\n1. Iya\n2. Tidak [1/2] :")  

        
