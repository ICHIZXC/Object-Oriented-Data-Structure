class LinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self,val):
        if not self.head:
            self.head = self.Node(val)
        else:
            h = self.head
            while h.next:
                h = h.next
            h.next = self.Node(val)
        self.size += 1
    
    def peek_head(self):
        return self.head.val
        
    def delete_head(self):
        if self.head == None: return
        if self.head.next == None:
            p = self.head
            self.head = None
            self.size -= 1
            return p.val
        else:
            p = self.head
            self.head = self.head.next
            self.size -= 1
            return p.val
        
    def isEmpty(self):
        return self.size == 0
        
    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.val))
            node = node.next
        if len(ans) == 0:
            return "Empty"
        return ' '.join(ans)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next
        

print("***This colony is our home***")
inp, op = input("Enter input : ").split('/')
worker, army = inp.split()

count_a, count_w = 0, 0
w_food, a_food = 2, 5
w_dmg, a_dmg =  5, 10
queen_angry = 0

al = LinkedList()
for i in range(1, int(worker)+1):
    al.append(f"W{i}")
    count_w += 1
for j in range(1, int(army)+1):
    al.append(f"A{j}")
    count_a += 1
    
print(f"Current Ant List: {al}\n")

for i in op.split(','):
    if i.startswith("C"):
        _, food = i.split()
        print("Food carrying mission : ", end = '')
        usedc = []
        total = 0
        
        if al.isEmpty():
            print("Empty")
            print("The food load is incomplete!")
            print("Queen is angry! ! !")
            queen_angry += 1
        
        else:
            while total < int(food) and not al.isEmpty():
                ant = al.peek_head()
                if ant.startswith("W"):
                    total += 2
                    count_w -= 1
                elif ant.startswith("A"):
                    total += 5
                    count_a -= 1
                usedc.append(ant)
                al.delete_head()

            if total < int(food):
                print(' '.join(usedc))
                print("The food load is incomplete!")
                print("Queen is angry! ! !")
                queen_angry += 1
            else:
                print(' '.join(usedc))
                
        if queen_angry == 3: print("**The queen is furious! The ant colony has been destroyed**")    
        
    elif i.startswith("F"):
        _, hp = i.split()
        print("Attack mission : ", end='')
        usedf = []
        totalhp = 0

        if al.isEmpty():
            print("Empty")
        else:
            while not al.isEmpty() and totalhp < int(hp):
                antf = al.peek_head()
                if antf.startswith("A"):
                    totalhp += 10
                    count_a -= 1
                    usedf.append(antf)
                    al.delete_head()
                elif antf.startswith("W"):
                    totalhp += 5
                    count_w -= 1
                    usedf.append(antf)
                    al.delete_head()
                else:
                    break
            print(' '.join(usedf))
            if totalhp < int(hp):
                print("Ant nest has fallen!")
                exit()
        
    elif i.startswith("S"):
        w_ant = []
        s_ant = []
        for i in al:
            if i.startswith("W"):
                w_ant.append(i)
            else: s_ant.append(i)
        print("-> Remaining worker ants:", ' '.join(w_ant) if w_ant else "Empty")
        print("-> Remaining soldier ants:", ' '.join(s_ant) if s_ant else "Empty")

    elif i.startswith("W"):
        _, amount = i.split()
        for j in range(int(amount)):
            count_w += 1
            al.append(f"W{count_w}")


    elif i.startswith("A"):
        _, amount = i.split()
        for k in range(int(amount)):
            count_a += 1
            al.append(f"A{count_a}")