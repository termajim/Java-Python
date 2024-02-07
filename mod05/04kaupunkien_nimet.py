# Kaupungin nimet ohjelma

def main():
    kaupungit = []

    for i in range(5):
        kaupunki = input(f"Syötä {i+1}. kaupungin nimi: ")
        kaupungit.append(kaupunki)

    print("Kaupungit:")
    for kaupunki in kaupungit:
        print(kaupunki)

if __name__ == "__main__":
    main()
