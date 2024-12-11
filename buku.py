print("       ======TOKO BUKU VIVA======")
print("-"*40)
daftar0 = ["One Piece",220,111324,45000,12]
daftar1 = ["Hunter x Hunter",125,222324,60000,10]
daftar2 = ["Black Clover",240,333324,55000,4]
daftar3 = ["Kaijuu",170,444324,55000,6]
daftar4 = ["Wind Breaker",215,555324,40000,5]
Store = [daftar0,daftar1,daftar2,daftar3,daftar4,]
for book in Store:
    print(f"Judul\t  : {book[0]}")
    print(f"Stok\t  : {book[1]}")
    print(f"Kode Buku : {book[2]}")
    print(f"Harga Buku : {book[3]}")
    print(f"Diskon : {book[4]}")
    print("-"*20)
while True :
    kode = input("Kode Buku :")
    buku_ditemukan = []
    ditemukan = False
    for item in Store:
        if item[2] == int(kode):
            buku_ditemukan = item
            ditemukan = True
            break

    if ditemukan == True :
        print(f"Judul = {buku_ditemukan[0]}")
        print(f"Kode = {buku_ditemukan[2]}")
        print(f"Stok = {buku_ditemukan[1]}")
        print(f"Harga = Rp{buku_ditemukan[3]}")
        print(f"Diskon = %{buku_ditemukan[4]}")
        
        harga = buku_ditemukan[3]
        diskon = buku_ditemukan[4]

        price = harga - (harga * diskon / 100)
        jumlah = int(input("Jumlah buku :"))
        
        total = price * jumlah
        print(f"Totalnya = {total}")
        pembayaran = int(input("pembayaran :"))
        kembalian = pembayaran - total
        print(f"uang kembali Rp.{kembalian}")

        lanjut = input("Lanjut beli? (yes/no) :")
        if lanjut == "no":
            break
    else :
        print("Buku tidak ditemukan")
        lanjut = input("Lanjut beli? (yes/no) :")
        if lanjut == "no":
            break
print("Terimakasih telah belanja di Toko Viva")