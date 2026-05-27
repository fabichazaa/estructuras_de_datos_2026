class Dictionary:
    def __init__(self):
        self.keys = []
        self.values = []
        self.size = 0

    def _find_key_index(self, key):
        for i in range(self.size):
            if self.keys[i] == key:
                return i
        return -1

    def insert(self, key, value):  # O(n)
        index = self._find_key_index(key)
        if index != -1:
            # Key exists, update value
            self.values[index] = value
        else:
            # Key does not exist, add new pair
            self.keys.append(key)
            self.values.append(value)
            self.size += 1
    
    def delete(self, key):  # O(n)
        index = self._find_key_index(key)
        if index != -1:
            self.keys.pop(index)
            self.values.pop(index)
            self.size -= 1
        else:
            raise Exception("Key not found")
    
    def exists(self, key):  # O(n)
        return self._find_key_index(key) != -1
    
    def get(self, key):  # O(n)
        index = self._find_key_index(key)
        if index != -1:
            return self.values[index]
        else:
            raise Exception("Key not found")
    
    def len(self):  # O(1)
        return self.size
    
    def __repr__(self):  # O(n)
        pairs_str = ", ".join(f"{self.keys[i]}: {self.values[i]}" for i in range(self.size))
        return f"{{{pairs_str}}}"
    
    def __iter__(self):  # O(n)
        for i in range(self.size):
            yield (self.keys[i], self.values[i])