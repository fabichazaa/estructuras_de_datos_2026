# EJERCICIO 1
#INV(i) = contador va a almacenar la cantidad de apariciones del valor buscado dentro de los i primeros elementos
def cantidad_pares_menores(lista: list[int], valor: int):
    contador = 0
    for x in lista:
        if x % 2 == 0 and x < valor:
            contador += 1
    return contador

#INV(i) = valor_mas_repetido va a almacenar el valor mas repetido dentro de los i primeros elementos
def mas_repetido(lista: list[int]):
    valor_mas_repetido = lista[0]
    repeticiones = contador(lista, valor_mas_repetido)
    for x in lista[1:]:
        repeticiones_de_x = contador(lista, x)
        if repeticiones_de_x > repeticiones:
            repeticiones = repeticiones_de_x
            valor_mas_repetido = x
    return valor_mas_repetido

def contador(lista: list[int], elemento: int):
    apariciones = 0
    for x in lista:
        if x == elemento:
            apariciones += 1
    return apariciones

#INV(i) = lsita_intercalada va a contener los primeros i elementos de las listas A y B de manera intercalada
def intercalar(listaA: list[int], listaB: list[int]):
    lista_intercalada = []
    for i in range(len(listaA)):
        lista_intercalada = lista_intercalada + [listaA[i]] + [listaB[i]]
    return lista_intercalada

# EJERCICIO 2
# Caso base: si la lista esta vacia, devuelve False. Esto ocurre si la entrada es una lista vacia o si no se encontro ningun numero negativo
# Caso recursivo: se delega la busqueda del numero negativo en el resto de la lista (no incluye el primer elemento, porque ya fue evaluado)
def hay_negativos(lista: list[int]):
    if lista == []:
        return False
    elif lista[0] < 0:
        return True
    else: hay_negativos(lista[1:])

# Caso base: si la lista esta vacia, devuelve 0. No hay elementos para sumar
# Caso recursivo 1: si el elemento en la primera posicion de la lista es mayor al valor, se devuelve la suma entre ese elemento y se delega la suma de mayores del resto de la lista
# Caso recursivo 2: si el elemento no es mayor, se delega la suma de mayores al resto de la lista, sin incluir el primer elemento
def suma_mayores(lista: list[int], valor: int):
    if lista == []:
        return 0
    elif lista[0] > valor:
        return lista[0] + suma_mayores(lista[1:], valor)
    else:
        return suma_mayores(lista[1:], valor)
    
# EJERCICIO 3 - DIBUJO

# EJERCICIO 4
def practica_listas():
    lista_1 = [3 , 2, 1]
    lista_2 = [1 , 2, 3]
    lista_2 = lista_1 #lista 2 hace referencia a [3,2,1]
    lista_1 [0] = 0 #lista 1 se modifica a [0,2,1] afecta tanto a lista 1 como lista 2
    lista_3 = lista_2 # lista 3 hace referencia a lista 2, la cual hace referencia a lista 1
    lista_3 [1] = 5 # se modifica lista 1 en la posicion 1, queda [0,5,1]
    lista_3 = [1 , 2, 3] # se limpia la referencia, ahora lista 3 refiere a una nueva lista
    # lista 1 y 2 quedan [0,5,1]
    #lista 3 queda [1,2,3]
    print(lista_1)
    print(lista_2)
    print(lista_3)

# EJERCICIO 5 - DIBUJO

# EJERCICIO 6 - DIBUJO
#print(mas_repetido([1,2,1,1,1,3,4,5,6,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4]))

print(practica_listas())