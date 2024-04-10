# Una función que dada una lista "n" quite todos los valores repetidos de dicha lista
# y retorne otra lista sin los valores repetidos.

# Una función que, dada una lista "n", ordene los valores distintos que hay
# y cuántos hay de cada uno.
# El retorno debe ser un valor que sea útil para su empleabilidad posteriormente.

lista = [5, 2, 2, 2, 3, 2, 5]

# mi_lista = list(set(lista))
# print("lista de números sin repetidos: ", mi_lista)

# print("números sin repetir y cantidad de veces que se repite:")
# for i in mi_lista:
#     print(i, ":", lista.count(i))


def clean_list(lista):
    a = list(set(lista))
    return a
clean_list(lista)
print(clean_list(lista))


def count_list(lista):
    b = {i: lista.count(i) for i in lista}
    return b
count_list(lista)
print(count_list(lista))

# Una función que, dada una lista "n", ordene los valores distintos que hay
# y cuántos hay de cada uno.
# El retorno debe ser un valor que sea útil para su empleabilidad posteriormente.


def contar_ocurrencias(lista):
    ocurrencias = {}
    for i in lista:
        if i in ocurrencias:
            ocurrencias[i] += 1
        else:
            ocurrencias[i] = 1
    # lista_ordenada = sorted(ocurrencias.items())
    lista_ordenada = sorted(f"{clave}: {valor}" for clave, valor in ocurrencias.items())
    return lista_ordenada
print(contar_ocurrencias(lista))