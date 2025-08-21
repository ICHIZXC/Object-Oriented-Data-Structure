class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def appendHead(self,val):
        node = Node(val,self.head)
        self.head = node
        self.size += 1

    def appendLast(self,val):
        if self.head is None:
            self.appendHead(val)
            self.size += 1
            return

        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = Node(val)
            self.size += 1

    def removeLast(self):
        if self.head == None:
            self.size = 0
            return
        if self.head.next == None:
            self.head = None
            self.size = 0
            return
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1

    def rename(self, newName):
        if self.head == None:
            return
        if self.head.next == None:
            self.head.val = newName
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next.val = newName

    def printList(self):
        p = self.head
        if self.isEmpty():
            print("Linklist is empty!")
        while p != None:
            if p.next is None:
                print(p.val)
            else:
                print(p.val, end = ' -> ')
            p = p.next

    def printListWithNoDuplicate(self):
        c = self.head
        while c:
            r = c
            while r.next:
                if r.next.val == c.val:
                    r.next = r.next.next
                else:
                    r = r.next
            c = c.next
        
        self.printList()

    def isEmpty(self):
        return self.size == 0

def convertToLinkList(ls):
    x = LinkList()
    for i in ls:
        x.appendLast(i)
    return x


print("*** My Favourite Keynote ***")

inputl = input("Enter Input / List of operation : ").split('/')

listSong = [ele for ele in inputl[0].strip().split(' ')]

operations = [ele for ele in inputl[1].strip().split(", ")]



myLinkList = convertToLinkList(listSong)

myLinkList.printList()

for i in operations:
    if i.startswith("D"):
        if myLinkList.isEmpty():
            print("Error!!!")
        else: myLinkList.removeLast()
    elif i.startswith("R"):
        if myLinkList.isEmpty():
            print("Error!!!")
            continue
        _, re = i.split()
        re = str(re)
        myLinkList.rename(re)
    elif i.startswith("A"):
        _, add = i.split()
        add = str(add)
        myLinkList.appendLast(add)

myLinkList.printList()

myLinkList.printListWithNoDuplicate()