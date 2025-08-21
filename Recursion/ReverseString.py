def reverse(n: str):
    if len(n) == 0:
        return n
    return reverse(n[1:]) + n[0]
    
print(reverse("Hello"))