#autot ali luokat sähköauto ja polttomoottori

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def ajo(self, tuntia):
        self.matkamittari += self.huippunopeus * tuntia


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def tulostatiedot(self):
        print(f'Sähköauto ajoi {sähköauto.matkamittari}km 3h matkan aikana.')


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)

    def tulostatiedot(self):
        print(f'Bensa-auto ajoi {polttoauto.matkamittari}km 3h matkan aikana.')



sähköauto = Sähköauto(f'ABC-15', 180, 52.5)
sähköauto.ajo(3)
polttoauto = Polttomoottoriauto(f'ACD-123', 165, 32.3)
polttoauto.ajo(3)

sähköauto.tulostatiedot()
polttoauto.tulostatiedot()
