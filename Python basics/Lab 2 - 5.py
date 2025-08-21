def bon(w):
    max_count = 0
    max_c = ''
    for i in w:
        count = 0
        for c in w:
            if i == c:
                count += 1
        if count > max_count:
            max_count = count
            max_c = i
    return (ord(max_c) - 96) * 4

secretCode = input("Enter secret code : ")
print(bon(secretCode))