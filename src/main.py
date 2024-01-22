#halaman utama dari program
from tambahProduk import tambah_produk
from lihatProduk import lihat_produk
from cekHarga import cek_harga
from cekStok import cek_stok
from update import update_produk
database_produk = []

while True:

    print('#'*5, "Selamat Datang di Program kasir Sederhana", '#'*5)
    print('#'*5, "Silahkan pilih menu untuk melanjutkan", '#'*5 )
    print("1. Tambah Produk")
    print("2. Cek Harga Produk")
    print("3. Cek Stok Produk")
    print("4. Update Produk")
    print("5. Lihat Produk")
    print("ketik 'exit' untuk keluar")


#meminta input dari user
    try:
        options = int(input("masukan pilihan anda : "))
        if options < 1 or options > 5 :
            print("Pilihan tidak valid, silahkan ketik kembali")
        else :
            if options == 1 :
                print("anda memilih tambah produk")
                tambah_produk(database_produk)
            elif options == 2 :
                print("anda memilih cek harga")
                cek_harga(database_produk)
            elif options == 3 :
                print("anda memilih cek stok")
                cek_stok(database_produk)
            elif options == 4 :
                print("anda memilih update produk")
                update_produk(database_produk)
            elif options == 5 :
                print("anda memilih lihat produk")
                lihat_produk(database_produk)



    except ValueError:
        print('#'*10, "pilihan tidak valid, silahkan masukan angka", '#'*10)
