inp, op = input("***Fun with Word***\nEnter Input : ").split('/')
my_list = inp.split()
if op == 'W':
    w = []
    for i in my_list:
        w.append([i])
        
    index = 0
    for i in my_list:
        weight = 0
        for j in i:
            weight += ord(j.lower()) - 96
        w[index].append(weight)
        index += 1
    
    for i in range(len(w)):
        for j in range(len(w) - i -1):
            if w[j][1] >= w[j+1][1]:
                w[j], w[j+1] = w[j+1], w[j]
    
    # print(w)
    ans = []
    for i in w:
        ans.append(i[0])
    
    print(" ".join(ans))
    
elif op == "V":
    v = []
    for i in my_list:
        v.append([i])
    
    index = 0
    for i in my_list:
        vowel = 0
        for j in i:
            if j in "aeiou":
                vowel += 1
        v[index].append(vowel)
        index += 1
        
    order = {"a": 5, "e": 4, "i": 3, "o": 2, "u": 1}

    for i in range(len(v)):
        for j in range(len(v) - i -1):
            if v[j][1] > v[j+1][1]:
                v[j], v[j+1] = v[j+1], v[j]
            elif v[j][1] == v[j+1][1]:
                best1 = max([order[ch] for ch in v[j][0] if ch in order], default=0)
                best2 = max([order[ch] for ch in v[j+1][0] if ch in order], default=0)
                if best1 < best2:
                    v[j], v[j+1] = v[j+1], v[j]

    ans = []
    for i in v:
        ans.append(i[0])
    
    print(" ".join(ans))