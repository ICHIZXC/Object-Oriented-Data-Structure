class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def add(self,data):
        self.root= self._add(self.root,data)

    def _add(self,root,data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self._add(root.left,data)
        else:
            root.right = self._add(root.right,data)    
        return root
    def printTree(self,root,level=0):
        if root is not None:
            self.printTree(root.right,level+1)
            print('     ' * level, root.data)
            self.printTree(root.left,level+1)
        
        
    def find_path(self):
        result = []
        self.fp(self.root,[],result)
        return result
    
    def fp(self,root,path,result):
        if not root:return
        
        path.append(root)
        if not root.left and not root.right:
            result.append(list(path))
        if root.left:
            self.fp(root.left,path,result)
        if root.right:
            self.fp(root.right,path,result)
        path.pop()
    

    def delete_node(self, root, node_to_delete):
        if not root:
            return root
        
        if root is node_to_delete:
            # Node เจอแล้ว → ลบตามปกติ
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            succ = self._min_value(root.right)
            root.data = succ.data
            root.right = self.delete_node(root.right, succ)
            return root
        
        # ถ้าไม่เจอ node ตรง ๆ ให้ค้นหาใน subtree
        root.left = self.delete_node(root.left, node_to_delete)
        root.right = self.delete_node(root.right, node_to_delete)
        return root
    def _min_value(self, node):
        while node.left:
            node = node.left
        return node


T = BST()
Input,actions = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split('/')
Input = list(map(int,Input.split()))
actions = actions.split(',')
for i in Input:
    T.add(i)

print("(City A) Before the war:")
T.printTree(T.root)
for ac in actions:
    cond, k = ac.split()
    k = int(k)
    
    print("--------------------------------------------------")
    if cond == 'L':
        text = 'less than'
    if cond == 'M':
        text = 'greater than'
    if cond == 'EQ':
        text = 'equal to'
    print(f"Removing paths where the sum is {text} {k}:")
    
    count = 0
    while True:
        
        paths = T.find_path()
        
        found_match = None
        
        for p in paths:
            s = sum(node.data for node in p)
            if (cond == 'L' and s < k) or \
               (cond == 'EQ' and s == k) or \
               (cond == 'M' and s > k):
                found_match = (p, s)
                break  
        
        
        if found_match is None:
            break
        
        
        p, s = found_match
        count += 1
        print(f"{count}) {'->'.join(map(str, [node.data for node in p]))} = {s}")
        T.root = T.delete_node(T.root, p[-1])
    
    if count == 0:
        print("No paths were removed.")
    print("--------------------------------------------------")
    print(f"(City A) After the war:")
    T.printTree(T.root)
    if T.root is None:
        print("City A has fallen!")
        break
