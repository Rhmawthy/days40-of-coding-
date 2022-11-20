#program menentukan bilangan genap dan ganjil

bilangan = int(input("masukkan angka"))

#kondisi
if bilangan %2 == 0:
    print ("bilangan genap")
elif bilangan %2 != 0:
    print("bilangan ganjil")
