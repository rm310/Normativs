import random

#1.1

#a:
harorat = int(input("Haroratni kiriting: "))
if harorat < 0:
    print("Sovuq kun, issiqroq kiyining!")
elif 0 <= harorat <= 20:
    print("Ob-Havo yaxshi, lekin sovuq.")
else:
    print("Juda yaxshi ob-havo, zavqlaning!")

#b:
f_yosh = int(input("Futbolchini yoshini kiriting: "))
gollar = int(input("Gollarni kiriting: "))
#b1:
if f_yosh < 18:
    print("Yosh istedod!")
else:
    print("Mashq qilish kerak.")

#b2:
if 18 <= f_yosh <= 35:
    if 3 < gollar:
        print("Yulduz futbolchi!")
    else:
        print("Oddiy futbolchi!")

#b3:
if f_yosh > 35:
    if gollar > 1:
        print("Maglubiyatsiz veteran!")
    else:
        print("Tajribali murabbiy")

#1.2

#a:
num = [1, 2, 3, 4, 5]
kattasi = num[0]
for i in num[1:]:
    if kattasi < i:
        kattasi = i
print(f"listda eng kattasi bu {kattasi}")

#b:
num = [1, 2, 3, 4, 5]
kichigi = num[0]
for i in num[1:]:
    if kichigi > i:
        kichigi = i
print(f"listda eng kichigi bu {kichigi}")

#c:
num = [1, 2, 3, 4, 5]
yigindisi = 0
for i in num:
    yigindisi += i
print(f"Hamma sonlarni yigindisi - {yigindisi}")

#d:
num = [1, 2, 3, 4, 5]
kopaytmasi = num[0]
for i in num[1:]:
    kopaytmasi *= i
print(f"Hamma sonlarni yigindisi - {kopaytmasi}")

#f:
i = 1
j = 1
for i in range(10):
    for j in range(10):
        print(f"{i} * {j} = {i * j}")
    print()

#1.3:
son = random.randint(1,20)
while(True):
    s = int(input("Butun son kiriting: "))
    if s < son:
        print("Berilgan son siznikidan kattaroq")
    if son == s:
        print("Tabriklaymz! toptingiz")
        break
    if son < s:
        print("Berilgan son siznikidan kichikroq")