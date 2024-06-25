numeros = []

for i in range(10):
    numero = int(input("Ingrese 10 numeros: "))
    numeros.append(numero)
numeros.reverse()

print("el orden inverso de los numeros es:")
for numero in numeros:
    print(numero)