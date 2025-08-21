e, a = input("Enter Input : ").split("/")
stack = [int(i) for i in e.split() if i != '0']

print("\nstart")
print(stack)
print()

actions = a.split(",")

for i in actions:
    if i.startswith("spawn"):
        _, hp = i.split()
        if int(hp) == 0:
            continue
        stack.append(int(hp))
        print(f"spawn an enemy of {hp} HP")
        print(stack)
        print()
    
    elif i.startswith("dmg"):
        _, damage = i.split()
        dmg = int(damage)
        kill = 0
        while dmg > 0 and stack:
            if stack[-1] <= dmg:
                dmg -= stack[-1]
                stack.pop(-1)
                kill += 1
            else:
                stack[-1] -= dmg
                dmg = 0
        
        if int(damage) <= 0: print("Invalid number")
                
        else:
            print(f"deal {damage} damage, killed {kill} enemy")
            print(stack)
            print()
    
    if len(stack) == 0:
        print(">>>> Player Wins <<<<")