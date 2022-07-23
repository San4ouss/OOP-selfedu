class Morph:
    def __init__(self, *args):
        self.words = list(args)

    def add_word(self, word):
        self.words.append(word)

    def get_words(self):
        return tuple(self.words)

    def __eq__(self, other):
        if not isinstance(other, str):
            raise AttributeError("Правый или левый операнд должен иметь тип str")
        return other.lower() in self.words


mw1 = Morph("word1", "word2", "word")
# print(mw1 == "word")  # True, если объект mv1 содержит слово "word" (без учета регистра)
# print(mw1 != "word")  # True, если объект mv1 не содержит слово "word" (без учета регистра)

# print("word" == mw1)
# print("word" != mw1)

