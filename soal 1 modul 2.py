
# Nama : Fathur Rahman
# NIM : 065002200013
# display awal
import math
print("\n===SILAHKAN MASUKKAN NILAI===")
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
print("\n==HASIL PERHITUNGAN==")
# Penjumlahan
a += b
print("\nPENJUMLAHAN A DAN B: ",a)

# variabel
a -= b
pengurangan = b - a
perkalian = a*b
sisapembagian = a % b
pembagian = a / b
logaritma = math.log(a)
perpangkatan = a ** b
akar = math.sqrt(a + b )
sisabagi1 = (b % a )  



# OUTPUT
print("PENGURANGAN B DAN A: ",abs(pengurangan))
print("PERKALIAN A DAN B: ",perkalian)
print("SISA BAGI A DAN B: ",sisapembagian)
print("PEMBAGIAN A DAN B: ",pembagian)
print("log (",a ,") :",abs(logaritma))
print("A PANGKAT B: ",perpangkatan)
print("AKAR DARI HASIL a + b = ",abs(akar))
print("SISABAGI B DAN A: ", sisabagi1)

