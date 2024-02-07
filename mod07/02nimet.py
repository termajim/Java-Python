# Kysyy käyttäjältä nimeä siihen saakka
# kunnes käytjjäjä syöttää tyhjän merkkijonon
# Kunkin syöttämän nimen jälkeen ohjelma tulostaa
# joko tekstin Uusi nimi tai Aimmenin syötetty nimi sen mukaan
# syötettiinkö nimi ensimmäistä kertaa
# Lopuksi ohjelma luettelee syätetyt nimet yksi kerrallaan allekain
# mielivaltaisesti järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen

nimet = set()

while True:
    nimi = input("Kerro nimi: ")
    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nAnnoit seuraavat nimet: ")
for nimi in nimet:
    print(nimi)
