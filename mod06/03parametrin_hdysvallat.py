# Parametrin bensiinin määrä yhdysvaloissa ohjelma

def muunna_gallonoiksi(gallona_maara):
    return gallona_maara * 3.785

def main():
    while True:
        try:
            gallona_maara = float(input("Syötä bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))
            if gallona_maara < 0:
                print("Lopetetaan.")
                break
            litra_maara = muunna_gallonoiksi(gallona_maara)
            print(f"{gallona_maara} gallonaa on {litra_maara:.2f} litraa.")
        except ValueError:
            print("Virheellinen syöte. Syötä desimaaliluku.")

if __name__ == "__main__":
    main()
