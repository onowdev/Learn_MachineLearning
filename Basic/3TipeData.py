'''
Tipe data
Cara mengisi nilai variabel ditentukan dengan jenis datanya, 
misalkan untuk tipe data teks (string) maka harus diapit dengan tanda petik ("..."). 
Sedangkan untuk angka (integer) dan boolean tidak perlu diapit dengan tanda petik.
'''
# Contoh

nama_ku = "Onowdev"
umur = 25
tinggi = 170

# Untuk memeriksa tipe data pada suatu variabel, kita bisa menggunakan fungsi type()

print(type(nama_ku))
print(type(umur))
print(type(tinggi))

'''
Jenis-jenis Tipe Data
Secara umum, tipe data primitif dalam python dibagi menjadi tiga jenis:
1. Tipe data angka
2. Tipe data teks
3. Tipe data boolan
'''
#Tipedata angka >> Int & Float

harga = 800000
jarak = 900.978
print(type(harga))
print(type(jarak))

'''
Tipe Data Teks
Tipe data teks dibagi menjadi dua jenis lagi: Char dan string
'''
nama = "Ivan"
jenis_kelamin = 'L'
alamat = """
    Jl. Ular Python, No 212. RT:70 RW:55 Kode:4L901217MA,
    Kelurahan Gaming, Yogyakarta
"""
agama = 'Islam'

print(type(nama))
print(type(jenis_kelamin))
print(type(alamat))
print(type(agama))

'''
Tipe data boolean
Tipe data boolean adalah tipe data yang hanya memiliki dua nilai yaitu True dan False atau 0 dan 1.
Penulisan True dan False, huruf pertamnya harus kapital dan tanpa tanda petik.
'''

bergerak = True
nyala = 1
print(type(bergerak))
print(type(nyala))