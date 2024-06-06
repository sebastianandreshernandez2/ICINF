ptjes = []

for dia in range(1, 16):
    puntaje = int(input("Ingrese el puntaje del día:"))
    ptjes.append(puntaje)

print("Días con puntaje menor a 70:")
dia = 1
for puntaje in ptjes:
    if puntaje <= 70:
        print("Día", dia)
    dia += 1

print("Días con puntaje mayor a 70:")
dia = 1
for puntaje in ptjes:
    if puntaje > 70:
        print("Día", dia)
    dia += 1