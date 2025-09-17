class AVL:
    class Node:
        def __init__(self, val, left = None, right = None):
            self.val = val
            self.left = left
            self.right = right
            self.height = self.setHeight()

        def __str__ (self):
            return str(self.val)
        
        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height
        
        def getHeight(self, node):
            return -1 if node == None else node.height
        
        def balanceValue(self):
            return int(self.getHeight(self.left)) - int(self.getHeight(self.right))
        
    def __init__ (self):
        self.root = None

    def insert(self,val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if root is None:
            return self.Node(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        root = self.rebalance(root)
        return root
        
    def rebalance(self, x):
        if x == None:
            return x
        balance = x.balanceValue()
        if balance ==  -2:
            if x.right.balanceValue() > 0:
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)
        elif balance == 2:
            if x.left.balanceValue() < 0:
                x.left = self.leftRotate(x.left)
            x = self.rightRotate(x)
        x.setHeight()
        return x
    
    def leftRotate(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root

        root.setHeight()
        newRoot.setHeight()

        return newRoot

    def rightRotate(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root           

        root.setHeight()
        newRoot.setHeight()

        return newRoot
        
    def print_tree(self, node=None, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('    ' * level + str(node))
            self.print_tree(node.left, level + 1)


def check_same_tree(Tree1, Tree2):
    if Tree1 is None and Tree2 is None:
        return True
    
    # one is None but not both → different
    if Tree1 is None or Tree2 is None:
        return False
    
    return (Tree1.val == Tree2.val and
            check_same_tree(Tree1.left, Tree2.left) and
            check_same_tree(Tree1.right, Tree2.right))


Tree1 = AVL()

Tree2 = AVL()



Tree1_inp, Tree2_inp = (input("Enter Tree1/Tree2 : ")).split("/")

Tree1_inp = Tree1_inp.split()

Tree2_inp = Tree2_inp.split()



for data in Tree1_inp:

    Tree1.insert(int(data))



for data in Tree2_inp:

    Tree2.insert(int(data))


print("Tree 1")    

Tree1.print_tree(Tree1.root)



print()

print("Tree 2")

Tree2.print_tree(Tree2.root)



print()

if check_same_tree(Tree1.root, Tree2.root):

    print("Same Tree")

else:

    print("Different Tree")
