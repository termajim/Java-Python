# Jatkoa kilpailu tehtävään
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, aika):
        self.matka += self.nopeus * aika
        return


'''
    Määritellään Kilpailu-luokka
'''
class Kilpailu:
    def __init__(self, nimi, pituus, kilpailijat):
        self.kilpailun_nimi = nimi
        self.kilpailun_pituus = pituus
        self.kilpailijat = kilpailijat

    def tunti_kuluu(self):
        for auto in self.kilpailijat:
            muutos = random.randint(-10, 15)

    def tulosta_tilanne(self):
        print("Rekkkari\t huippunopeus\t nopeus\t kuljettu matka")
        for kaara in self.kilpailijat:
            print(f"{kaara.rekisteritunnus:10s} {kaara.huippunopeus:10d} {kaara.nopeus:10d} {kaara.matka:12d}")

    def kilpailu_ohi(self):
        vastaus = False
        for kaara in self.kilpailijat:
            if kaara.matka > 8000:
                vastaus = True
                break
        return vastaus


kilpailijat = []

for nro in range(1, 11):
    rekkari = "ABC-" + str(nro)
    huippunop = random.randint(100, 200)
    kaara = Auto(rekkari, huippunop)
    kilpailijat.append(kaara)

romuralli = Kilpailu("Suuri romuralli", 8000, kilpailijat)
kilpailun_kesto = 0
kilpailu_paattynyt = False

while kilpailu_paattynyt != True:
    romuralli.tunti_kuluu()
    kilpailu_paattynyt = romuralli.kilpailu_ohi()
    kilpailun_kesto += 1
    if kilpailun_kesto % 10 == 0:
        print(f"Kilpailu on kestänyt {kilpailun_kesto} tuntia, tilanne:")
        romuralli.tulosta_tilanne()
    break

print(f"Kilpailu on päättynyt {kilpailun_kesto} tunnin jälkeen")
print("* Alla ovat kilpailun lopputulokset *")
romuralli.tulosta_tilanne()