from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, x): # O(1)
        new_node = Node(x)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def insert_last(self, x): # O(1)
        new_node = Node(x)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1
    
    def insert_at(self, x, i): # O(n)
        if i == 0:
            self.insert_first(x)

        n = self.head
        for i in range(i-1):
            n = n.next
        next_node = n.next

        new_node = Node(x)
        new_node.next = next_node
        n.next = new_node
        
        self.size += 1

    def delete_element(self, x):
        n = self.head
        prev = None
        for _ in range(self.size):
            if (n.data == x and prev is None):
                self.head = n.next
                return True
            elif (n.data == x):
                prev.next = n.next
                return True
            prev = n
            n = n.next
        return False

    def delete_position(self, i):
        "boop"

    def len(self):
        return self.size

    def index_of(self, x):
        n = self.head
        for i in range(self.size):
            if x == n.data:
                return i
            n = n.next
        return -1

    def exists(self, x):
        return self.index_of(x) != -1
    
    def __repr__(self): # O(n)
        conj_str = ""

        n = self.head
        for _ in range(self.size):
            conj_str += f"{n.data},"
            n = n.next

        return f"{{{conj_str[:-1]}}}"


            
