# käyttäjätunnus ja salasana ohjelma

def kirjaudu_sisaan():
    oikea_kayttajatunnus = "python"
    oikea_salasana = "rules"
    yritykset = 0

    while yritykset < 5:
        kayttajatunnus = input("Syötä käyttäjätunnus: ")
        salasana = input("Syötä salasana: ")

        if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
            print("Tervetuloa!")
            return
        else:
            print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
            yritykset += 1

    print("Pääsy evätty.")
kirjaudu_sisaan()
