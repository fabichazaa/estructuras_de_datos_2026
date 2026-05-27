class FixedQueue:
    def __init__(self, capacity): # O(1)
        if capacity < 1:
            raise Exception("Capacity must be greater than 0")
    
        self.data = [None] * (capacity + 1)
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, value): # O(1)
        if self.size == self.capacity:
            raise Exception("Queue is full")
        
        if self.size == 0:
            self.data[self.rear] = value
        else:
            # Divider returns the remainder of the division
            # If rear+1 is equal to the length of the data array, it wraps around to 0
            self.rear = (self.rear + 1) % len(self.data)
            self.data[self.rear] = value
        self.size += 1

    def dequeue(self): # O(1)
        if self.size == 0:
            raise Exception("Queue is empty")
        
        element = self.data[self.front]
        self.data[self.front] = None
        self.size -= 1

        if self.size > 0:
            self.front = (self.front + 1) % len(self.data)
        else:
            self.front = 0
            self.rear = 0

        return element
    
    def peek(self): # O(1)
        if self.size == 0:
            raise Exception("Queue is empty")
        
        return self.data[self.front]
    
    def len(self): # O(1)
        return self.size
    
    def is_empty(self): # O(1)
        return self.size == 0
    
    def __repr__(self): # O(n)
        conj_str = ""

        for i in range(self.size):
            index = (self.front + i) % len(self.data)
            conj_str += f"{self.data[index]},"

        return f"{{{conj_str[:-1]}}}"
    
    def __iter__(self): # O(n)
        for i in range(self.size):
            index = (self.front + i) % len(self.data)
            yield self.data[index]    