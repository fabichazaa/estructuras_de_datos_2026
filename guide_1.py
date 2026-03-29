# EXERCISE 1
x = 7
y = x + 1 # y = 8
y = y + 2 # y = 10
z = x + 2 * y # z = 7 + 2 * 10 = 27 multiplication has priority over addition
z = z - 1 # z = 26
print("Final value of z is", z)

# EXERCISE 2
def ex2_a(x):
    if x > 7:
        y = 1
    else:
        y = 0
    return y

def ex2_b(x):
    if x <= 3:
        y = 0
    else:
        y = 1
    return y

x2a = 8
print("Fun 2a needs x to be greater than 7 for y to be 1. x = ", x2a, " y = ",ex2_a(x2a))

x2b = 4
print("Fun 2b needs x to be greater than 3 for y to be 1. x = ", x2b, " y = ",ex2_b(x2b))