# IN CLASS - RECURSIVE LISTS
listFabi = [1,2,3,4,5,6]
def list_operations_review():
    myList = [1,2,3,4,5,6,7,8]

    # SLICING
    print("~ Last element with known index | list[7]: ", myList[7])
    print("~ Last element without known index | list[-1]]: ", myList[-1])
    # getting [i:j] is inclusive for i, exclusive for j
    print("~ List range [1:4] goes from index 1 to index 3 :", myList[1:4])
    print("~ List range [:4] goes from index 0 to index 3 :", myList[:4])
    # if the list has no more elements when trying to get an index out of range,
    #  an empty list is returned
    print("~ List range [60:] goes from index 0 to index 3 :", myList[60:])

def myLength(list):
    if list == []:
        return 0
    return 1 + myLength(list[1:])

def countElement(list, elem):
    if list == []:
        return 0

    if list[0] == elem:
        return 1 + countElement(list[1:], elem)
    else:
        return countElement(list[1:], elem)

def isInList(list, elem):
    if list == []:
        return False
    
    if list[0] == elem:
        return True
    else:
        return isInList(list[1:], elem)

def maxElement(list):
    if len(list) == 1:
        return list[0]
    else:
        maxDelegated = maxElement(list[1:])
        if list[0] > maxDelegated:
            return list[0]
        else:
            return maxDelegated

# ⋆ GUIDE 4 ⋆
# EXERCISE 1
# Needs base case of empty list, dont fall in first index
def sumList(list: list[int]):
    if list == []:
        return 0
    return list[0] + sumList(list[1:])

# EXERCISE 2
def isInList(list: list[int], elem: int):
    if list == []:
        return False

    if list[0] == elem:
        return True
    else:
        return isInList(list[1:], elem)

# EXERCISE 3
# Precondition: List is not empty
def lastElement(list: list[int]):
    if len(list) == 1:
        return list[0]
    return lastElement(list[1:])

# EXERCISE 4
def quantityOfEvens(list: list[int]):
    if list == []:
        return 0
    
    if list[0] % 2 == 0:
        return 1 + quantityOfEvens(list[1:])
    else:
        return quantityOfEvens(list[1:])

# EXERCISE 5
def greaterThanElement(list: list[int], n: int):
    if list == []:
        return []
    
    if list[0] > n:
        return [list[0]] + greaterThanElement(list[1:], n)
    else:
        return greaterThanElement(list[1:], n)

# EXERCISE 6
def smallerList(list: list[int], threshold: int):
    if list == []:
        return []
    
    if list[0] > threshold:
        return [threshold] + smallerList(list[1:], threshold)
    else:
        return [list[0]] + smallerList(list[1:], threshold)
    
# EXERCISE 7
def removeElement(list: list[int], n: int):
    if list == []:
        return []
    
    if list[0] == n:
        return list[1:]
    else:
        return [list[0]] + removeElement(list[1:], n)

# EXERCISE 8
def duplicateElements(list: list[int]):
    if list == []:
        return []
    
    return [list[0]]*2 + duplicateElements(list[1:])

# EXERCISE 9
def areAllEqual(list: list[int]):
    if len(list) < 2:
        return True
    
    if list[0] == list[1]:
        return areAllEqual(list[1:])
    else:
        return False

# EXERCISE 10
# When concatanating lists, dont forget the braces!!! If not the element wont be considered a list!!
# Precondition: Both lists have same length
def intercalateLists(list1: list[int], list2: list[int]):
    if list1 == []:
        return []
    return [list1[0]] + [list2[0]] + intercalateLists(list1[1:], list2[1:])

# EXERCISE 11
#[1:-1] goes from second element inclusive, to the last one exclusive
def isPalindrome(list: list[int]):
    if len(list) < 2:
        return True
    
    if list[0] == list[-1]:
        return isPalindrome(list[1:-1])
    else:
        return False

# EXERCISE 12
def areRepeated(list: list[int]):
    if len(list) < 2:
        return False
    
    if list[0] in list[1:]:
        return True
    else:
        return areRepeated(list[1:])
    
# EXERCISE 13
def reOrganizedList(list: list[int]):
    if list == []:
        return []
    
    if list[0]%2 == 0:
        return [list[0]] + reOrganizedList(list[1:])
    else:
        return reOrganizedList(list[1:]) + [list[0]]

# EXERCISE 14
# Precondition: Both lists have same length
def newListWithMax(list1: list[int], list2: list[int]):
    if list1 == []:
        return []
    
    if list1[0] > list2[0]:
        return [list1[0]] + newListWithMax(list1[1:], list2[1:])
    else:
        return [list2[0]] + newListWithMax(list1[1:], list2[1:])
print(newListWithMax([2, 4, 1], [6, 2, 0]))