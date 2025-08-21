class Stack:
    def __init__ (self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self, i):
        self.items.append(i)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
s = Stack()
index_stack = Stack()
l = list(map(int, input("*****Big leg on the right side*****\nEnter input: ").split()))
n = len(l)
res = [-1] * n

for i, val in enumerate(l):
    while not s.isEmpty() and val > s.peek():
        popped_val = s.pop()
        popped_idx = index_stack.pop()
        print(f"input[{i}]({val}) is greater than input[top of stack]({popped_val})")
        print("Stack pop")
        res[popped_idx] = val
        print("Output:", res)
    
    print(f"Stack push {i} index of {val}")
    s.push(val)
    index_stack.push(i)

print("Output:", res)