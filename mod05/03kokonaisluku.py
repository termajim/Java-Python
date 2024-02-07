# Kokonaisluvut ilmoittaa onko alkuluku

def onko_alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            return False
    return True

def main():
    while True:
        try:
            luku = int(input("Syötä kokonaisluku (lopeta syöttämällä kirjoittamalla 'exit'): "))
            if luku < 0:
                print("Negatiivinen luku ei voi olla alkuluku.")
            elif onko_alkuluku(luku):
                print(f"{luku} on alkuluku.")
            else:
                print(f"{luku} ei ole alkuluku.")
        except ValueError:
            print("Virheellinen syöte. Syötä kokonaisluku tai 'exit' lopettaaksesi.")
            continue
        else:
            break

if __name__ == "__main__":
    main()
