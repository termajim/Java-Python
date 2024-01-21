#Suorakulmio piiri ja pinta-ala
import math

kanta = float(input("Syötä suorakulmion kanta: "))
korkeus = float(input("Syötä suorakulmion korkeus: "))

pinta_ala = kanta * korkeus
piiri = (kanta + korkeus) * 2

print("Suorakulmion pinta-ala on: %.2f" % pinta_ala)
print("Suorakulmion piiri on: %.2f" % piiri)
