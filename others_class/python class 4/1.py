# se define una función sequence que recibe un número entero n y devuelve una lista con la secuencia de Collatz de n.
def sequence(n):
    # se crea una variable que es una lista con el valor de n
    answer = [n]
    # se utiliza un ciclo while que se ejecuta mientras n sea diferente de 1
    while n != 1:
        # si n es par, se divide entre 2
        if n % 2 == 0:
            n //= 2
        else:
            # si n es impar, se multiplica por 3 y se suma 1
            n = 3 * n + 1
        # se agrega el valor de n a la lista
        answer.append(n)
    # se imprime y retorna la respuesta
    print(answer)
    return answer

# se llama a la función con el valor de n, en este caso 3
sequence(3)

# assert sequence(3) == [ 3, 10, 5, 16, 8, 4, 2, 1 ]
