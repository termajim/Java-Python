#Kuhan pituus ohjelma

kuhap = float(input("Kerro kuhan pituus senttimetreinä, kiitos: "))
alamittainenp = 37

if kuhap < alamittainenp:
    puuttuvatcm = alamittainenp - kuhap
    print(f"Kuha on liian lyhyt. Kuhan pitäisi olla: {puuttuvatcm}cm pidempi.")
else:
    print("Kuhan voi ottaa.")
