#ohjelma hemoglobiini arviointiin

# kysytään käyttäjältä lähtö arvot
sukup = input("Oletko nainen vai mies (N/M)? ")
hgb = int(input("Syötä hemoglobiini arvosi g/l: "))

#jaetaan tarkastelu erikseen naisiin ja miehiin
if sukup == "N" or "n":
    if 117 <= hgb < 175:
        print("Hemoglobiinisi on normaalilla tasolla")
    elif hgb > 175:
        print("Hemoglobiinisi on liian korkea")
    else:
        print("Hemoglobiinisi on liian alhainen")

elif sukup == "M" or "m":
    if 134 <= hgb < 195:
        print("Hemoglobiinisi on normaalilla tasolla")
    elif hgb > 195:
        print("Hemoglobiinisi on liian korkea")
    else:
        print("Hemoglobiinision on liian alhainen")
else:
    print("Tätä sukupuolta ei ole järjestelmässä. Valitse N (nainen) tai M (mies)")
