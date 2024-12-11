print("====KALKULATOR====\n")
angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (+,-,*,/) : ")
angka_2 = float(input("masukkan angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("yang bener aja, rugi dong")

print("akhir dari program")