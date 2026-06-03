class Node:
    def __init__(self, x):
        self.data = x
        # at start the following node is none
        self.next = None
        self.prev = None