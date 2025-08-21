class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
            self.size += 1
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = self.Node(data)
        self.size += 1
        
    def swap(self, x):
        temp1 = x.next
        temp2 = x.next.next
        x.next = temp2
        temp1.next = temp2.next
        temp2.next = temp1
        
    def swap_head(self):
        temp1 = self.head
        temp2 = self.head.next
        temp1.next = temp2.next
        temp2.next = temp1
        self.head = temp2
    
    def find(self, x):
        if x >= self.size:
            return None
        h = self.head
        for i in range(x-1):
            h = h.next
        return h

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data, end=" → " if current.next else "\n")
            current = current.next
            
print(" *** Ant Army ***")
inp, node = input("Input : ").split(',')

al = LinkedList()

for i in inp.split():
    al.append(i)
print('Before : ',end='')
al.print_list()

count = 0
while count < al.size:
    start = count
    if int(node) == 0:
        break
    for i in range(start, min(start + int(node), al.size - 1)):
        print("Start", start+1, start*2 + int(node) - i, min(start + int(node), al.size - 1))
        for j in range(start, min(start*2 + int(node) - i - 1, al.size - i + start - 1)):
            print(count+1, i+1, j+1)
            if j == 0:
                al.swap_head()
            else:
                temp = al.find(j)
                al.swap(temp)
            al.print_list()
        count += 1
    count += int(node)
    
print("After : ", end ='')
al.print_list()