#Sama kaava kuin aikasempi tehtävä, mutta lisätään kiihdytys

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nytnopeus = 0
        self.matka = 0

auto1 = Auto('ABC-123', '142km/h')

print(f'Auto rekistorinumero on {auto1.rekisteritunnus} \nhuippu nopeus on {auto1.huippunopeus} \ntämän hetkinen nopeus on {auto1.nytnopeus} \nkuljettu matka {auto1.matka}')