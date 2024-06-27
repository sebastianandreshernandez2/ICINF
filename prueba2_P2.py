usd=[]
clp=950

for prodc in range (10):
    prodc=float (input("ingrese 10 precios de productos en dolares: "))
    usd.append(prodc)

cambio=[prodc*clp for prodc in usd]
print ("el cambio a pesos chilenos es de :",cambio)