def number_spiral(x, y):                # se define una función number_spiral que recibe dos números enteros x y y
    if x == y:                          # si x es igual a y, se retorna x al cuadrado menos x más 1
        return x ** 2 - x + 1           # se retorna x al cuadrado menos x más 1
    elif x > y:                         # si x es mayor que y
        if x % 2 == 0:                  # si x es par...
            return x ** 2 - y + 1       # se retorna x al cuadrado menos y más 1
        else:                           # si x es impar...
            return (x - 1) ** 2 + y     # se retorna x menos 1 al cuadrado más y
    else:                               # si x es menor que y
        if y % 2 == 0:                  # si y es par...
            return (y - 1) ** 2 + x     # se retorna y menos 1 al cuadrado más x
        else:                           # si y es impar...
            return y ** 2 - x + 1       # se retorna y al cuadrado menos x más 1
    
print(number_spiral(2, 2))

# assert number_spiral(2, 2) == 3, "Error en el caso de prueba"

