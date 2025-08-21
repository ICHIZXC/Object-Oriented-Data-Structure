class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.size += 1
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(data)
        self.size += 1
        

    def print_list(self):
        p = self.head
        out = []
        while p:
            out.append(p.data)
            p = p.next
        print(" -> ".join(out))

    def swap(self, x):
        temp1 = x.next
        temp2 = x.next.next
        x.next = temp2
        temp1.next = temp2.next
        temp2.next = temp1
        
    def swapHead(self):
        temp1 = self.head
        temp2 = self.head.next
        temp1.next = temp2.next
        temp2.next = temp1
        self.head = temp2
    
    def find(self, x):
        h = self.head
        if x > self.size:
            return None
        for i in range(x-1):
            h = h.next
        return h


inp = input("input : ").split()
ll = LinkedList()
for i in inp:
    ll.append(i)
    
print("Original")
ll.print_list()

print("\nProcess")
for i in range(ll.size):
    for j in range(ll.size - i - 1):
        if j == 0:
            ll.swapHead()
        else:
            temp = ll.find(j)
            ll.swap(temp)
        ll.print_list()

print("\nReverse")
ll.print_list()