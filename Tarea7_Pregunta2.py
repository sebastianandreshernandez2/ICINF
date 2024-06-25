palabras = []

while True:
    pal = input("Ingresa una palabra (presione Enter para finalizar): ")
    if pal == "":
        break
    palabras.append(pal)

def contar_a(pal):
    return pal.count('A') + pal.count('a')

print("Conteo de letras 'A' y 'a' en las palabras:")
for pal in palabras:
    cantidad_a = contar_a(pal)
    print("La palabra ",pal, "tiene", cantidad_a, "letras 'A' o 'a'.")