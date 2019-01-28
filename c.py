#Ujian_Top5_News

import requests
print('Selamat datang, mau tahu berita apa hari ini?')
print('[1] Berita seputar teknologi')
print('[2] Berita seputar bisnis')
print('[3] Berita seputar olahraga')
print('[4] Berita seputar kesehatan')
print('[5] Berita seputar science')
kategori = input('Ketik pilihan Anda [1/2/3/4/5] : ')
if kategori == '1':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang technology :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
elif kategori == '2':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang business :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
elif kategori == '3':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang sports :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
elif kategori == '4':
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang health :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])
else:
    url = 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=84b85859b12744358ca6eba326fe65ff'
    data = requests.get(url)
    output = data.json()
    print('Berikut adalah top 5 berita Indonesia bidang science :')
    print('1 - ', data.json()['articles'][1]['title'])
    print('2 - ',data.json()['articles'][2]['title'])
    print('3 - ',data.json()['articles'][3]['title'])
    print('4 - ',data.json()['articles'][4]['title'])
    print('5 - ',data.json()['articles'][5]['title'])

'''
kategori = {
    1: 'technology',
    2: 'business',
    3: 'sports',
    4: 'health',
    5: 'science'
}
    if konversi == '1':
        bank = input('Silakan ketik bank pilihan Anda : ')
        if bank.lower() in listbank:
            url = 'https://kurs.web.id/api/v1/'+bank.lower()
            nominal = input('Silakan input nominal uang yang akan dikonversi : Rp. ')
            data = requests.get(url)
            kursJual = data.json()["jual"]
            kursBeli = data.json()["beli"]
            hasil = int(nominal) / int(kursJual)
            hasil2 = round(hasil, 2)
            print('Hasil konversi Rp', nominal, 'adalah USD', hasil2)
            print('Dengan kurs jual =', kursJual, '& kurs beli =', kursBeli)
        else:
            print('Maaf bank tidak tersedia')
    elif konversi == '2':
        bank = input('Silakan ketik bank pilihan Anda : ')
        if bank.lower() in listbank:    
            nominal = input('Silakan input nominal uang yang akan dikonversi : US$. ')
            data = requests.get(url)
            kursJual = data.json()["jual"]
            kursBeli = data.json()["beli"]
            hasil = int(nominal) * int(kursJual)
            hasil2 = round(hasil, 2)
            print('Hasil konversi US$', nominal, 'adalah Rp.', hasil2)
            print('Dengan kurs jual =', kursJual, '& kurs beli =', kursBeli)
        else:
            print('Maaf bank tidak tersedia')
    elif konversi == '3':
        nominal = input('Silakan input nominal uang yang akan dikonversi : US$. ')
        link = 'https://blockchain.info/tobtc?currency=USD&value='
        data = requests.get(link+nominal).json()
        print('Hasil konversi US$', nominal, 'adalah BTC', data)
    else:
        print('Maaf layanan tidak tersedia')
'''