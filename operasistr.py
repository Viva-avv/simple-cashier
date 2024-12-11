# menyambung string
nama_pertama = "Viva"
nama_tengah = "D"
nama_belakang = "Dragneel"
nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_belakang
print(nama_lengkap)

panjang = len(nama_lengkap)
print(panjang)

# operasi untuk string
d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " =" + str(status))

d = "Viva"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " =" + str(status))

# mengulang string
print("ha"*5)
print(6*"ya")

# indexing
print("index ke-3 : " +  nama_lengkap[3])
print("index ke-(-3) : " +  nama_lengkap[-3])
print("index ke-[0:4] : " +  nama_lengkap[0:4])

#item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling
print("paling besar : " + max(nama_lengkap))
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))

# mengubah case dari string
salam = "hai viva"
salam = salam.upper()
print("upper = " + salam) #upper = huruf besar
jepang = "WibuuUuu"
jepang = jepang.lower()  #lower = huruf kecil
print("lower = " + jepang)

#pengecekan isX method
salam = "hai vivaaa"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower)) #hasilnya bool
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalnum() > akan false jika huruf dan angka digabungkan
hurang = "Viva 11 April"
cek_ha = hurang.isalnum()
print(hurang + " is alnum = " + str(cek_ha))
hurang = "viva"
cek_ha = hurang.isalnum()
print(hurang + " is alnum = " + str(cek_ha))
hurang = "11"
cek_ha = hurang.isalnum()
print(hurang + " is alnum = " + str(cek_ha))

# alokasi karakter rjust(), ljust(), center()
kanan = "viva".rjust(8)
print("'"+kanan+"'")
tengah = "vivaaa".center(12,"-")
print("'"+tengah+"'")
# strip()
tengah = "vivaaa".strip("-")
print("'"+tengah+"'")

# join(), split()
pisah = ['viva','chan','wibu']
v = ','.join(pisah)
print(v)
pisah = ['viva','chan','wibu']
v = ' '.join(pisah)
print(v)

gabung = "vivayachanyawibu"
print(gabung.split('ya'))
viva = "naruto-h-boruto"
print(viva.split('h'))