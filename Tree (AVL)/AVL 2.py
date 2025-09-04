class AVL:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None
        self.height = 0 if val is None else self.setHeight()
        self.root = self if val is not None else None

    def __str__(self):
        return str(self.val)
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a, b)
        return self.height
    
    def getHeight(self, node):
        return -1 if node is None else node.height

    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)
    
    def insert(self, val):
        self.root = self._add(self.root, val)

    def _add(self, root, val):
        if root is None:
            return AVL(val)
        else:
            if int(val) < int(root.val):
                root.left = self._add(root.left, val)
            else:
                root.right = self._add(root.right, val)
        root = self.rebalance(root)
        root.setHeight()
        return root
    
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y
    
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y

    def rebalance(self, x):
        if x is None:
            return x
        balance = x.balanceValue()
        if balance == -2:
            if x.right and x.right.balanceValue() == 1:
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)
        elif balance == 2:
            if x.left and x.left.balanceValue() == -1:
                x.left = self.leftRotate(x.left)
            x = self.rightRotate(x)
        return x
    
    def printTree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


def check_same_tree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return (t1.val == t2.val and
            check_same_tree(t1.left, t2.left) and
            check_same_tree(t1.right, t2.right))


# ---------------- MAIN ----------------
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
Tree1.printTree(Tree1.root)

print("\nTree 2")
Tree2.printTree(Tree2.root)

print()
if check_same_tree(Tree1.root, Tree2.root):
    print("Same Tree")
else:
    print("Different Tree")
