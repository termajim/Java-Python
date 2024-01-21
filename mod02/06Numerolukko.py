# Arpa numerolukko ohjelma
import random

koodi1 = int(input("Esitä 3 numeron koodi, 0-9 väliltä: "))
koodi2 = int(input("Esitä 4 numeron koodi, 1-6 väliltä: "))

kolmenumeroinen_koodi = (random.randint(0, 9) for _ in range(3))
nelinumeroinen_koodi = (random.randint(1, 6) for _ in range(4))

print("Kolmenumeroinen lukkokoodi: ", ''.join(map(str, kolmenumeroinen_koodi)))
print("Nelinumeroinen lukkokoodi: ", ''.join(map(str, nelinumeroinen_koodi)))
