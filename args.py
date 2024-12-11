# FUNGSI DENGAN *ARGS
def struk (*barang) :
    benda = barang[0]
    harga = barang[1]
    pcs = barang[2]
    merk = barang[3]
    print(f" jenis = {benda}\n harga = {harga}\n berapa pcs = {pcs}\n merk = {merk}")
struk("Kipas", 15000, 1, "Loid")

# FUNGSI DENGAN **KWARGS
def math (*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("not")
    return output
hasil = math(3,7,option="tambah")
print(f"hasil tambah {hasil}")
hasil = math(6,2,option="kali")
print(f"hasil kali {hasil}")