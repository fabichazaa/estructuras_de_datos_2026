# Modelo I
# EJ 1
def hay_mas_positivos(lista: list[int]):
    contador_positivos = 0
    contador_negativos = 0
    for elem in lista:
        if elem > 0:
            contador_positivos += 1
        else:
            contador_negativos += 1
    return contador_positivos > contador_negativos

# EJ 2
# Serie: 0, 1, 1, 2, 3, 5, 8, 13...
def fibonacci(n):
    if n <= 1:
        return n
    
    ultimo = 1
    anteultimo = 0
    while n > 1:
        ultimo_provisorio = ultimo + anteultimo
        anteultimo = ultimo
        ultimo = ultimo_provisorio
        n = n - 1
    return ultimo

# EJ 4
def lista_acotada(lista: list[int], umbral):
    if lista == []:
        return []
    if lista[0] > umbral: 
        return [umbral] + lista_acotada(lista[1:], umbral)
    else:
        return [lista[0]] + lista_acotada(lista[1:], umbral)

# EJ 5
# Precondition: list has one element! There is no minimum if it is empty
def minimo(lista: list[int]):
    length = len(lista)
    if length == 1:
        return lista[0]
    else:
        minimo_del_resto = minimo(lista[1:])
        if minimo_del_resto < lista[0]:
            return minimo_del_resto
        else:
            return lista[0]


# Modelo IV
# EJ 1
def lista_referencias():
    lista_a = [1,2,3]
    lista_b = lista_a
    lista_a = lista_a + [4]
    print("Lista a: ", lista_a)
    print("Lista b: ", lista_b)

def misterio(s):
    s[0] = s[0] * 2
    s = s[1:3]
    s.append(99)
    print(f"s: {s}")

def slicing_tests():
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lista[2:8:3])
    print(lista[5:1:-1])
    print(lista[7:2])
    print(lista[-3:])
    print(lista[1:-1])

# PRECONDICION: la lista tiene longitud par
def suma_extremos(lista: list[int]):
    if lista == []:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + lista[-1] + suma_extremos(lista[1:-1])

# datos = [10, 20, 30, 40]
# misterio(datos)
# print(f"datos: {datos}")


# Cuestionario I
def ejercicio_1():
    x = [1, 2]
    y = x
    x = x + [3]
    y.append(4)
    print(f"y: {y}")
    print(f"x: {x}")


ejercicio_1()


def verificar_elementos(lista_a, lista_b):
    # lista_a tiene n elementos
    # lista_b tiene n elementos y está ordenada
    
    for elemento in lista_a:
        encontrado = busqueda_binaria(lista_b, elemento)
        if encontrado:
            print(f"{elemento} está en la lista B")

def busqueda_binaria(lista_b, elemento):
    return "boop"