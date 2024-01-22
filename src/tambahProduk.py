def tambah_produk(database):
    # Meminta input dari pengguna
    nama_produk = input("Masukkan nama produk: ")
    harga_produk = float(input("Masukkan harga produk: "))
    stok_produk = int(input("Masukkan stok produk: "))

    # Membuat entri produk dalam dictionary
    produk_baru = {
        'nama': nama_produk,
        'harga': harga_produk,
        'stok': stok_produk
    }

    # Menambahkan produk baru ke dalam database
    database.append(produk_baru)
    print("Produk berhasil ditambahkan.")

if __name__ == "__main__":
    # Contoh penggunaan
    database_produk = []

    # Memanggil fungsi tambah_produk
    tambah_produk(database_produk)

    # Menampilkan database setelah penambahan produk
    print("Database Produk:")
    print(database_produk)
