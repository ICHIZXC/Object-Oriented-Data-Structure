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
            print('     ' * level, str(node))
            self.print_tree(node.left, level + 1)
    
    def check_max_sum(self):
        self.max_sum = float("-inf")
        self.max_path = []

        def dfs(node, path):
            if node is None:
                return
            path.append(node.val)

            # if leaf → check sum
            if node.left is None and node.right is None:
                total = sum(path)
                if total > self.max_sum:
                    self.max_sum = total
                    self.max_path = path[:]

            # recurse deeper
            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()  # backtrack

        dfs(self.root, [])

        path_str = " + ".join(map(str, self.max_path))
        return f"{path_str} = {self.max_sum}"
        
T = AVL()
inp = input("Enter tree nodes: ").split()

for i in inp:
    T.insert(int(i))
    
T.print_tree(T.root)
print(f"\nPath with maximum sum: {T.check_max_sum()}")
