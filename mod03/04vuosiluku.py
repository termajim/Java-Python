#Vuosiluku ohjelma

vuosiluku = int(input("Syötä vuosiluku: "))
if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print(f"{vuosiluku} on karkausvuosi.")
else:
    print(f"{vuosiluku} ei ole karkausvuosi. Karkausvuosi on jos vuosi on jaollinen 4, 100 jos se on jalollinen 400!")
