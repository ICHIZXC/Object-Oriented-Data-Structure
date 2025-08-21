class Stack:
    def __init__ (self, list = []):
        self.items = list
        self.size = 0
        
    def __str__(self):
        s = ''
        for i in self.items:
            s += str(i) + ' '
        return s
        
    def stackSize(self):
        print(len(self.items))
    
    def isEmpty(self):
        return self.size == 0
    
    def pop(self):
        if not self.isEmpty():
            self.size -= 1
            return self.items.pop()
            
        
    def push(self, i):
        self.items.append(i)
        self.size += 1
        
    def top(self):
        return self.items[-1]
    
    def buttom(self):
        return self.items[0]

s = Stack()
x = input()
for i in range(len(x)-1, -1, -1):
    if(x[i].isnumeric()):
        s.push(int(x[i]))
    elif(x[i] == '+'):
        a = s.pop()
        b = s.pop()
        c = a+b
        s.push(c)
    elif(x[i] == '-'):
        a = s.pop()
        b = s.pop()
        c = a-b
        s.push(c)
    elif(x[i] == '/'):
        a = s.pop()
        b = s.pop()
        c = a/b
        s.push(c)
    elif(x[i] == '*'):
        a = s.pop()
        b = s.pop()
        print(type(a), type(b))
        c = a*b
        s.push(c)

print(s.top())