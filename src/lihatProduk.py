def lihat_produk(database):
    if not database:
        print("Database produk kosong.")
    else:
        print("Daftar Produk:")
        for idx, produk in enumerate(database, start=1):
            print(f"{idx}. Nama: {produk['nama']}, Harga: {produk['harga']}, Stok: {produk['stok']}")
