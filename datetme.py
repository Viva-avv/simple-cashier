# date and time
import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)

tanggal = dt.date(2001,4,11)
print(tanggal)

print("masukkan tgl lahir")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))
tgl_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda : {tgl_lahir}")
print(f"Hari : {tgl_lahir:%A}") # gunakan %A >untuk hari

# hitung umur
hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur = hari_ini - tgl_lahir #dikurangi
print(f"umur anda: {umur}")
