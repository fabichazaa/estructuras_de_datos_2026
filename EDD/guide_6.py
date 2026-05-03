def linearSearch(list: list[int], elem: int):
    for x in list:
        if x == elem:
            return True
    return False

# Precondition: list needs to be sorted
def binarySearch(list: list[int], elem: int):
    i = 0
    n = len(list)-1
    while(i < n):
        middle = int(n/2)
        print(f"Start {i} | Middle {middle} | End {n}")
        if(list[middle] == elem):
            return True
        elif(list[middle] > elem):
            n = middle
        else:
            i = middle

def insertionSort(list: list[int]):
    n = len(list)
    for i in range(1, n):
        for j in range(0, i):
            if list[i] > list[j]:
                list[j] = list[i]

        
# INV(i) = el objetivo no esta en los primeros i valores de la lista
print(binarySearch([1,2,3,4,5,6], 1))