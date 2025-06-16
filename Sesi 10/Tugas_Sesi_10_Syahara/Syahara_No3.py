inventory = {}

def tambah_barang():
    nama_barang = input("Masukan Nama Barang: ")
    harga = float(input("Masukan Harga: "))
    stok = int(input("Masukan Stok: "))
    inventory[nama_barang] = ("harga, Stok: ")
    print(f"{nama_barang} barhasl ditambahkan.")

def tampilkan_semua_barang():
    if not inventory:
        print("Tidak ada barang dalam inventaris.")
        return
    print("\nDaftar Semua Barang: ")
    print("{;\:<20} {:<10} {:<10}".format("Nama Barang","Harga", "Stok"))
    for nama, (harga, stok) in inventory.items():
        print("{:<20} {:<10} {:<10}". format(nama, harga, stok))

    def cari_barang():
        nama_barang  = input("Masukan Nama Barang yang dicari: ")
        if nama_barang in inventory:
            harga, stok = inventory[nama_barang]
            print(f"Detail Barang: {nama_barang}, Harga: {harga}, Stok: {stok}")
        else:
            print("Barang tidak ditemukan.")

    def perbarui_stok():
        nama_barang = input("Masukan Nama Barang Untuk di perbarui: ")
        if nama_barang in inventory:
            stok_baru = int(input("Masukan Stok Baru: "))
            harga = inventory[nama_barang][0]
            inventory[nama_barang] = (harga, stok_baru)
            print(f"Stok untuk{nama_barang} berhasil diperbaharui.")
        else:
            print("Barang tidak ditemuan.")

    def hapus_barang():
        nama_barang = ("Masukan nama barang yang akan di hapus: ")
        if nama_barang in inventory:
            del inventory[nama_barang]
            print(f"{nama_barang} berhasul dihapus dari inventaris.")
        else:
            print("Barang tidak ditemukan.")

    def analisis_data():
        if not inventory:
            print("Tidak ada barang dalam inventaris.")
            return
        
        barang_tertinggi = max(inventory.items(), key=lambda x: x[1][0])
        barang_terendah = min(inventory.items(), key=lambda x: x[1][0])

        total_nilai = sum(harga * stok for harga, (harga,stok) in inventory.items())

        print(f"Barang dengan harga tertinggi: {barang_tertinggi[0]} - Harga: {barang_tertinggi[1][0]} Stok: {barang_tertinggi[1][1]}")
        print(f"Barang dengan harga terendah: {barang_terendah[0]} - Harga: {barang_terendah[1][0]} Stok: {barang_terendah[1][1]}")
        print(f"Total nilai inventaris: {total_nilai}")

    def menu_program():
        while True:
            print("\nMenu: ")
            print("1. Tambah Barang Baru")
            print("2. Tampilkan Semua Barang")
            print("3. Cari Barang")
            print("4. Hapus Barang")
            print("5. Hapua Barang")
            print("6. Analisis Data")
            print("7. Keluar")
            pilihan = input("Pilih menu (1-7): ")

            if pilihan == '1':
                tambah_barang()
            if pilihan == '2':
                tampilkan_semua_barang()
            if pilihan == '3':
                cari_barang()
            if pilihan == '4':
                perbarui_stok()
            if pilihan == '5':
                hapus_barang()
            if pilihan == '6':
                analisis_data()
            if pilihan == '7':
                print("Keluar daro program.")
                break
            else:
                print("Pilihan tidak valid. Silahkan coba lagi.")

    menu_program()


            