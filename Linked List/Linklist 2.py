class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
        
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def append(self,val):
        if self.head is None:
            node = Node(val, self.head)
            self.head = node
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = Node(val)

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.val))
            node = node.next
        return '->'.join(ans)
    
    def sortList(self):
        swap = True
        while swap:
            p = self.head
            swap = False
            while p and p.next:
                if p.val > p.next.val:
                    print(f"\nSwapping {p.val} and {p.next.val}")
                    p.val, p.next.val = p.next.val, p.val
                    swap = True
                    print(f"List: {x}")
                p = p.next
    
def convertToLinkList(_input):
    x = LinkedList()
    for i in _input:
        x.append(i)
    return x
    
print("*****Bubble Sort Linked List*****")
num = list(map(int, input("Enter Input: ").split(',')))
print("Input List:", '->'.join(map(str, num)), end = '\n')
print("_______________________________________")

x = convertToLinkList(num)
x.sortList()

print("_______________________________________")
print("Sorted List:", x)