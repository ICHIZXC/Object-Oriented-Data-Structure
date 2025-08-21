max_car, cars, op, car = input("******** Parking Lot ********\nEnter max of car,car in soi,operation : ").split()

stack = [] if cars == '0' else [int(x) for x in cars.split(',')]

c = int(car)
    
if op.startswith("arrive"):
    if len(stack) == int(max_car):
        print(f"car {c} cannot arrive : Soi Full")
    else:
        if c not in stack:
            stack.append(c)
            print(f"car {c} arrive! : Add Car {c}")    
        else:
            print(f"car {c} already in soi")

elif op.startswith("depart"):
    if not stack:
        print(f"car {c} cannot depart : Soi Empty")
    else:
        if c in stack:
            stack.remove(c)
            print(f"car {c} depart ! : Car {c} was remove")
        else:
            print(f"car {c} cannot depart : Dont Have Car {c}")

print(stack)