def missing_number(n, arr):
    acc1 = 0 # se crea una variable que almacenará la suma de los elementos de la lista arr
    acc2 = 0 # se crea una variable que almacenará la suma de los números del 1 al n
# se utiliza un ciclo for para sumar los elementos de la lista arr
    for i in arr:
        acc1 += i # se suma el valor de i a la variable acc1
# se utiliza un ciclo for para sumar los números del 1 al n
    for j in range(1, n + 1):
        acc2 += j # se suma el valor de j a la variable acc2
# se calcula la diferencia entre acc2 y acc1
    result = acc2 - acc1 
# se imprime y retorna el resultado
    print(result) 
    return result

# assert missing_number(5, [1, 2, 3, 5]) == 4, "Error en el caso de prueba"

missing_number(5, [1, 2, 3, 5])

