dicc={}
x=0
while x<5:
    x+=1
    pais=input("ingrese un paises: ")
    capital=input("ingrese la capital del pais escrito de antemano: ")
    dicc[pais]=capital
   
turista=input("nombre del turista: ")
pais_de_prosedencia=input("pais de prosedencia del turista:")
print("el turista con el nombre: ", turista,"viene del pais",pais_de_prosedencia,"y su capital es", dicc[pais_de_prosedencia])