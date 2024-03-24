#Auto luokka rek-numerot, huippunopeus, tämän hetkinen nopeus ja kuljettumatka

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nytnopeus = 0
        self.matka = 0

auto1 = Auto('ABC-123', '142km/h')

print(f'Auto rekistorinumero on {auto1.rekisteritunnus} \nHuippu nopeus on {auto1.huippunopeus} \nTämän hetkinen nopeus on {auto1.nytnopeus} \nKuljettu matka {auto1.matka}')