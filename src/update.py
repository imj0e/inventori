from lihatProduk import lihat_produk

def update_produk(database):
    if not database:
        print("Database produk kosong.")
    else:
        lihat_produk(database)  # Menampilkan daftar produk

        try:
            index_produk = int(input("Masukkan nomor produk untuk update: "))
            if 1 <= index_produk <= len(database):
                produk_terpilih = database[index_produk - 1]

                print("Pilih opsi update:")
                print("1. Update Nama")
                print("2. Update Harga")
                print("3. Update Stok")
                option_update = int(input("Masukkan pilihan anda: "))

                if option_update == 1:
                    new_nama = input("Masukkan nama baru: ")
                    produk_terpilih['nama'] = new_nama
                elif option_update == 2:
                    new_harga = float(input("Masukkan harga baru: "))
                    produk_terpilih['harga'] = new_harga
                    print(f"Nama produk{nama}, harga baru adalah {new_harga}, sisa stok produk{stok}")
                elif option_update == 3:
                    new_stok = int(input("Masukkan stok baru: "))
                    produk_terpilih['stok'] = new_stok
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Nomor produk tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor.")
