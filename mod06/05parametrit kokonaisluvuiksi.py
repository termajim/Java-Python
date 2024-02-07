# Parametrit luvuiksi 2 ohjelma

def poista_parittomat(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Voit muuttaa tätä listaa testataksesi eri syötteitä
    karsittu_lista = poista_parittomat(alkuperainen_lista)

    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Karsittu lista (parilliset luvut):", karsittu_lista)


if __name__ == "__main__":
    main()
