inp = input("Enter Input : ").split('/')
data = []
for team in inp:
    parts = team.split(',')
    name = parts[0]
    win, draw, sc, cc = parts[1], parts[3], parts[4], parts[5]
    score = 3*int(win) + 1*int(draw)
    gd = int(sc) - int(cc)
    data.append([name, score, gd])

# print(data)
n = len(data)
for i in range(n):
    for j in range(n-i-1):
        if data[j][1] < data[j+1][1]:
            data[j], data[j+1] = data[j+1], data[j]
        elif data[j][1] == data[j+1][1]:
            if data[j][2] < data[j+1][2]:
                data[j], data[j+1] = data[j+1], data[j]
# print(data)
print("== results ==")
for i in data:
    print(f"['{i[0]}', {{'points': {i[1]}}}, {{'gd': {i[2]}}}]")

