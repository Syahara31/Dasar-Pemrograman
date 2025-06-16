from ecommerce.pricing import hitung_diskon, hitung_pajak, hitung_total
from ecommerce.order import generate_order_id

def main():
    nama_pelanggan = input("Masukan nama pelanggan: ")
    nama_produk = input("Masukan produk: ")
    harga_asli = float(input ("Masukan Harga: "))
    persentasi_diskon = float(input("Masukan persentase disakon: "))
    persentase_pajak =float(input("Masukan persentase pajak: "))

    diskon = harga_asli * (persentase_diskon/100)
    total = hitung_total(harga_asli, persentase_diskon, persentase_pajak)
    order_id = generate_order_id()

    print("-"*40)
    print("      RINCIANPEMBELIAN      ")
    print("-"*40)
    print(f"{'ID Pesanan':20}: {order_id}")
    print(f"{'Nama Pelanggan':20}: {nama_pelanggan}")
    print(f"{'Nama Produk':20}: {nama_produk}")
    print(f"{'Harga asli':20}; {nama_produk}")
    print(f"{'Diskon': 20}: Rp {diskon:,.2f}")
    print(f"{'Pajak': 20}: Rp {hitung_pajak(harga_asli - diskon, persentase_pajak):,.2f}")
    print(f"-"*40)
    print(f"{'Total belanja':20}: Rp {total:,.2f}")
    print("-"*40)

if __name__ == "__main__":
        main()


