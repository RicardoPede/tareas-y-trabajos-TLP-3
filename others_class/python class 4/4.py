def palindrome_reorder(input):
    diccionary = {}
    for chararter in input:                     # se crea un diccionario con los caracteres del input y su frecuencia
        if chararter in diccionary:             # si el carácter ya está en el diccionario...
            diccionary[chararter] += 1          # se incrementa su frecuencia
        else:                                   # si el carácter no está en el diccionario...
            diccionary[chararter] = 1           # se agrega al diccionario con una frecuencia de 1

    first = []                                  # se crea una lista vacía
    middle = ""                                 # se crea una cadena de texto vacía
    for key in diccionary:                      # se utiliza un ciclo for para recorrer los elementos del diccionario
        if diccionary[key] % 2 == 0:            # si el valor de la key es par...
            first.extend([key] * (diccionary[key] // 2))  # se agrega a la lista first
        else:                                   # si el valor de la key es impar...
            if middle:                          # si ya hay un carácter en el medio...
                return "NO SOLUTION"            # se retorna "NO SOLUTION"
            middle = key                        # se asigna el carácter impar al medio
            first.extend([key] * (diccionary[key] // 2))  # se agrega la mitad de los caracteres impares a la lista first

    answer = first + list(middle) + first[::-1] # se crea la lista answer con la lista first, el carácter del medio y la lista first invertida
    return "".join(answer)                      # retorna la lista answer como una cadena de texto

print(palindrome_reorder("aabbc"))

# Caso de prueba: assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"