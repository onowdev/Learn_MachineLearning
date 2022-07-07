"""
Konversi Tipe Data
Meskipun Python telah otomatis mendeteksi tipe data yang tersimpan dalam variabel, tapi ada kalanya kita perlu melakukan konversi tipe data.

Misalkan, pada contoh berikut ini:

a = 10
b = 3
c = a / b

print(c) #output: 3

Pembagian nilai a dan b menghasilkan 3 (integer). Mengapa demikian?

Karena nilai a dan b bertipe integer, maka hasilnya pun berupa integer.

Bagaimana agar hasilnya ada komanya?

Tentu kita harus merubah tipe variabel a dan b menjadi bilangan pecahan (float) dulu, baru setelah itu dibagi.

a = 10
b = 3
c = float(a) / float(b) #output: 3.3333333333333335

print(c)

===============
Fungsi-fungsi untuk mengubah tipe data:

1. int() untuk mengubah menjadi integer;
2. long() untuk mengubah menjadi integer panjang;
3. float() untuk mengubah menjadi float;
4. bool() untuk mengubah menjadi boolean;
5. chr() untuk mengubah menjadi karakter;
6. str() untuk mengubah menjadi string.
7. bin() untuk mengubah menjadi bilangan Biner.
8. hex() untuk mengubah menjadi bilangan Heksadesimal.
9. oct() untuk mengubah menjadi bilangan okta.
"""
a = 900
b = 20
c = a/b
print(c)
d = float(a) / float(b)
print(d)