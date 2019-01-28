#Ujian_FPB_KPK

angka1 = int(input('Ketik angka pertama        : '))
angka2 = int(input('Ketik angka kedua          : '))

def fpb(angka1, angka2):
    while 1:
        sisa = angka1 % angka2
        if sisa == 0:
            break
        angka1, angka2 = angka2, sisa
    print('FPB dari ', angka1, ' dan ', angka2, ' adalah = ', angka2)

def kpk(angka1, angka2):
    x = 1
    y = 1
    p = angka1 * x
    q = angka2 * y
    while p != q:
        while p > q:
            y += 1
            q = angka2 * y
        while p < q:
            x += 1
            p = angka1 * x
    if p == q:
        print('KPK dari ', angka1, ' dan ', angka2, ' adalah = ', p)
fpb(angka1, angka2)
kpk(angka1, angka2)