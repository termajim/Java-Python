#Tehdään hissi luokka

class Hissi:
    def __init__(self, alin_kerros, ylinkerros):
        self.alin_kerros = alin_kerros
        self.ylinkerros = ylinkerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, tavoite):
        if tavoite > self.kerros:
            while self.kerros < tavoite:
                self.kerros_ylos()
        elif tavoite < self.kerros:
            while self.kerros > tavoite:
                self.kerros_alas()

        print("Hissi on halutussa kerroksessa")
        return

    def kerros_ylos(self):
        self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return


ekaHissi = Hissi(1, 7)
ekaHissi.siirry_kerrokseen(4)
ekaHissi.siirry_kerrokseen(1)
