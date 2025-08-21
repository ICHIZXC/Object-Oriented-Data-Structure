n = int(input("*** Fun with Drawing ***\nEnter input : "))

size = 5 + (4 * (n - 2))
for i in range(size):
    for j in range(size):
        if min(i, j, size - i - 1, size - j - 1) % 2 == 0:
            print("#", end = '')
        else: print(".", end = '')
    print("")
    