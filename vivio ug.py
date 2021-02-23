kainputih = 20000
kainhitam = 18000
kainwarna = 15000
batiktangan=20000
batikprint=18000

print('SELAMAT DATANG DI LAYANAN TOKO KAIN DAN BATIK')

Nama=str(input('Masukkan nama anda: '))
print('Apa yang anda butuhkan?')
print('1. Kain')
print('2. Batik')
a=str(input('Masukkan piliohan anda: '))

if a=='1':
    print('Kain mana yang anda inginkan?')
    print('1. Kain Putih')
    print('1. Kain Hitam')
    print('3. Kain Warna')
    b=str(input('Masukkan Pilihan Anda: '))
    if b=='1':
        c=int(input('Berapa meter kain yang anda butuhkan?'))
        if c>100:
            print('Anda mendapat bonus kain sebanyak 5 meter')
            print('jumlah kain anda adalah :',c+5,'meter')
            print('Total biaya yang harus di bayar adalah Rp. ', c*20000)
        else :
            print('Total biaya yang harus di bayar adalah Rp. ', c*20000)

    if b=='2':
        c=int(input('Berapa meter kain yang anda butuhkan?'))
        if c>150 :
            print('Anda mendapat bonus kain sebanyak 3 meter')
            print('Ju7mlah kain anda adalah :',c+3,'meter')
            print('Total biaya yang harus di bayar adalah Rp. ', c*18000)
        else :
            print('Total yang harus di bayar adalah Rp.' ,c*18000)

    if b=='3':
        c=int(input('Berapa meter kain yang anda butuhkan?'))
        if c>200 :
            print('Anda mendapat bonus kain sebanyak 7 meter')
            print('Jumlah kain anda adalah :',c+7,'meter')
            print('Total biaya yang harus di bayar adalah Rp. ', c*15000)
        else :
            print('Total yang harus di bayar adalah Rp.' ,c*15000)
elif a=='2':
    print('Batik apa yang anda butuhkan?')
    print('1. Batik Tangan')
    print('2. Batik Print')
    d=str(input('Masukkan pilihan anda: '))
    if d=='1' :
        e=int(input('Berepa meter batik yang anda butuhkan?'))
        print('Jumlah batik anda adalah ', e,'meter')
        print('Total biaya yang harus di bayar adalah Rp. ', e*20000)
    else:
        e=int(input('Berepa meter batik yang anda butuhkan?'))
        print('Jumlah batik anda adalah ', e,'meter')
        print('Total biaya yang harus di bayar adalah Rp. ', e*18000)
          
    
        
