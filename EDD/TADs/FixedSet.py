class FixedSet:
    def __init__(self, capacity: int): # O(1)
        '''Set Constructor'''
        if capacity < 1:
            raise Exception("Capacity must be greater than 0")
        
        # Goes from 0 to capacity
        self.data = [False] * (capacity + 1)
        self.size = 0
        self.capacity = capacity

    def insert(self, value): # O(1)
        '''Insert a value to the set'''
        self.validate(value)

        if not self.data[value]:
            self.data[value] = True
            self.size += 1

    def delete(self, value): # O(1)
        self.validate(value)

        if self.data[value]:
            self.data[value] = False
            self.size -= 1
    
    def exists(self, value): # O(1)
        self.validate(value)
        return self.data[value]
    
    def len(self): # O(1)
        return self.size
    
    def validate(self, value): # O(1)
        if value < 0 or value > self.capacity:
            raise Exception("Value out of bounds")
        
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