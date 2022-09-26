# NAMA : FATHUR RAHMAN
# NIM : 065002200013
# JURUSAN : SISTEM INFORMASI
import math as q
print("\n--MENGHITUNG JARAK ANTARA DUA TITIK DIBUMI--")
x1 = float(input("\nMasukkan lattitude kota pertama: "))
y1 = float(input("Masukkan longitude kota pertama: "))
x2 = float(input("Masukkan lattitude kota kedua: "))
y2 = float(input("Masukkan longitude kota kedua: "))
a = x2 - x1
b = y2 -y1
rumus = q.sin(q.radians(a/2))**2 - q.cos(q.radians(x1))*q.cos(q.radians(x2))*q.sin(q.radians(b/2))**2
rumus1 = 2*q.asin(q.sqrt(rumus))
r = 6371.01
hasil = rumus1*r
print("\nJarak antara dua titik adalah: ",abs(hasil),"Kilometer")