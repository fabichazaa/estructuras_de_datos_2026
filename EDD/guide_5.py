def sumaDobles(a, b):
    doble_a = 2 * a # 2OE
    doble_b = 2 * b # 2OE
    return doble_a * doble_b # 2OE
# T(a, b) = 6 Operaciones Elementales. 
# La cantidad de operaciones que hace es constante

def sumatoria(n: int):
    res = 0             # 1 OE
    i = 1               # 1 OE
    while i <= n:       # 1 OE | ---> + 1OE del ultimo while
        res = res + i   # 2 OE | ---> * n
        i = i + 1       # 2 OE |
    return res          # 1 OE

# T(n): 2 OE + 5 OE*(n) + 1 OE + 1 OE = 5n + 4 ===> ORDEN N ===> O(n)

def dobleProducto(n: int):
    res = 1                     # 1 OE
    i = 1                       # 1 OE
    while i <= n:               # 1 OE | + 1 OE ultima evaluacion del while
        j = 1                   # 1 OE |
        while j <= n:           # 1 OE |      | + 1 OE ultima evaluacion
            res = res * i * j   # 2 OE | * n  |  * n
            j = j + 1           # 2 OE |      |
        i = i + 1               # 2 OE |
    return res

# T(n) = 2 + 1 + n*(3 + n*(5)+1) + 1 = 4 + n*(5n + 4) = 4 +5n^2 +4n 