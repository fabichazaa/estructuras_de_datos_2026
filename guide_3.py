# IN CLASS - Recursion
def sum(n):
    if n == 1:
        return 1

    return n + sum(n-1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# If the else of an if-else sentence is not used in recursiveness, one should explain why
# Type of entry parameters should be specified
def multiplicar(n, m):
    if m == 1:
        return n
    return n + multiplicar(n, m-1)

# Position 1 is n = 0
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# ⋆ GUIDE 3 ⋆
# EXERCISE 1
# Precondition: n > 0
def sum(n: int):
    if n == 1: 
        return n
    return n + sum(n-1)

# EXERCISE 2
# Precondition: pos >= 0
def fibonacci(pos: int):
    if pos < 2:
        return pos
    return fibonacci(pos - 1) + fibonacci(pos - 2)

# EXERCISE 3
# Precondition: n >= 0
def is_even(n: int):
    if n == 0:
        return True
    elif n == 1:
        return False
    
    return is_even(n-2)

# EXERCISE 4
# Precondition: n >= 1
def f(n: int):
    if n == 1:
        return 5
    return 3 * f(n-1) - (2**n)

# EXERCISE 5
# Precondition: n >= 1
def g(n: int):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return (g(n-1) + g(n-2) + 3*n + 5)/2

# EXERCISE 6
# Precondition: n >= 0
def is_multiple_of_3(n):
    if n == 0:
        return True
    if n <= 2:
        return False
    return is_multiple_of_3(n-3)

# EXERCISE 7
# Precondition: 0 <= n <= 100
def sum_up_to_100_from_n(n: int):
    if n == 100:
        return 100
    return n + sum_up_to_100_from_n(n+1)

# EXERCISE 8
def h(n: int):
    if n == 1:
        return -3
    elif n == 2:
        return 6
    
    if (n % 2 == 0):
        return -(h(n-1)) - 3
    else:
        return h(n-1) + 2*(h(n-2)) + 9

# EXERCISE 11
# Precondition: n > 0
def add_evens(n: int):
    if n == 1:
        return 2
    return n*2 + add_evens(n-1)

# EXERCISE 12
# Precondition: a > 0 and b > 0
def is_divisible(a, b):
    if a == 0:
        return True
    if a < b:
        return False
    return is_divisible(a-b, b)

# EXECUTION ZONE
print(is_divisible(101,10))