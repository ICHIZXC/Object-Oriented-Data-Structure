class AVL:
    class Node:
        def __init__ (self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.height = 1

        def __str__(self):
            return str(self.val)

        def getHeight(self, root):
            return 0 if root is None else root.height

        def updateHeight(self):
            self.height = 1 + max(self.getHeight(self.left),self.getHeight(self.right))

        def balanceFactor(self):
            return self.getHeight(self.left) - self.getHeight(self.right)

    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if root is None:
            return AVL.Node(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)

        root.updateHeight()
        return self.rebalance(root)

    def leftRotate(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.updateHeight()
        newRoot.updateHeight()
        return newRoot

    def rightRotate(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.updateHeight()
        newRoot.updateHeight()
        return newRoot

    def rebalance(self, node):
        if node is None:
            return node
        balance = node.balanceFactor()

        if balance < -1:
            if node.right.balanceFactor() > 0:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        if balance > 1:
            if node.left.balanceFactor() < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        return node
    
    def minVal(root):
        current = root
        while current.left:
            current = current.left
        return current
        
    
    def delete(self, val):
        self.root = AVL._delete(self.root, val)
        
    def _delete(root, val):
        if root is None:
            return None
        
        if val < root.val:
            if val < root.val:
                root.left = AVL._delete(root.left, val)
            elif val > root.val:
                root.right = AVL._delete(root.right, val)
                
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            root.val = AVL.minVal(root.right).val
            root.right = AVL._delete(root.right, root.val)

        root.updateHeight()
        return root

    def printTree(self, node=None, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('    ' * level, str(node))
            self.printTree(node.left, level + 1)

            
T = AVL()
inp = list(map(int ,input("Enter Input : ").split()))
for i in inp:
    T.insert(i)

print("Tree Before:")
T.printTree(T.root)

T.delete(5)
print("Tree After:")
T.printTree(T.root)