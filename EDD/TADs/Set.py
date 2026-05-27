class Set:
    def __init__(self): # O(1)
        self.data = []
        self.size = 0

    def insert(self, value): # O(n)
        if value < 0:
            raise Exception("Value must be non-negative")
        
        if value >= self.size:
            # we need to resize the data array to accommodate the new value
            new_data = [False] * (value + 1)
            for i in range(len(self.data)):
                new_data[i] = self.data[i]
            new_data[value] = True
            self.data = new_data
            self.size += 1
        elif not self.data[value]:
            self.data[value] = True
            self.size += 1
        
    def delete(self, value): # O(1)
        if value < 0 or value >= len(self.data):
            raise Exception("Value out of bounds")
        
        if self.data[value]:
            self.data[value] = False
            self.size -= 1
    
    def exists(self, value): # O(1)
        if value < 0 or value >= len(self.data):
            return False
        
        return self.data[value]
    
    def len(self): # O(1)
        return self.size
    
        
    def __repr__(self): # O(n)
        conj_str = ""

        for i in range(len(self.data)):
            if self.data[i]:
                conj_str += f"{i},"

        return f"{{{conj_str[:-1]}}}"
    
    def __iter__(self): # O(n)
        # looks at every position in the boolean array
        # selects only positions marked True
        # returns those positions as the elements of the set
        yield from [i for i in range(len(self.data)) if self.data[i]]