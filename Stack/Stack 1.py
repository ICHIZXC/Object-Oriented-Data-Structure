l = list(int(x) for x in input("***Always 5 or 10***\nEnter Input : ").split())
s = []

if l:
    s.append(l[0])

    for i in range(1, len(l)):
        top = s[-1]
        if abs(top + l[i]) in [5, 10] or abs(top - l[i]) in [5, 10]:
            s.append(l[i])

print("Output :", *s)