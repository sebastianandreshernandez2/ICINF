def solo_numeros(var):
    números=("0987654321")
    for x in var:
        if x in números:
            sn=True
        else:
            sn=False
            break
    return sn

var=input("Ingrese la variable: ")
print(solo_numeros(var))