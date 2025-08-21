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
org = {}
n = input(" ***Queue of Queue of Queue of ...*** \nEnter Input : ").split(',')

for i in n:
    if i.startswith("en"):
        _, c = i.split()
        c = int(c)
        if (str(c)[0]) not in org:
            sq = [c]
            q.enQueue(sq)
            org[str(c)[0]] = sq
        else:
            org[str(c)[0]].append(c)
        print(f"Enqueued: {int(c)}")

    if i.startswith("de"):
        if q.isEmpty():
            print("Queue is empty")
            continue

        sq = q.items[0]
        number = sq.pop(0)

        if not sq:
            q.deQueue()

            org_id = int(str(number)[0])
            del org[str(number)[0]]

        print(f"Dequeued: {number}")

    if q.isEmpty():
        print("Queue state: []")
    else:
        print(f"Queue state: {q.items}")
