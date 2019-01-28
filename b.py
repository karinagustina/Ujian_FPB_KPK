#Ujian_Kategori_Bilangan

angka = int(input('Ketik angka : '))

def KategoriBilangan(angka):
    if angka>=0 or angka<=0:
        return 'bulat'
    elif angka>=0:
        return 'cacah'
    elif angka< 0:
        return 'negatif'
    elif angka == 0:
        return 'nol'
    elif angka>0:
        return 'asli'
    elif angka%2 != 0:
        return 'ganjil'
    elif angka%2 == 0:
        return 'genap'
    elif angka>1 and angka/1==angka and angka/angka==1:
        return 'prima'
    else:
        return 'komposit'
print(KategoriBilangan(angka))