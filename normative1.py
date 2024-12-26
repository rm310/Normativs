print("\"O\'zbekiston Vatan\"im meni!!!")
print()

#2
tezlik = float(input("Tezlikni kiriting: "))
masofa = float(input("Masofani kiriting: "))
vaqt = masofa / tezlik
print(f"bosib otilgan masofani vaqti {vaqt}")
print()

#3
#birinchiga ozbekiston sozini print qilamiz
#ikkinchiga vaqtni topamiz
#uchinchiga izoh yozamz
#tortinchiga code ni togrlaymz
#beshinchiga ikkita ozgaruvchini joyini almashtramz
#oltnchga ozgaruvchilardan matn yasaymz
#yettinchiga arifmetik amallarni ishlatamz

#4
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("New lines can be created with a \\ and the letter n")
print()

#5
a = float(input("Birinchi raqamni kiriting: "))
b = float(input("Ikkinchi raqamni kiriting: "))
c = a
a = b
b = c
print("Birinchi raqamni ozgartirlgan qiymati: ", a)
print("Ikkinchi raqamni ozgartirilgan qiymati: ", b)
print()

#6
kocha = "Bog\'bon"
mahalla = "Sog\'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
manzil = f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
print()