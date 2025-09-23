inp = input("Enter Input : ").split()
ml = []
for i in inp:
    if int(i) >= 0:
        ml.append(i)

def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if int(l[j]) > int(l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
                swap = True
        if not swap: break
bubble_sort(ml)

index = 0
for i in inp:
    if int(i) < 0:
        ml.insert(index, i)
    index += 1

print(" ".join(ml))