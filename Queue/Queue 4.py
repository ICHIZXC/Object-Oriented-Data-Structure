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
    
mq = Queue()
yq = Queue()

ma = Queue()
mp = Queue()
ya = Queue()
yp = Queue()

al = input("Enter Input : ").split(',')
for pair in al:
    my, your = pair.strip().split()
    mq.enQueue(my)
    yq.enQueue(your)

print('My   Queue =', ', '.join(mq.items))
print('Your Queue =', ', '.join(yq.items))

Activity = {0:'Eat', 1:'Game', 2:'Learn', 3:'Movie'}
Place = {0:'Res.', 1:'ClassR.', 2:'SuperM.', 3:'Home'}

my_activities = []
your_activities = []

score = 0

for i in mq.items:
    my_act, my_pla = i.split(':')
    ma.enQueue(Activity[int(my_act)])
    mp.enQueue(Place[int(my_pla)])
    my_activities.append(f"{Activity[int(my_act)]}:{Place[int(my_pla)]}")
    
for j in yq.items:
    your_act, your_pla = j.split(':')
    ya.enQueue(Activity[int(your_act)])
    yp.enQueue(Place[int(your_pla)])
    your_activities.append(f"{Activity[int(your_act)]}:{Place[int(your_pla)]}")

print('My   Activity:Location =', ', '.join(my_activities))
print('Your Activity:Location =', ', '.join(your_activities))

for i in range(mq.size()):
    my_act, my_pla = map(int, mq.items[i].split(':'))
    your_act, your_pla = map(int, yq.items[i].split(':'))
    if my_act == your_act and my_pla == your_pla:
        score += 4
    elif my_act == your_act:
        score += 1
    elif my_pla == your_pla:
        score += 2
    else: score -= 5
    
if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
    
elif score > 0:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
    
else: print(f"No! We're just friends. : Score is {score}.")