# Nested List
#contoh penggunaan
pesertaV = ["viva",20,"wanita"]
pesertaY = ["yamada",17,"laki-laki"]
list_peserta = [pesertaV,pesertaY]
for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"gender\t : {peserta[2]}")