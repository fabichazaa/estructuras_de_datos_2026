from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # tail is always next to head
    def dequeue(self): # O (1) GOOD

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            element = self.head.data
            self.tail.next = self.head.next
            self.head = self.head.next
        self.size -= 1

        return element