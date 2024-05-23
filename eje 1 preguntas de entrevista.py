preguntas = int (input("¿cuantas preguntas se hicieron? "))
correctas = int (input("¿cuantas fueron las respuestas correctas? "))
porcentaje = correctas / preguntas * 100

print("el porcentaje es de: ", porcentaje)

if porcentaje >= 95:
    print ("el conocimiento es de nivel maximo")
else:
    if porcentaje >= 70:
          print ("el conocimiento es de nivel medio")
    else:
         if porcentaje >= 40:
              print("el conocimiento es de nivel regular")
         else:
              print("el conocimiento es de nivel insuficiente")