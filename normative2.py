#a:
ismlar = ['Mubina', 'Madina', 'Sayyora', 'Amir', 'Kamila']

#b:
ismlar[0] = 'Salim'
#c:
yangi_ism = ismlar.pop(0) #index boyicha qidirib qirqib oladi
print(yangi_ism)

del ismlar[0] #0 elementdagi esmni ochirib tashlaydi

ismlar.remove('Amir') #elementni nomi boyicha ochirib tashlaydi

#d:
yaqinlar = ismlar

#e:
yaqinlar.sort()

#f:
sonlar = []
i = 1
for i in range(101):
    sonlar.append(i)
    print(i)
sonlar.reverse()
print(sonlar)

yangi_sonlar = sonlar[0:11] + sonlar[35:46] + sonlar[90:100]
print(yangi_sonlar)

#1.2

#a:
sonlarr = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#b:
print(sonlarr[3:7])

#c:
# nw_list = list(sonlarr)
# nw_list[3] = 17
# sonlarr = tuple(nw_list)
# print(sonlarr)

#1.3

#a:
talaba_info = {
    'madina':{'ingliz tili': 5, 'matem': 2},
    'soliha':{'ingliz tili': 2, 'matem': 2},
    'akobir':{'ingliz tili': 3, 'matem': 4},
    'malika':{'ingliz tili': 5, 'matem': 5},
}

#b:
talaba_info['sabina']['ingliz tili'] = 5
talaba_info['sabina']['matem'] = 2
print(talaba_info)

#c:
del talaba_info['sabina']
print(talaba_info) #del nomi orqali - key, ochirib tashlaydi, pop esa index orqali olib tashlaydi

#d:
for value in talaba_info.values():
    print(value)

#e:
talaba_info['madina']['ingliz tili'] = 1

#f:
ortacha_baho = {}
for key, value in talaba_info.items():
    avg = sum(value.values()) / len(value)
    ortacha_baho[key] = avg
print(ortacha_baho)

#g:
for key, avg in ortacha_baho.items():
    if avg < 3:
        print(key, avg)
        print("Uchdan kichik bolgani uchun yiqildingiz")

#1.4

#a:
bosh_toplam = set()

#b:
bosh_toplam.update([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#c:
bosh_toplam.remove(5) #elemnt toplmasa error berilad
bosh_toplam.discard(7) #toplmasa berilmaydi

#d:
toplam1 = {1, 2, 3, 4, 5}
toplam2 = {4, 5, 6, 7, 8}

#e:
toplam3 = toplam1.union(toplam2)

#f:
toplam4 = toplam1.intersection(toplam2)
