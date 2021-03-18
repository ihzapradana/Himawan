def penjumlahan (a,b):
    return a + b
def pengurangan (a,b):
    return a - b
def perkalian (a,b):
    return a * b
def pembagian (a,b):
    return a / b
def pangkat (a,b):
    return a**b
def akar (a,b):
    return a**1/b
print('Tentukan Pilihan Anda:')
print('1. Penjumlahan \n2. Pengurangan \n3. Perkalian \n4. Pembagian \n5. Pangkat 2 \n6. akar')
pilihan = int(input('Operasi apa yang anda inginkan?: '))
def inputan():
    global angka1
    global angka2
    angka1 = int(input('masukkan angka pertamanya: '))
    angka2 = int(input('masukkan angka keduanya: '))
    
if pilihan == 1:
    inputan()
    print(angka1, '+', angka2, '=', penjumlahan(angka1,angka2))
        
elif pilihan == 2:
    inputan()
    print(angka1, '-', angka2, '=', pengurangan(angka1,angka2))
        
elif pilihan == 3:
    inputan()
    print(angka1, '*', angka2, '=', perkalian(angka1,angka2))
       
elif pilihan == 4:
    inputan()
    print(angka1, '/', angka2,'=', pembagian(angka1,angka2))
elif pilihan == 5:
    inputan()
    print(angka1, '^', angka2, '=', pangkat(angka1,angka2))
elif pilihan == 6:
    inputan()
    print(angka1, 'akar', angka2, '=', akar(angka1,angka2))
else:
    print('maaf, input yang anda masukkan salah!')

    
