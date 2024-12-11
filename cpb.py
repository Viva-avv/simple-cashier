# continue (membuat loop meloncat ke step next)
angka = 0
print(f"contoh -> {angka}")
while angka < 5:
    angka += 1
    print(f"contoh -> {angka}")

    if angka == 3: #melompat sesuai angka yg diminta
        print("nomor tiga") #ada continue hanya masuk di no 3
        continue
    print("bukan tiga") #melompati no 3
print("stop\n")

# Pass
angka = 0
print(f"contoh -> {angka}")
while angka < 5:
    angka += 1
    print(f"contoh -> {angka}")

    if angka == 3: #print masuk di no 3
        print(" hanya ad di nomor tiga") # ada pass hanya masuk d no3
        pass
    print("ini") # masuk disemua angka
print("stop\n")

# Break
angka = 0
while angka < 5:
    angka += 1
    print(f"contoh -> {angka}")

    if angka == 3: #print berhenti sampai angka 3
        print(" hanya ad di nomor tiga") # hanya masuk di no3
        break
    print("ini") # stop sampai no3
print("stop\n")