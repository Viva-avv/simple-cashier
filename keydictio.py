# MULTIKEY DICTIONARY
print("-"*50)
import datetime
mahasiswa1 = {
    'nama':'Viva Dragneel',
    'nim':1902201,
    'sks_lulus':60,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,4,11)
}
mahasiswa2 = {
    'nama':'Kenma Kozume',
    'nim':1902203,
    'sks_lulus':30,
    'beasiswa':True,
    'lahir':datetime.datetime(1995,10,16)
}
mahasiswa3 = {
    'nama':'Naruto',
    'nim':1902204,
    'sks_lulus':20,
    'beasiswa':False,
    'lahir':datetime.datetime(1995,10,10)
}
data_mahasiswa = {
    'MAH01':mahasiswa1,
    'MAH02':mahasiswa2,
    'MAH03':mahasiswa3,
}
print(f"{'KEY': <6} {'Nama': <14} {'sks': <4} {'Beasiswa': <10} {'Lahir': <10}")
print("-"*50)

for mahasiswa in data_mahasiswa :
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY: <6} {NAMA: <14} {SKS: ^4} {BEASISWA: ^10} {LAHIR: <10}")

