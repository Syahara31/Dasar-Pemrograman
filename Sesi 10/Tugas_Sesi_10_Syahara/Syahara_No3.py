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
            harga, stok = inventory[nama_barang ]
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




    