# lentoaseman syöttö ohjelma

lentoasemat = {}

while True:
    print("\nValitse toiminto: ")
    print("1. Lisää uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valintasi (1/2/3): ")

    if valinta == "1":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao_koodi] = nimi
        print("Uusi lentoasema lisätty.")
    elif valinta == "2":
        icao_koodi = input("Syötä haettavan lentoaseman ICAO-koodi: ")
        if icao_koodi in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao_koodi]}")
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break
    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")
