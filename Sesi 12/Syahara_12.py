import pandas as pd

# 1. Membaca dan Menampilkan Data
file_path = "data/data_penjualan.xlsx"
df = pd.read_excel(file_path)
print("Tampilkan 5 baris pertama data penjualan: ")
print(df.head())

# 2. Menambahkan Kolom Total Harga
df["Total Harga"] = df["Jumlah"] * df["Harga Satuan"]
print("\nData dengan kolom total harga: ")
print(df.head())

# 3. Filter Data Kategori Elektonik
df_elektronik = df[df["Kategori"] == "Elektronik"]
df_elektronik.to_excel("electronik.xlsx", index=False)
print("\nData penjualan kategori elektronik: ")
print(df_elektronik)

# 4. Rekap Penjualan per Kategori
rekap = df.groupby("Kategori")["Total Harga"].sum().reset_index()
rekap.columns = ["Kategori", "Total Pendapatan"]
print("\n Rekap total pendapatan per kategori: ")
print(rekap)

# 5. Sortir Data Berdasarkan Total Harga
df_sorted = df.sort_values(by="Total Harga", ascending=False)
df_sorted.to_excel("penjualan_terurut.xlsx", index=False)
print("\nData diurutkan berdasarkan total harga (menurun): ")
print(df_sorted.head())