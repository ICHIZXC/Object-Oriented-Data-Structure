class AVL:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.h = 1

        def update_height(self):
            left_h = self.left.h if self.left else 0
            right_h = self.right.h if self.right else 0
            self.h = 1 + max(left_h, right_h)

        def balance_factor(self):
            left_h = self.left.h if self.left else 0
            right_h = self.right.h if self.right else 0
            return left_h - right_h
        
        def __str__(self):
            return str(self.val)
    
    def __init__(self):
        self.root = None
    
    def getHeight(self, node):
        return 0 if node is None else node.height
    
    def getSize(self, node):
        return 0 if node is None else node.size

    def balanceFactor(self, node):
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def update(self, node):
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        node.size = 1 + self.getSize(node.left) + self.getSize(node.right)
    
    def insert(self, val):
        self.root = self._insert(self.root, val)
        return self.root

    def _insert(self, root, val):
        if root is None:
            return self.Node(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        self.update(root)
        balance = self.balanceFactor(root)

        # Rebalance
        if balance > 1:
            if val < root.left.val:   # LL
                return self.rotateRight(root)
            else:                     # LR
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)
        if balance < -1:
            if val > root.right.val:  # RR
                return self.rotateLeft(root)
            else:                     # RL
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)
        return root
    
    def rotateRight(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update(y)
        self.update(x)
        return x

    def rotateLeft(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update(x)
        self.update(y)
        return y
    
    def printTree(self, node=None, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def kthSmallest(self, k):
        return self._kthSmallest(self.root, k)

    def _kthSmallest(self, node, k):
        if not node:
            return None
        left_size = self.getSize(node.left)
        if k == left_size + 1:
            return node.val
        elif k <= left_size:
            return self._kthSmallest(node.left, k)
        else:
            return self._kthSmallest(node.right, k - left_size - 1)

T = AVL()
amount, inp, k = input("*** Simple but more ***\ninput  N node, Data, K small : ").split(',')
for i in [int(i) for i in inp.split()]:
    T.insert(i)

print(T.kthSmallest(int(k)))