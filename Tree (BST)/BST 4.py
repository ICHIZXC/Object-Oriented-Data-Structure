class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__ (self):
        return str(self.val)

class BST:
    def __init__ (self):
        self.root = None
        self.found_ts = False
        self.success = False
        
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
            
    def printPaths(self, ts, esc):
        self._printPaths(self.root, [], ts, esc)
        
        if not self.success:
            print(">>> Mission Failed <<<")

    def _printPaths(self, node, path, ts, esc):        
        if node is None:
            return

        path.append(node.val)
        
        if node.val == int(ts) and not self.found_ts:
            self.found_ts = True
            print("Found Treasure !!!")
            if node.val == int(esc):
                self.success = True
                print("Found Escape !!!")
                print("✅", " -> ".join(map(str, path)))
                print(">>> Mission Complete <<<")
                path.pop()
                return
            print("❌", " -> ".join(map(str, path)))

        elif node.val == int(esc) and self.found_ts:
            self.success = True
            print("Found Escape !!!")
            print("✅", " -> ".join(map(str, path)))
            print(">>> Mission Complete <<<")
            path.pop()
            exit()
        # Normal path node
        else:
            print("❌", " -> ".join(map(str, path)))
        
        # if node.val != int(ts):
        #     if node.val == int(esc) and self.found_ts:
        #         self.success = True
        #         print("Found Escape !!!")
        #         print("✅", " -> ".join(map(str, path)))
        #         print(">>> Mission Complete <<<")
        #         exit()
        #     print("❌", " -> ".join(map(str, path)))
        
        # if (node.val == int(ts)):
        #     self.found_ts = True
        #     print("Found Treasure !!!")
        #     print("❌", " -> ".join(map(str, path)))
        
        self._printPaths(node.left, path, ts, esc)
        self._printPaths(node.right, path, ts, esc)

        path.pop()

inp, ts, esc = input("Enter Input : ").split('/')
T = BST()

for i in [int(j) for j in inp.split()]:
    T.insert(i)

T.printTree(T.root)
print("-------------------------------------------------")
T.printPaths(ts, esc)
