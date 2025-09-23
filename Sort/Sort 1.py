def check_sort(s):
    for i in range(len(s) - 1):
        if s[i+1] < s[i]:
            return "No"
    return "Yes"
        
inp = list(map(int, input("Enter Input : ").split()))
print(check_sort(inp))
