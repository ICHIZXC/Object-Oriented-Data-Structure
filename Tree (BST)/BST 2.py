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

    def _insert(root, val):
        if root is None:
            return Node(val)
        else:
            if val < root.val:
                root.left = BST._insert(root.left, val)
            else:
                root.right = BST._insert(root.right, val)
        return root
    
    # def inOrder(self, root):
    #     if root:
    #         self.inOrder(root.left)
    #         print(root.val, end=" ")
    #         self.inOrder(root.right)
    
    def inOrder(self):
        BST._inOrder(self.root)
        
    def _inOrder(root):
        if root:
            BST._inOrder(root.left)
            print(root.val, end = ' ')
            BST._inOrder(root.right)
            
    def checkSum(self, node, target):
        if node is None:
            return False

        if node.left is None and node.right is None:
            return target == node.val

        return (self.checkSum(node.left, target - node.val) or self.checkSum(node.right, target - node.val))

T = BST()
inp, plus = input('Enter the values to insert into BST and target sum : ').split(' / ')
ls = [int(i) for i in inp.split()]
for i in ls:
    T.insert(i)

print("Inorder Traversal of BST : ", end = '')
T.inOrder()

pathCheck = T.checkSum(T.root, int(plus))
print(f"\nPath with sum {plus} exists : {pathCheck}")