# FUNGSI DENGAN RETURN
def kuadrat (contoh_input) :
    contoh_output = contoh_input**2
    return contoh_output
y = kuadrat(3)
print(y)

print(kuadrat(11))

v = 4 + (kuadrat(6))
print(v)


# FUNGSI DENGAN RETURN BANYAK
def operasi_mtk (angka1,angka2) :
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah,kurang,kali,bagi

v,w,x,y = operasi_mtk (11,4)
print(f"hasil tambah = {v}")
print(f"hasil kurang = {w}")
print(f"hasil kali = {x}")
print(f"hasil bagi = {y}\n")

# DEFAULT ARGUMENT FUNGSI
def say_hi (nama, pesan="apa kabar") :
    print(f"hallo {nama}, {pesan}")
say_hi("Viva", "hai wibu")
say_hi("shinichi")
