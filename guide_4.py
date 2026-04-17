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
    
print(maxElement([3,1,2,3,4,5,1]))