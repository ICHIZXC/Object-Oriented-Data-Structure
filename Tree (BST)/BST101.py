class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            
        def __str__(self):
            return str(self.val)
        
    def __init__(self):
        self.root = None
        
    def minVal(root):
        current = root
        while current.left != None:
            current = current.left
        return current
    
    def insert(self, val):
        self.root = BST._insert(self.root, val)
    
    def _insert(root, val):
        if root is None:
            return BST.Node(val)
        
        else:
            if val < root.val:
                root.left = BST._insert(root.left, val)
            elif val > root.val:
                root.right = BST._insert(root.right, val)
        return root
    
    def delete(self, val):
        self.root = BST._delete(self.root, val)
        
    def _delete(root, val):
        if root is None:
            return None
        
        if val < root.val:
            if val < root.val:
                root.left = BST._delete(root.left, val)
            elif val > root.val:
                root.right = BST._delete(root.right, val)
                
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            root.val = BST.minVal(root.right).val
            root.right = BST._delete(root.right, root.val)

        return root
    
    def levelOrder(self):
        if self.root is None:
            return None
        queue = [self.root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(str(node))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(" ".join(res))
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def preOrder(self, root):
        if root != None:
            print(root, end = ' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print(root, end = ' ')
            self.inOrder(root.right)
    
    def postOrder(self, root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root, end = ' ')
    
    # def preOrder(self, root):
    #     result = []
    #     def traverse(node):
    #         if node:
    #             result.append(str(node))
    #             traverse(node.left)
    #             traverse(node.right)
    #     traverse(root)
    #     print(" ".join(result))

    # def inOrder(self, root):
    #     result = []
    #     def traverse(node):
    #         if node:
    #             traverse(node.left)
    #             result.append(str(node))
    #             traverse(node.right)
    #     traverse(root)
    #     print(" ".join(result))

    # def postOrder(self, root):
    #     result = []
    #     def traverse(node):
    #         if node:
    #             traverse(node.left)
    #             traverse(node.right)
    #             result.append(str(node))
    #     traverse(root)
    #     print(" ".join(result))
        
    def dfsPaths(self, root):
        def helper(node, path):
            if node is None:
                return
            path.append(str(node)) 

            if node.left is None and node.right is None:
                print("->".join(path))

            helper(node.left, path)
            helper(node.right, path)

            path.pop()
        
        helper(root, [])


T = BST()
inp = list(map(int ,input("Enter Input : ").split()))
for i in inp:
    T.insert(i)

print("Tree Before:")
T.printTree(T.root)
# T.delete(14)
# print("\nTree after:")
# T.printTree(T.root)


# T.preOrder(T.root)
# print()
# T.inOrder(T.root)
# print()
# T.postOrder(T.root)
