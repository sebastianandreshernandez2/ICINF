deudo = {}

print("Ingrese el RUT y la deuda de 5 usuarios:")
for _ in range(5):
    rut = input("Ingrese el RUT: ")
    deuda = int(input("Ingrese la deuda: "))
    deudo[rut] = deuda

print("Ingrese el RUT de la persona y el monto del abono. Para finalizar, presione Enter.")
while True:
    rut = input("Ingrese el RUT de la persona: ")
    if rut == "":
        break
    if rut in deudo:
        abono = int(input("Ingrese el monto del abono: "))
        deudo[rut] -= abono
        if deudo[rut] <= 0:
            del deudo[rut]
    else:
        print("El RUT ingresado no está en la lista de deudores.")

print("Personas que quedaron deudoras y sus respectivos saldos de deuda:")
for rut, deuda in deudo.items():
    print("RUT: " + rut + ", Deuda: " + str(deuda))