# Tehdään luokkahierarkia Python kielellä lehti

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivuja):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivuja
        super().__init__(nimi)

    def tulostatiedot(self):
        print(f'Kirja: {self.nimi} {self.kirjoittaja} ja sivujen määrä {self.sivumäärä}')


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulostatiedot(self):
        print(f'Lehti: {self.nimi}: Päätoimittaja on {self.päätoimittaja}')


lehti = Lehti(f'Aku Ankka', 'Aki Hyyppä')
kirja = Kirja(f'Hytti n:0 6', 'Rosa Liksom', 200)

lehti.tulostatiedot()
kirja.tulostatiedot()
