#jeje
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

    def kulje(self, tuntimaara):
        self.matka += self.nytnopeus * tuntimaara
        return

auto1 = Auto('ABC-123', '142km/h')

print(f'Auton rekisteritunnus on {auto1.rekisteritunnus}'
      f'\nHuippunopeus {auto1.huippunopeus}km/h'
      f'\nTämän hetkinen nopeus {auto1.nytnopeus}km/h')

auto1.kiihdyta(60)
auto1.kulje(1.5)

print(f'Auto kulkenut 1.5 tunnin ajon jälkeen: {auto1.matka}km')
