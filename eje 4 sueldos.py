
empleados_bajo = empleados_alto = gasto_general = 0

print("Ingrese los sueldos de los empleados mensualmente. Para terminar, ingrese -1.")

sueldo = int(input("ingrese el sueldo de los empleados : "))
while sueldo != -1:
    if sueldo <= 900000:
       empleados_bajo+=1
    else:
       empleados_alto+=1
    gasto_general += sueldo
    sueldo = int(input("ingrese el sueldo de los empleados : "))

print("la cantidad de empleados que cobran hasta $900.000 es de : " + str(empleados_bajo))
print("la cantidad de empleados que cobran mas de $900.000 es de : " + str(empleados_alto))
print("gasto total en sueldos: $" + str(gasto_general))