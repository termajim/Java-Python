#Sama kaava kuin aikasempi tehtävä, mutta lisätään kiihdytys

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = int(huippunopeus.rstrip('km/h'))
        self.nytnopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenmuutos):
        if nopeudenmuutos > 0:
            if self.nytnopeus + nopeudenmuutos <= self.huippunopeus:
                self.nytnopeus += nopeudenmuutos
            else:
                self.nytnopeus = self.huippunopeus
        elif nopeudenmuutos < 0:
            if self.nytnopeus + nopeudenmuutos >= 0:
                self.nytnopeus += nopeudenmuutos
            else: self.nytnopeus = 0


auto1 = Auto('ABC-123', '142km/h')

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f'Auto rekistorinumero on {auto1.rekisteritunnus} \nHuippu nopeus on {auto1.huippunopeus}km/h \nTämän hetkinen nopeus on {auto1.nytnopeus}km/h \nKuljettu matka alussa {auto1.matka}')

#Hätäjarrutus
auto1.kiihdyta(-200)
print(f'Auton nopeus hätäjarrutuksen jälkeen on {auto1.nytnopeus}km/h')