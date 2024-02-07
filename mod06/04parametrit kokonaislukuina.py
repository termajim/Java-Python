# Parametrit kokonaislukuina ohjelma

def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

def main():
    testilista = [1, 2, 3, 4, 5]
    summa = laske_summa(testilista)
    print("Listan summa on:", summa)

if __name__ == "__main__":
    main()
