class SquaredMatrix:
    def __init__(self, dimension):
        if dimension < 1:
            raise Exception("Dimension must be greater than 0")
        # a range is done to avoid memory referencing
        self.data = [[None] * dimension for _ in range(dimension)]        
        self.size = 0
        self.dimension = dimension

    def insert(self, i, j, value): # O(1)
        self.validate(i, j)

        prev = self.data[i][j]
        self.data[i][j] = value
        if prev is None: self.size += 1
            
    def delete(self, i, j): # O(1)
        self.validate(i, j)

        if self.data[i][j] is not None:
            self.data[i][j] = None
            self.size -= 1
        else:
            raise Exception("No element to delete")
                
    def get(self, i, j): # O(1)
        self.validate(i, j)
        return self.data[i][j]

    def validate(self, i, j): # O(1)
        if (i < 0 or i >= self.dimension) or (j < 0 or j >= self.dimension):
            raise Exception("Index out of bound")
        
    def __repr__(self): # O(n^2)
        matrix_str = ""
        for i in range(self.dimension):
            row_str = ", ".join(str(self.data[i][j]) for j in range(self.dimension))
            matrix_str += f"[{row_str}]\n"
        return matrix_str
    
    def __iter__(self): # O(n^2)
        for i in range(self.dimension):
            for j in range(self.dimension):
                yield self.data[i][j]