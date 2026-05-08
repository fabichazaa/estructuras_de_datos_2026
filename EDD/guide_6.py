def linearSearch(list: list[int], elem: int):
    for x in list:
        if x == elem:
            return True
    return False

# Precondition: list needs to be sorted
def binarySearch(list: list[int], elem: int):
    i = 0
    n = len(list)-1
    while(i <= n):
        middle = (n+i) // 2
        print(f"Start {i} | Middle {middle} | End {n}")
        
        if(list[middle] == elem):
            return True
        elif(list[middle] > elem):
            print("Element is smaller than middle")
            n = middle - 1
            print(f"New end: {n}")
        else:
            i = middle + 1
            print("Element is greater than middle")
            print(f"New start: {i}")

    return False

def insertionSort(list: list[int]):
    n = len(list)
    for i in range(1, n):
        for j in range(0, i):
            if list[i] > list[j]:
                list[j] = list[i]

# INSERTION SORT
# Starts at the second element of the list, and compares it with the previous elements
# If it is smaller than the previous element, it swaps them, 
# and continues to compare it with the next previous element until it finds the correct position for it.
def insertion_sort(lista: list[int]):
    for i in range(1, len(lista)):
        print(f"i: {i} | lista: {lista}")
        j = i
        print(f"j: {j} | lista[j]: {lista[j]} | lista[j-1]: {lista[j-1]}")
        # if the neareast element is greater than the current element, we need to swap them
        # if the nearest element is smaller than the current element, we need to stop, because the list is already sorted until that point
        while j > 0 and lista[j] < lista[j-1]:
            print(f"Swapping {lista[j]} and {lista[j-1]}")
            swap(lista, j, j-1)
            j = j - 1


# SELECTION SORT
# Starts at the first element of the list, and finds the smallest element in the list, 
# and swaps it with the first element.
def selection_sort(lista: list[int]):
    print(f"Estado inicial: {lista}\n" + "-"*30)
    
    for i in range(len(lista)):
        # Buscamos el índice del mínimo desde la posición 'i' hasta el final
        i_min = i
        for j in range(i, len(lista)):
            print(j)
            print(f"Comparando {lista[j]} con {lista[i_min]} (actual mínimo)")
            # Si encontramos un número menor al que creíamos que era el mínimo
            if lista[j] < lista[i_min]:
                i_min = j
        
        print(f"Iteración {i}: El valor más pequeño encontrado es {lista[i_min]} (en índice {i_min})")
        print(f"Intercambiando {lista[i]} con {lista[i_min]}")
        
        # Realizamos el intercambio (swap)
        swap(lista, i, i_min)
        
        print(f"Lista tras intercambio: {lista}")
        print("-" * 30)

# BUBBLE SORT
# Starts at the first element of the list, and compares it with the next element,
# if it is greater than the next element, it swaps them, 
# and continues to compare it with the next element until it reaches the end of the list, then it starts again from the first element until the list is sorted.
def bubble_sort(lista: list[int]):
    print(f"Estado inicial: {lista}\n" + "-"*30)
    for i in range(len(lista)-1):
        print(f"Iteración i: {i}")
        for j in range(len(lista)-1): 
            print("Iteracion j:", j) 
            print(f"Comparando {lista[j]} con {lista[j+1]}")
            if lista[j] > lista[j+1]:
                swap(lista, j, j+1)
                print(f"Intercambiando {lista[j]} con {lista[j+1]}")
            print("----"*5)
        print("--------"*5)


def swap(lista: list[int], i: int, j: int):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux



inicio = 0
fin = 7
mitad = (inicio + fin) // 2
print(selection_sort([5,4,3,2,1]))
