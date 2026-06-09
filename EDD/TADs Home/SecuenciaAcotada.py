class SecuenciaAcotada:
    def __init__(self, capacidad):
        if capacidad < 0:
            raise Exception("La capacidad no puede ser negativa")
        
        # si capacidad es 5 va a crear [None, None, None, None, None]
        self.data = [None] * capacidad
        self.size = 0
        self.capacidad = capacidad

    def len(self): 
        return self.size
    
    def insert_at(self, i, x):
        self.validar_indice(i)

        if self.capacidad == self.size:
            raise Exception("No se pueden agregar mas elementos")
        
        nueva_data = [None] * self.capacidad
        for j in range(i):
            nueva_data[j] = self.data[j]

        nueva_data[i] = x
        
        for k in range(i, self.size):
            nueva_data[k+1] = self.data[k]

        self.data = nueva_data
        self.size += 1
    
    def delete_at(self, i):
        self.validar_indice(i)

        if self.capacidad == self.size:
            raise Exception("No se pueden agregar mas elementos")
        
        nueva_data = [None] * self.capacidad

        for j in range(i):
            nueva_data[j] = self.data[j]

        elemento = self.data[i]

        for k in range(i+1, self.size):
            nueva_data[k-1] = self.data[k]

        self.data = nueva_data
        self.size -=1
        return elemento

        
    def validar_indice(self, i):
        # si la capacidad es 5, y el i es 5:
        # no puedo agergar mas, el ultimo indice disponible es 4
        if i < 0 or i > self.size:
            raise Exception("Indice fuera de la capacidad")
    