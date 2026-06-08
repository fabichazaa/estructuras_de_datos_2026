class Secuencia:
    def __init__(self):
        self.datos = [] # array vacio
        self.size = 0
    
    def len(self): # O(1)
        return self.size
    
    def get_at(self, i): # O(1)
        self.validar_indice()
        return self.datos[i]
    
    def set_at(self, i, x): # O(1)
        self.validar_indice()
        self.datos[i] = x

    def insert_at(self, i, x):
        self.validar_indice()

        nuevos_datos = [None] * (self.size + 1)

        # Copio datos del 0 al i-1
        for j in range(i):
            nuevos_datos[j] = self.data[j]
        
        nuevos_datos[i] = x

        # Voy de i a n pero +1, ya que arrastro todo una posicion a la derecha
        for k in range(i, self.size):
            nuevos_datos [k+1] = self.data[k]
        
        self.datos = nuevos_datos
        self.size += 1

    def remove_at(self, i):
        self.validar_indice()

        dato_removido = self.datos[i]
        nuevos_datos = [None] * (self.size - 1)

        for j in range(i):
            nuevos_datos[j] = self.datos[j]

        # copio posiciones de i+1 hasta el final, desplazo 1 hacia la derecha
        # i lo ignoro
        for k in range(i+1, self.size):
            nuevos_datos[k-1] = self.datos[k]

        self.datos = nuevos_datos
        self.datos -= 1

        return dato_removido
    
    def insert_first(self, x):
        self.insert_at(0, x)
    
    def delete_first(self, x):
        return self.remove_at(0, x)

    def insert_last(self, x):
        self.insert_at(self.size, x)

    def remove_last(self, x):
        return self.insert_at(self.size-1, x)

    def validar_indice(self, i):
        if i < 0 or i > self.size:
            return IndexError("Index out of bounds")
    
