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
    
q1, q2 = Queue(), Queue()
time = 1
t1, t2 = 0, 0
n = list(map(str, input("Enter people : ")))

for i in range(len(n)):
    if t1 == 3 and not q1.isEmpty():
        q1.deQueue()
        t1 = 0
    
    if t2 == 2 and not q2.isEmpty():
        q2.deQueue()
        t2 = 0

    if len(n) > 0:
        if q1.size() < 5:
            q1.enQueue(n.pop(0))
        elif q2.size() < 5:
            q2.enQueue(n.pop(0))

    if not q1.isEmpty():
        t1 += 1
    if not q2.isEmpty():
        t2 += 1
    
    print(time, n, q1.items, q2.items)
    time += 1