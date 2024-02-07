# Ohjelma kysyy käyttäjältä arpakuutioiden lukumäärää
import random

def arpakuution_heitto():
    lkm = int(input("Anna arpakuutioiden lukumäärä: "))
    silmalukujen_summa = 0
    for _ in range(lkm):
        silmaluku = random.randint(1, 6)
        print(f"Heitto: {silmaluku}")
        silmalukujen_summa += silmaluku
    print(f"Arpakuutioiden silmäluku summa: {silmalukujen_summa}")

arpakuution_heitto()
