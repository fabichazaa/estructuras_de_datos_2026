from NodeABB import NodeABB

class ConjuntoABB:
    def __init__(self):
        self.root = None
        self.size = 0

    # complejidad peor caso -> O(n)
    # complejidad caso promedio -> o(log)
    def add(self, x):
        if self.size == 0:
            new_node = NodeABB(x)
            self.root = new_node
        else:
            parent = self.get_parent(x)

            new_node = NodeABB(x)
            new_node.parent = parent

            if x > parent.data:
                parent.right = x
            else:
                parent.left = x
            
        self.size += 1

    # TODO: HACERLO RECURSIVO!!!
    def get_parent(self, x):
        curr = self.root

        while curr is not None:
            parent = curr
            if x < curr.data:
                curr = curr.left
            else:
                curr = curr.right
                
        return parent
    
    # Complejidad peor caso O(n)
    # complejidad caso promedio o(logn)
    def get_contains(self, x):
        curr = self.root

        while curr is not None:
            if x == curr.data:
                return True
            elif x > curr.data:
                curr = curr.right
            else:
                curr = curr.left
        return False

    def sum_r(self, node):
        if node is None:
            return 0
        return node.data + self.sum_r(node.left) + self.sum_r(node.right)

    def sum(self):
        return self.sum_r(self.root)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
    # PREORDER RID [ROOT IZQUIERDA DERECHA]
    def preorder(self, node):
        # RID
        if node is not None:
            # ROOT
            print(node.data)
            # IZQUIERDA
            self.preorder(node.left)
            # DERECHA
            self.preorder(node.right)
    
    # todo va a su correspondiente 
    # MUESTRO EL ROOT AL FINAL -> queda ordenado de menor a mayor
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    # D I R
    def get_parent_r(self, x):
        print("booop")