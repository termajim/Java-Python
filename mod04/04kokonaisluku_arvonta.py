# Kokonaisluku arvonta ohjelma
import random

def arvaa_luku():
    oikea_luku = random.randint(1, 10)

    while True:
        arvaus = int(input("Arvaa luku 1-10 välillä: "))

        if arvaus < oikea_luku:
            print("Luku on liian pieni")
        elif arvaus > oikea_luku:
            print("Luku on liian suuri")
        else:
            print("Arvasit oikein")
            break
arvaa_luku()