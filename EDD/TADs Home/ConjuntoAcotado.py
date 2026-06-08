class ConjuntoAcotado:
    def __init__(self, capacidad):
        if capacidad < 0:
            raise IndexError("Capacidad no puede ser negativa")
        
        self.data = [False] * capacidad
        self.capacidad = capacidad
        self.size = 0

    def len(self):
        return self.size
    
    def insertar(self, x):
        self.validar_elemento(x)

        if self.data[x] == False:
            self.data[x] = True
            self.size += 1

    def remover(self, x):
        self.validar_elemento(x)

        if self.data[x] == True:
            self.data[x] = False
            self.size -= 1

    def forma_parte(self, x):
        self.validar_elemento(x)
        
        return self.data[x]
    
    # capacidad: la capacidad del conjunto mas grande
    def union(self, conjunto2: ConjuntoAcotado):
        if conjunto2.capacidad > self.capacidad:
            capacidad_nueva = conjunto2.capacidad
        else:
            capacidad_nueva = self.capacidad
        
        conjunto_union = ConjuntoAcotado(capacidad_nueva)

        for i in range(capacidad_nueva):
            # el conjunto mas chico no va a tener todos los data!
            valor_self = self.data[i] if i < self.capacidad else False

            valor_c2 = conjunto2.data[i] if i < conjunto2.capacidad else False

            conjunto_union.data[i] = valor_self or valor_c2

        return conjunto_union


    # capacidad: tomo el size del mas chico!
    # No va a haber intersecciones en los espacios de diferencia
    def interseccion(self, conjunto2):
        if conjunto2.capacidad > self.capacidad:
            capacidad_nueva = self.capacidad
        else:
            capacidad_nueva = conjunto2.capacidad

        conjunto_inter = ConjuntoAcotado(capacidad_nueva)

        for i in range(capacidad_nueva):
            conjunto_inter.data[i] = self.data[i] and conjunto2.data[i]
            

    def validar_elemento(self, x):
        if x < 0 or x >= self.capacidad:
            raise Exception("El elemento se encuentra fuera de la capacidad")

    