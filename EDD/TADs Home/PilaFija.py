class PilaFija:
    def __init__(self, capacidad):
        if (capacidad < 0):
            raise IndexError("Cantidad no puede ser menor a 0")
        
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def len(self):
        return self.size
    
    def push(self, x):
        if self.size == self.capacidad:
            raise IndexError("Pila en capacidad maxima")

        self.datos[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Pila vacia")
        
        elemento = self.datos[self.size-1]
        self.datos[self.size-1] = None
        self.size -= 1
        return elemento
    
    def top(self):
        if self.size == 0:
            raise Exception("Pila vacia")
        
        return self.datos[self.size-1]
