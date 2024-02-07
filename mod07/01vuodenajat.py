# Kysyy käyttäjän kuukauden numeron, jonka jälkeen
# tulostaa sitä vastaavan vuodenajan

def main():
    try:
        kuukausi = int(input("Anna kuukauden numero 1-12: "))
        if kuukausi < 1 or kuukausi > 12:
            print("Virhe kuukauden numeron tulee olla välillä 1-12.")
        else:
            if kuukausi == 12 or kuukausi < 3:
                print("Talvi")
            elif kuukausi < 6:
                print("Kevät")
            elif kuukausi < 9:
                print("Kesä")
            else:
                print("Syksy")
    except ValueError:
        print("Virhe: Syötteen tulee olla kokonaisluku.")

if __name__ == "__main__":
    main()
