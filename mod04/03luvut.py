# luvut ohjelma
luvut = []
while True:
    syota = input("Anna luku (Paina ENTER lopettaa toiminnon): ")
    if not syota:
        break
    try:
        luku = float(syota)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen luku: Anna luku uudelleen: ")

# Tulostetaan pienin ja suurin luku
if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")
