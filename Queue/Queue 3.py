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

word, hint = input("Enter code,hint : ").split(',')

code = ord(hint) - ord(word[0])

new_char = ""
for i in word:
    new_char = chr(ord(i) + code)
    q.enQueue(new_char)
    print(q.items)