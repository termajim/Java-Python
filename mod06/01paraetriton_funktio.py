# Parametriton funktio ohjelma
import random

def noppa():
    return random.randint(1, 6)

def main():
    while True:
        silmaluku = noppa()
        print("Nopan silmäluku:", silmaluku)
        if silmaluku == 6:
            break

if __name__ == "__main__":
    main()
