# INVARIANTS
# EXERCISE 1
def exercise_1():
    product = 1
    for i in range(1,11):
        product = product * i 

# a. INV(i) = Producto es la multiplicación de todos los i números enteros
# b. Producto representa el factorial de i

def exercise_2():
    lista = [1,2,3,4]
    contador = 0
    for x in lista :
        if x > 0:
            contador += 1

# a. Contador cuenta los números positivos
# b. En cada iteración, contador almacena la cantidad de los números positivos
# dentro de los elementos recorridos hasta el momento
# INV(i) = Contador es la cantidad de números positivos dentro de los
# primeros i elementos recorridos

# EXERCISE 3
def fibonacci ( n : int ):
    if n == 1: return 0
    if n == 2: return 1
    anteultimo = 0
    ultimo = 1
    for i in range (3 , n + 1):
        siguiente = anteultimo + ultimo
        anteultimo = ultimo
        ultimo = siguiente
        return ultimo
    
# Invariante anteultimo
# INV(i) = anteultimo es la sumatoria de los i-1 términos de la secuencia fibonacci
# Invariante último
# INV(i) = ultimo es la sumatoria de los i términos de la secuencia fibonacci

# EXERCISES WHERE ANSWERED ON NOTEPAD

# EXERCISE 8
def ex_8(lista: list[int]):
	promedio = sum(lista)/len(lista)
	contador = 0
     
	for elem in list:
		if elem > promedio:
			contador = contador + 1
# EXERCISE 9
def ex_9(lista: list[int]):
    if(len(lista) < 2):
        print("Invalid list")
        return
    
    contador = 0
    anterior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > anterior:
              contador += 1
        anterior = lista[i]
    return contador

# EXERCISE 10
def ex_10(lista: list[int]):
     actual = lista[0]
     maxRepeticionesPrevias = 1
     repeticiones= 1
     for i in range(1, len(lista)):
          if actual == lista[i]:
               repeticiones += 1
          else:
               if maxRepeticionesPrevias < repeticiones:
                maxRepeticionesPrevias = repeticiones

                actual = lista[i]
                repeticiones = 1

     if maxRepeticionesPrevias < repeticiones:
        return repeticiones
     else: return maxRepeticionesPrevias

def ex_10_improved(list):
     if not list:
          return "List not valid"
     
     maxRepeticiones = 0
     repeticionesActuales = 0

     for i in range(1, len(list)):
          if list[i] == list[i-1]:
               repeticionesActuales += 1
          else:
                repeticionesActuales = 1
        
          if maxRepeticiones < repeticionesActuales:
               maxRepeticiones = repeticionesActuales
    
     return maxRepeticiones