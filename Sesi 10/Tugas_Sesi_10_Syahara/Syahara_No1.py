buah_1 = input ("Masukan nama buah pertama: ")
buah_2 = input ("Masukan nama buah kedua: ")
buah_3 = input ("Masukan nama buah ketiga: ")
buah_4 = input ("Masukan nama buah keempat: ")
buah_5 = input ("Masukan nama buah kelima: ")

mytuple = (buah_1, buah_2, buah_3, buah_4, buah_5)

print("Tuple buah: ", mytuple)

cari = input("Masukan nama buah yang ingin dicari: ")

if cari in mytuple:
    print(f"{cari} ada dalam tuple")
else:
    print (f"{cari} tidak ada dalam tuple.")
for buah in mytuple:
    jumlah = mytuple.cout(buah)
    print(f"Jumlah kemunculan '{buah}': {jumlah}")