# Ympyrän likiarvon laskemista
import random

def laskepi(n):
    pisteiden_sisalla = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            pisteiden_sisalla += 1
    pi_likiarvo = 4 * pisteiden_sisalla / n
    return pi_likiarvo

def main():
    try:
        pisteiden_maara = int(input("Syötä arvottavien pisteiden määrä: "))
        if pisteiden_maara <= 0:
            print("Virhe: Pisteiden määrän tulee olla positiivinen kokonaisluku.")
            return
        pi_likiarvo = laskepi(pisteiden_maara)
        print(f"Piin likiarvo on: {pi_likiarvo}")
    except ValueError:
        print("Virhe syötteen tulee olla kokonaisluku")

if __name__ == "__main__":
    main()
