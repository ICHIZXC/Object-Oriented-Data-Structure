class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)
    
class BST:
    def __init__ (self):
        self.root = None
        
    def insert(self, val):
        self.root = BST._insert(self.root, val)
    
    def _insert(root, val):
        if root is None:
            return Node(val)
        else:
            if val < root.val:
                root.left = BST._insert(root.left, val)
            elif val > root.val:
                root.right = BST._insert(root.right, val)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    # def cal_sum(self):
    #     return BST._cal_sum(self.root)
        
    # def _cal_sum(root):
    #     if root is None:
    #         return 0
    #     else:
    #         return root.val + BST._cal_sum(root.left) + BST._cal_sum(root.right)
    
    # THIS IS MUCH BETTER #
    def cal_sum(self, root):
        if root is None:
            return 0
        return root.val + self.cal_sum(root.left) + self.cal_sum(root.right)
    
    def times_k(self, k):
        self.root = BST._times_k(self.root, int(k))
        
    def _times_k(root, k: int):
        if root:
            BST._times_k(root.left, k)
            if int(root.val) > k:
                root.val *= k
            BST._times_k(root.right, k)
        return root

    # def times_k(self, k, node=None):
    #     if node is None:
    #         node = self.root
    #     if node:
    #         self.times_k(k, node.left)       # process left subtree
    #         if node.val > k:                 # only multiply if value > k
    #             node.val *= k
    #         self.times_k(k, node.right)      # process right subtree

            
print("**Sum of tree**")
inp, k = input("Enter input : ").split('/')
T = BST()
ls = [int(i) for i in inp.split()]
for i in ls:
    T.insert(i)
    
print("\nTree before:")
T.printTree(T.root)

print(f"Sum of all nodes = {T.cal_sum(T.root)}")

print("\nTree after:")
T.times_k(k)
T.printTree(T.root)
print(f"Sum of all nodes = {T.cal_sum(T.root)}")