class SortedSequence:
    def __init__(self):
        self.data = []
        self.size = 0
    
    def len(self): # O(1)
        return self.size

    def insert_at(self, i: int, value): # O(n)
        if i < 0 or i > self.size:
            raise Exception("Index out of bounds")
        
        
        new_data = [None] * (self.size + 1)
        # we copy the elements before the index i
        for j in range(i):
            new_data[j] = self.data[j]

        # we insert the new value at index i
        new_data[i] = value
        # we copy the elements after the index i
        for j in range(i, self.size):
            new_data[j + 1] = self.data[j]

        self.data = new_data
        self.size += 1
    
    def delete_at(self, i: int): # O(n)
        if i < 0 or i >= self.size:
            raise Exception("Index out of bounds")
        
        new_data = [None] * (self.size - 1)
        # we copy the elements before the index i
        for j in range(i):
            new_data[j] = self.data[j]

        # we copy the elements after the index i
        for j in range(i + 1, self.size):
            new_data[j - 1] = self.data[j]

        self.data = new_data
        self.size -= 1

    def insert_first(self, value): # O(n)
        self.insert_at(0, value)

    def insert_last(self, value): # O(1)
        self.insert_at(self.size, value)
    
    def delete_first(self): # O(n)
        self.delete_at(0)
    
    def delete_last(self): # O(1)
        self.delete_at(self.size - 1)

    def __repr__(self): # O(n)
        conj_str = ""

        for i in range(self.size):
            conj_str += f"{self.data[i]},"

        return f"{{{conj_str[:-1]}}}"
    
    def __iter__(self): # O(n)
        for i in range(self.size):
            yield self.data[i]