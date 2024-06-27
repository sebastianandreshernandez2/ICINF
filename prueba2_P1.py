lista=[]
contador=0
contador_nota=0
while True:
    notas=float(input("ingrese N notas: "))
    if notas==0:
        break
    contador_nota+=notas
    lista.append(notas)
    contador+=1
    lista.sort()
print("cantidad de notas: ", len(lista))
print("promedio de notas: ",contador_nota/contador)
print("nota mas baja: ",lista[0])
print("nota mas alta: ",lista[-1])

    