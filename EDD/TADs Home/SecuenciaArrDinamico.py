class SecuenciaArrDinamico:
    def __init__(self):
        self.capacidad = 4
        self.size = 0
        self.data = [None] * self.capacidad
        
    def insert_at(self, i, x):
        # 1. Validación de índice para no dejar huecos
        if i < 0 or i > self.size:
            raise Exception("Índice fuera de rango")
            
        # 2. Si está lleno, el resize agranda la casa automáticamente
        if self.size == self.capacidad:
            self.resize(self.capacidad * 2)
            
        # 3. Desplazar los elementos hacia la derecha para hacer el "hueco"
        # Empezamos desde el último elemento real (self.size - 1) y vamos hacia atrás hasta 'i'
        for k in range(self.size - 1, i - 1, -1):
            self.data[k + 1] = self.data[k]
            
        # 4. Colocamos el nuevo elemento en el hueco libre
        self.data[i] = x
        
        # 5. Incrementamos el tamaño actual
        self.size += 1
        
    def insert_last(self, x):
        if self.capacidad == self.size:
            self.resize(self.capacidad*2)

        self.data[self.size] = x
        self.size += 1


    def resize(self, nueva_capacidad):
        redimensionado = [None] * nueva_capacidad
        for i in range(self.size):
            redimensionado[i] = self.data[i]
        self.data = redimensionado
        self.capacidad = nueva_capacidad

    def validar_indice(self, i):
        if i < 0:
            raise Exception("Indice no puede ser negativo")