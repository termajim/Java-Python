# Kysy käyttäjältä numeroita kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi

def main():
    luvut = []

    while True:
        syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")
        if syote == "":
            break
        try:
            luku = float(syote)
            luvut.append(luku)
        except ValueError:
            print("Virheellinen syöte. Syötä luku tai tyhjä merkkijono lopettaaksesi.")

    if len(luvut) == 0:
        print("Et syöttänyt yhtään lukua.")
    else:
        luvut.sort(reverse=True)
        print("Viisi suurinta lukua:")
        for luku in luvut[:5]:
            print(luku)


if __name__ == "__main__":
    main()
