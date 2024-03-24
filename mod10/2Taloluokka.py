class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerros = alinkerros

    def siirry_kerrokseen(self, tavoite):
        while self.kerros != tavoite:
            if tavoite > self.kerros:
                self.kerros_ylos()
            elif tavoite < self.kerros:
                self.kerros_alas()

        print("Hissi on halutussa kerroksessa")
        return

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros = self.kerros + 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")
        return


class Talo:
    def __init__(self, alin_kerros, ylin, lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin
        self.hissien_lkm = lkm
        self.hissit = []
        for nro in range(lkm):
            uusiHissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(uusiHissi)

    def aja_hissia(self, hissin_nro, kohdekerros):
        ajettavaHissi = self.hissit[hissin_nro - 1]
        ajettavaHissi.siirry_kerrokseen(kohdekerros)



ekaTalo = Talo(1, 5, 3)
ekaTalo.aja_hissia(1, 3)
ekaTalo.aja_hissia(2, 4)

for tutkittava_hissi in ekaTalo.hissit:
    print(f"Hissi on kerroksessa {tutkittava_hissi.kerros} ")