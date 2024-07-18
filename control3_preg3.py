def potencia(num, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return num * potencia(num, exp - 1)
    else:
        return 1 / potencia(num, -exp)

print(potencia(2, 9))
print(potencia(5, 7))
print(potencia(7, 4))