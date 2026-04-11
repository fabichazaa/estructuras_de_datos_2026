# IN CLASS - RECURSIVE
def sum(n):
    if n == 1:
        return 1

    return n + sum(n-1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# ESTA MAL si no uso el else?
# ESTA MAL si no defino el tipo de variable de entrada/salida??
def multiplicar(n, m):
    if m == 1:
        return n
    return n + multiplicar(n, m-1)

# position 1 is n = 0
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# EXECUTION ZONE
print(fibonacci(1))