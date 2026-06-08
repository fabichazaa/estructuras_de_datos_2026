class ColaFija:
    def __init__(self, capacidad):
        if capacidad < 0:
            raise IndexError("Capacidad no puede ser negativa")
        
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.size = 0

    def len(self):
        return self.size
    
    def enqueue(self, x):
        if self.capacidad == self.size:
            raise Exception("Cola tiene la capacidad maxima")
        
        self.datos[self.size] = x
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Cola esta vacia")
        
        elemento = self.datos[0]

        nuevos_datos = [None] * self.capacidad

        for i in range(self.capacidad-1):
            nuevos_datos[i] = self.datos[i+1]
        
        self.datos = nuevos_datos
        self.size -= 1
    
        return elemento
    
    def first(self):
        if self.size == 0:
            raise Exception("Cola esta vacia")
        return self.datos[0]
    
    def is_empty(self):
        return self.size == 0