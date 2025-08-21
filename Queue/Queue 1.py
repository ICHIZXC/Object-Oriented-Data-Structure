class Queue:
    def __init__ (self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def enQueue(self, i):
        self.items.append(i)
        
    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return int(len(self.items))
    
q = Queue()

enter = input("Enter Input : ").split(',')
for i in enter:
    if i.startswith('E'):
        _, val = i.split()
        q.enQueue(val)
        print(f"Add {val} index is {q.size() - 1}")
        
    elif i == 'D':
        if q.size() == 0:
            print("-1")
        else:
            val = q.deQueue()
            print(f"Pop {val} size in queue is {q.size()}")
        
if q.size() != 0:
    print(f"Number in Queue is :  {q.items}")
else:
    print("Empty")