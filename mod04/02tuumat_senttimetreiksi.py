# Tuummat senttimetreiksi ohjelma
def tuumat_cm(tuumat):
    return tuumat * 2.54

tuumat = float(input("Kerro tuumienmäärä: "))
while tuumat >= 0:
    cm = tuumat_cm(tuumat)
    print(f"{tuumat} tuumaa on {cm} senttimetriä.")
    tuumat = float(input("Kerro tuumienmäärä: "))
print("Ohjelma lopetetaan")
