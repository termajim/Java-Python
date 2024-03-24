class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nytnopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenmuutos):
        self.nytnopeus = self.nytnopeus + nopeudenmuutos
        if self.nytnopeus > self.huippunopeus:
            self.nytnopeus = self.huippunopeus
        if self.nytnopeus < 0:
            self.nytnopeus = 0
        return

    def kulje(self, tuntimaara):
        self.matka += self.nytnopeus * tuntimaara
        return

autot = []
import random
for nro in range(1, 11):
    rekkari = 'ABC-' + str(nro)
    maxnopeus = random.randint(100, 200)
    kuski = Auto(rekkari, maxnopeus)
    autot.append(kuski)

kesto = 0
tavoite = 10000
jatkuu = True

while jatkuu:
    for kilpailija in autot:
        muutos = random.randint(-10, 15)
        kilpailija.kiihdyta(muutos)
        if kilpailija.matka >= tavoite:
            jatkuu = False

    kesto += 1
print(f'Kilpailu päättyi, se kesti {kesto} tuntia.')
print(f'Rekkari\t huippunopeus\t kuljettumatka')
for kaara in autot:
    print(f'{kaara.rekisteritunnus:10s} {kaara.huippunopeus:10d} {kaara.nopeus:10d} {kaara.matka:12d}')