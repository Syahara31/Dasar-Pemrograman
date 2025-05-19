from datetime import datetime

def hitungUmur(tahunLahir):
    tahunIni = datetime.now().year
    umur = tahunIni - tahunLahir
    return umur

tahunLahir = int(input ("Masukam Tahun Lahir: "))
umur = hitungUmur(tahunLahir)
print("Umur", umur, "Tahun")
