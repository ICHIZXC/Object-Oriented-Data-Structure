def Combination(input_list, answer=[]):
    if not input_list:
        return [answer] if answer else []

    choose = Combination(input_list[1:], answer + [input_list[0]])
    skip = Combination(input_list[1:], answer)

    return choose + skip


inp = list(map(int, input("Enter Input: ").split()))
print("Output:", Combination(inp))