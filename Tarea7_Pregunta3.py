supermercado = {}

while True:
    prodc = input("Ingresa la palabra (presione Enter para finalizar): ")
    if prodc == "":
        break
    cantidad = int(input(f"Ingrese la cantidad del {prodc}: "))
    supermercado[prodc] = cantidad

x = int(input("Ingrese un valor numérico X para multiplicar las cantidades: "))

print("Productos y sus cantidades multiplicadas por X:")
for prodc, cantidad in supermercado.items():
    print(prodc,":", cantidad * x)