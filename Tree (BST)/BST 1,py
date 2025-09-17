class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = BST._insert(self.root, val)
        return self.root

    def _insert(root, val):
        if root is None:
            return Node(val)
        else:
            if val < root.val:
                root.left = BST._insert(root.left, val)
            else:
                root.right = BST._insert(root.right, val)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

T.printTree(root)
