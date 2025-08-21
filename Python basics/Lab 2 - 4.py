s = [int(x) for x in input("Enter Your List : ").split()]

l = []
if len(s) < 3:
    print("Array Input Length Must More Than 2")

else:
    for a in range(len(s)):
        for b in range(a + 1, len(s)):              
            for c in range(b + 1, len(s)):
                if s[a] + s[b] + s[c] == 0:
                    if [s[a], s[b], s[c]] not in l:            
                        l.append([s[a], s[b], s[c]])
    print(l)
    
    
def isValid( s: str) -> :
    """
    aslkrfjedklsjgdrkljthrektljyh
    """
    pass
    
    
    
isValid()   
    
