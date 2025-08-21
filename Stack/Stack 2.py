class Stack:
    def __init__(self, list=None):
        self.item = [] if list is None else list

    def push(self, i):
        self.item.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.item.pop()

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

def fine_plate(target):
    plate = [25, 20, 15, 10, 5, 2.5, 1.25]
    result = []
    for p in plate:
        while sum(result) + p <= target and len(result) < 5:
            result.append(p)
    return sorted(result,reverse=True) if sum(result) == target else None

def actions_plate(old, new):
    action = []

    
    mismatch_index = 0
    for i in range(min(len(old), len(new))):
        if old[i] != new[i]:
            break
        mismatch_index += 1

    
    for i in range(len(old) - 1, mismatch_index - 1, -1):
        removed = s.pop()
        action.append(f"PO:{int(removed) if removed == int(removed) else removed}")

    
    for i in range(mismatch_index, len(new)):
        s.push(new[i])
        action.append(f"PU:{int(new[i]) if new[i] == int(new[i]) else new[i]}")

    return ' '.join(action)



def print_bar(new,actions,w):
    dashes = '-' * (5 - len(new))
    plates = ''.join(f"[{int(i)}]" if i == int(i) else f"[{i}]" for i in new)
    reverse = ''.join(f"[{int(i)}]" if i == int(i) else f"[{i}]" for i in reversed(new))
    bar =  f"{dashes}{reverse}|======|{plates}{dashes}"

    has_float = any(isinstance(i,float) for i in new)

    if actions == '':
        if has_float:
            print(f"{bar} => {w:.1f} KG.")
        else:
            print(f"{bar} => {int(w)} KG.")    
    else:
        if has_float:
            print(f"{actions} => {bar} => {w:.1f} KG.")
        else:
            print(f"{actions} => {bar} => {int(w)} KG.") 


s = Stack()
weights = list(map(float, input("Enter needed weight(s): ").split()))
for w in weights:
    
    needs = (w - 20) / 2
    new_plate = fine_plate(needs)
    if new_plate is None:
        print(f"It's impossible to achieve the weight you want({int(w) if w == int(w) else w}).")
        break
    actions = actions_plate(s.item, new_plate)
    print_bar(new_plate,actions,w)