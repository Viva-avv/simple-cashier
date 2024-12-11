# contoh generic
nama = "viva"
umur = "20"
format_str = f"hai {nama} ,{umur}"
print(format_str)

# bilangan desimal
angka = 2001.0411
format_str = f"desimal = {angka:.2f}" #gunakan F krn data float
print(format_str)

# memformat persen
persentase = 0.0411
format_persen = f"persen = {persentase:%}"
print(format_persen)
persentase = 0.0411
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# operasi aritmatika dalam placeholder
angka = 11
jumlah = 400
format_str = f"harga total = Rp.{angka*jumlah:,}"
print(format_str)

## string multilne
nama = "viva"
umur = 20
tb = 158
bb = 42
misal = f"""
n = {nama}
u = {umur}
t = {tb}
b = {bb}
"""
print(misal)