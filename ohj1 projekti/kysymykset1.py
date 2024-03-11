# Testausta kysymyksistä ja niiden liitteistä

def odota_lentoa():
    print("Saavuit portille, jossa odotat lentoasi Latviaan vielä pari tuntia.")
    print("Tunnet, että sinulla on nälkä, ja mietit, olisiko pitänyt syödä jotain.")
    print("Viereinen matkustaja tarjoaa sinulle voileivän.")

    while True:
        print("\nValintasi:")
        print("A") Otan voileivän vastaan ja kiitän.")
        print("B") Otan voileivän.")
        print("C") Kieltäydyn voileivästä. Ei tuntemattomiin kannata luottaa.")

        valinta = input("Valitse vaihtoehto (A/B/C): ")

        if valinta == "A".lower():
            print("Valitsit ottaa voileivän vastaan ja kiität.")
            print("Jatkat portille odottamaan lentoa.")
            break
        elif valinta == "B".lower():
            print("Valitsit ottaa voileivän.")
            print("Jatkat matkaa portille.")
            break
        elif valinta == "C".lower():
            print("Valitsit kieltäytyä voileivästä.")
            print("Menet lentoportille ja odotat lentoa.")
            break
        else:
            print("Virheellinen valinta. Valitse vaihtoehto A, B tai C.")

odota_lentoa()
