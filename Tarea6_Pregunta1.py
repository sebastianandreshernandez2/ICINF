def contar_vocales_consonantes(palabra):
    vocales = "aeiouAEIOU"
    cant_vocales = 0
    cant_consonantes = 0
    
    for letra in palabra:
        if letra.isalpha():  # Verifica si el carácter es una letra
            if letra in vocales:
                cant_vocales += 1
            else:
                cant_consonantes += 1
                
    return cant_vocales, cant_consonantes

def main():
    palabras = []
    while True:
        palabra = input("Ingresa palabra(s) (o presiona enter para finalizar la ejecucion): ")
        if palabra == "":
            break
        palabras.append(palabra)
    
    for palabra in palabras:
        vocales, consonantes = contar_vocales_consonantes(palabra)
        print(f"Palabra: {palabra}, Vocales: {vocales}, Consonantes: {consonantes}")

if __name__ == "__main__":
    main()