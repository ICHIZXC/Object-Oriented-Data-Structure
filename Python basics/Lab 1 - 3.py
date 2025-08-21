# print("*** Election ***")

# n = int(input("Enter a number of voter(s) : "))
# v = list(map(int, input().split()))
# count = {}

# for i in v:
#     if i < 1 or i > 20: print("*** No Candidate Wins ***")
#     break
    
# for vote in v:
#     count[vote] = count.get(vote, 0) + 1

# winner = max(count.values())
# mode = [vote for vote, c in count.items() if c == winner]

# print(*mode)


n = int(input("*** Election ***\nEnter a number of voter(s) : "))
v = list(map(int, input().split()))

o  = [i for i in v if 1<=i<=20]

m=[[],[0]]
for i in o:
    if i not in m[1]:              
        if o.count(i) > o.count(m[1][0]):
            m[1]=[i]
        elif o.count(i) == o.count(m[1][0]):
            m[1].append(i)


print(" ".join(str(i) for i in sorted(m[1]))) if m[1] != [0] else print("*** No Candidate Wins ***")
        




    
