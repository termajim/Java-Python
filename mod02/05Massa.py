#Massa mittojen mukaan leiviskät, naulat ja luodit

leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

luodit_kerroin = 13.3
naulat_kerroin = luodit_kerroin * 32
leiviska_kerroin = luodit_kerroin * naulat_kerroin * 20

leiviskat_gr = leiviska_kerroin * leiviskat
naulat_gr = naulat_kerroin * naulat
luodit_gr = luodit_kerroin * luodit

paino_gr = leiviskat_gr + naulat_gr + luodit_gr

kilogrammaa = int(paino_gr / 1000)
grammaa = round(paino_gr % 1000)

print(f"Massa nykymittojen mukaan on: {kilogrammaa} kilogrammaa ja {grammaa} grammaa")
