
# Nama : Fathur Rahman
# NIM : 065002200013
# display awal
from cmath import log,sqrt

a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
# Penjumlahan
a += b
print()
print("a + b: ",a)
# variabel
a -= b
pengurangan = b - a
perkalian = a*b
sisapembagian = a % b
pembagian = a / b
logaritma = log(a)
perpangkatan = a ** b
akar = sqrt(a + b )
sisabagi1 = (b % a )  



# pengurangan
print(b,"-",a,"=",abs(pengurangan))
# perkalian
print(a,"*",b,"=",perkalian)

# sisa pembagian
print(a,"%",b,"=",sisapembagian)

# Pembagian
print(a,"/",b,"=",pembagian)

# logaritma
print("log", a, "=",abs(logaritma))

# perpangkatan
print(a,"**",b,"=",perpangkatan)

# akar dari a + b
print("AKAR DARI HASIL a + b = ",abs(akar))

# sisa bagi dari hasil b dibagi a
print(b, "%", a,"=", sisabagi1)

