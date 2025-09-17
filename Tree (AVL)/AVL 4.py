class BST:
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
        
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if not self.root:
            self.root = BST.Node(key)
        else:
            BST._insert(self.root,key)

    def _insert(node,key):
        if key < node.data:
            if node.left:
                BST._insert(node.left,key)
            else:
                node.left = BST.Node(key)
        else:
            if node.right:
                BST._insert(node.right,key)
            else:
                node.right = BST.Node(key)
                
        node.update_height()

    def _get_format(root,ans = ""):
        if root:
            temp = ""
            if root.right:
                temp += BST._get_format(root.right,ans + "     ")
            temp += f"{ans}{root.data}\n"
            if root.left:
                temp += BST._get_format(root.left,ans + "     ")
            return temp
        return ""
    
    def __str__(self):
        return BST._get_format(self.root)

    def isAVL(self):
        return self._isAVL(self.root)

    def _isAVL(self, node):
        if not node:
            return True
        if abs(node.balance_factor()) > 1:
            return False
        expected_height = 1 + max(node.left.h if node.left else -1, node.right.h if node.right else -1)
        if node.h != expected_height:
            return False
        return self._isAVL(node.left) and self._isAVL(node.right)


tree = BST()

print("**********IsAVL**********")
for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
    tree.insert(i)
print("Tree:")
print(tree)
print("Is AVL???:", tree.isAVL())