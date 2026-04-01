# EXERCISE 1
def ex1():
    x = 7
    y = x + 1 # y = 8
    y = y + 2 # y = 10
    z = x + 2 * y # z = 7 + 2 * 10 = 27 multiplication has priority over addition
    z = z - 1 # z = 26
    print("Final value of z is: ", z)

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

def ex2():
    x2a = 8
    print("Fun 2a needs x to be greater than 7 for y to be 1. x = ", x2a, " y = ",ex2_a(x2a))

    x2b = 4
    print("Fun 2b needs x to be greater than 3 for y to be 1. x = ", x2b, " y = ",ex2_b(x2b))

# EXERCISE 3
def ex3():
    n = 4
    m = 0
    iteration = 0
    while n > 0:
        m = m + 2
        n = n - 1
        iteration += 1
        print(f"Iteration n{iteration} | m = {m} , n = {n}\n")

# EXERCISE 4
def switch_variables():
    a = int(input("Insert value for a: "))
    b = int(input("Insert value for b: "))

    old_a = a
    a = b
    b = old_a

    print("Variable a now is: ", a)
    print("Variable b now is: ", b)

# EXERCISE 5
def positive_or_negative(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        return a*b
    
# EXERCISE 6
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# EXERCISE 7
def quantity_of_appearences(n, list):
    counter = 0

    for i in range(len(list)):
        if n == list[i]:
            counter += 1

    return counter

# EXERCISE 8
def add_max_and_min(list):
    if len(list) < 2:
        return "The list needs at least 2 elements."
    
    max = list[0]
    min = list[0]

    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    
    return f"Max is {max}\nMin is {min}\nAddition is: {max+min}"

# EXERCISE 9
def add_elements(list):
    length = len(list)
    if not (length > 2 and length%2 != 0):
        return "List not valid."
    print(f"Start value: {list[0]}\nMiddle value: {list[int(length/2)]}\nLast value: {list[length-1]}")
    return list[0] + list[int(length/2)] + list[length-1]      

# EXERCISE 10
def add_odd_squares(n):
    addition = 0
    for i in range(1,n):
        if i%2 != 0:
            addition += i**2
    return addition

# EXERCISE 11
def are_there_more_positives(list):
    positive_count = 0
    negative_count = 0

    for i in range(len(list)):
        if list[i] > 0:
            positive_count += 1
        else:
            negative_count += 1
    
    return positive_count > negative_count

# EXERCISE 12
def vowel_quantity(string):
    vowels = ["a", "e", "i", "o","u"]
    vowel_count = 0

    for i in range(len(string)):
        if string[i].lower() in vowels:
            vowel_count += 1

    return vowel_count

# EXERCISE 13
def are_all_equal(list):
    length = len(list)

    if length <= 1:
        return True
    
    current = list[0]

    for i in range(1, len(list)):
        if current == list[i]:
            current = list[i]
        else:
            return False
        
    return True

def does_odd_product_exist(list):
    length = len(list)
    for i in range(length-1):
        for j in range(i+1, length):
            print(f"i value: {list[i]}\nj value: {list[j]}\nproduct: {list[i]*list[j]}")
            print("--------------------------------------")
            product = list[i] * list[j]
            if product % 2 != 0:
                return True
    return False

# EXECUTION SECTION
print(does_odd_product_exist([0,2,3,4,2]))