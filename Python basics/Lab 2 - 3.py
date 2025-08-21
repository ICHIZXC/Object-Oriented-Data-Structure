class TorKham:
    def __init__(self):
        self.words = []

    def restart(self):
        self.words.clear()
        return "game restarted"

    def play(self, word):
        for w in self.words:
            if w.lower() == word.lower():
                return "game over"
        
        if not self.words:
            self.words.append(word)
            return f"'{word}' -> {self.words}"
        
        last = self.words[-1]
        if last[-2:].lower() == word[0:2].lower():
            self.words.append(word)
            return f"'{word}' -> {self.words}"
        else: return f"'{word}' -> game over"

torkham = TorKham()

print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')

for i in S:
    if i == 'X':
        break
    
    elif i == 'R':
        print(torkham.restart())
        
    elif i.startswith("P "):
        w = i.split(" ")
        word = w[1]
        print(torkham.play(word))

    else:
        print(f"'{i}' is Invalid Input !!!")
        break
