class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if self.game_over:
            return "\ngame over\n"

        if not self.words or word[0] == self.words[-1][-1] and word not in self.words:
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "\ngame over\n"

    def restart(self):
        self.words = []
        self.game_over = False
        return "\ngame restarted\n"


my_shiritori = Shiritori()

while not my_shiritori.game_over:
    word = input("Внесете збор: ")
    print(my_shiritori.play(word))

print("Играта заврши, зборовите се:")
print(my_shiritori.words)
print(my_shiritori.restart())
