class Linklist:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
        
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, val):
        n = self.Node(val)
        if self.head == None:
            self.head = n
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = n
        self.size += 1

    def add_head(self, val):
        n = self.Node(val)
        n.next = self.head
        self.head = n
        self.size += 1
        
    def print_list(self):
        ans = []
        p = self.head
        while p:
            ans.append(p.val)
            p = p.next
        print(' -> '.join(ans) if ans else "None")
        
    def print_advance(self):
        p = self.head
        while p:
            print(p.val, end = ' -> ')
            p = p.next
        print("None")
        
    def remove_head(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1
        
    def remove_tail(self):
        p = self.head
        if p.next == None:
            self.head = None
            self.size -= 1
            return
        while p.next.next:
            p = p.next
        p.next = None
        self.size -= 1
        
    def insert_after(self, i, val):
        n = self.Node(val)
        p = self.head
        count = 0
        while p:
            if count == i:
                n.next = p.next
                p.next = n
                return
            p = p.next
            count += 1
        
    def delete_after(self, i):
        p = self.head
        count = 0
        if p.next == None:
            return
        while p:
            if count == i:
                p.next = p.next.next
                return
            p = p.next
            count += 1

    def swap(self, p):
        temp1 = p.next
        temp2 = p.next.next
        p.next = temp2
        temp1.next = temp2.next
        temp2.next = temp1
    
    def swap_head(self):
        temp1 = self.head
        temp2 = self.head.next
        temp1.next = temp2.next
        temp2.next = temp1
        self.head = temp2
        
    def swap_from_index(self, i):
        if i == 0:
            self.swap_head()
            return

        p = self.head
        count = 0
        while p and count < i-1:
            p = p.next
            count += 1

        if p and p.next and p.next.next:
            temp1 = p.next
            temp2 = p.next.next
            p.next = temp2
            temp1.next = temp2.next
            temp2.next = temp1

    def buble_sort(self):
        swap = True
        while swap:
            p = self.head
            index = 0
            swap = False
            while p and p.next:
                if p.val > p.next.val:
                    if index == 0:
                        self.swap_head()
                    else:
                        self.swap_from_index(index)
                    swap = True
                    self.print_list()
                p = p.next
                index += 1

    def remove_dupe(self):
        check = self.head
        while check:
            runner = check
            while runner.next:
                if runner.next.val == check.val:
                    runner.next = runner.next.next
                    self.size -= 1
                else: runner = runner.next
            check = check.next
        
ml = Linklist()
inp = [c for c in input("Enter input : ").split()]
for i in inp:
    ml.append(i)

# ml.add_head('0')
# ml.remove_tail()
# ml.insert_after(3, "5")
# ml.delete_after(0)

ml.print_list()
# ml.swap_head()
ml.remove_dupe()
ml.print_list()
ml.buble_sort()
ml.print_list()



# ml.print_advance()

print(ml.size)