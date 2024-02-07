# Edellisen tehtävän muokattu parametri
import random

def noppa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

def main():
    while True:
        try:
            maksimisilmaluku = int(input("Anna nopan maksimisilmäluku: "))
            if maksimisilmaluku <= 0:
                print("Virhe nopan maksimisilmäluvun tulee olla positiivinen kokonaisluku.")
            else:
                break
        except ValueError:
            print("Virhe syötteen tulee olla kokonaisluku.")

    while True:
        silmaluku = noppa(maksimisilmaluku)
        print("Nopan silmäluku:", silmaluku)
        if silmaluku == maksimisilmaluku:
            break

if __name__ == "__main__":
    main()
