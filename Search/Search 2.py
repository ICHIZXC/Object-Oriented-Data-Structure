print("This is your BOOK!!!")
inp = input("Enter input: ").split('/')
shelf = [i for i in inp[0].split()]
cashier = []
cost = 0
for i in inp[1].split():
    if i in shelf:
        index = shelf.index(i)
        cost += index + 1
        temp = shelf.pop(index)
        shelf.insert(0, temp)
        print(f"Search {i} -> found at {index + 1} move to front ->  {' '.join(shelf)}")
    elif i not in shelf and i not in cashier:
        cost += len(shelf) + 1
        cashier.append(i)
        print(f"Search {i} -> not found -> {' '.join(shelf)}")
    elif i in cashier:
        shelf.insert(0, i)
        cost += 1
        print(f"Search {i} -> add new book ->  {' '.join(shelf)}")
        
print(f"\nFinal books: {' '.join(shelf)}")
print(f"Total cost: {cost}")
