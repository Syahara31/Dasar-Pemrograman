def welcomeName(name) :
    print("Halo", name, "Selamat Datang")

def welcFromArr(names):
    for name in names:
        print("Halo", name, "Selamat Datang")

names = ["Nurul","Febri","Deni","Raisa"]
for name in names :
    welcomeName(name)

welcFromArr(names)