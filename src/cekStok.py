from lihatProduk import lihat_produk


def cek_stok(database):
    if not database:
        print("Database produk kosong.")
    else:
        lihat_produk(database)  # Menampilkan daftar produk

        try:
            index_produk = int(input("Masukkan nomor produk untuk cek harga: "))
            if 1 <= index_produk <= len(database):
                daftar_produk = database[index_produk - 1]
                print(f"Harga produk {daftar_produk['nama']}: {daftar_produk['stok']}")
            else:
                print("Nomor produk tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor.")
