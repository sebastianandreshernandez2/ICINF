altura = 0
sumalturas = 0
cont = 0 

while altura >=0:
    altura = float(input("ingrese altura de las personas: "))
    if altura == 0:
        break
    sumalturas= sumalturas + altura
    cont = cont + 1

promedio = sumalturas / cont
print("el promedio de las estaturas ingresadas es de:", promedio)