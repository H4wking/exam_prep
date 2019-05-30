class First:
    def __init__(self, word):
        self.word = word
        self.consonants = [letter for letter in word if letter not in ["e", "y", "u", "i", "o", "a"]]
        self.vowels = [letter for letter in word if letter in ["e", "y", "u", "i", "o", "a"]]

    def __str__(self):
        return "{}(consonants={}, vowels={})".format(self.__class__.__name__, self.consonants, self.vowels)

    def __eq__(self, other):
        if not isinstance(other, First):
            return False
        return self.consonants == other.consonants

    def clear_vowels(self):
        self.vowels = []

    def cleared_vowels(self):
        new = First(self.word)
        new.clear_vowels()
        return new


class Second(First):
    def __init__(self, word, shift):
        super().__init__(word)
        self.shift = shift

    def encoder(self):
        new_word = ""
        for letter in self.word:
            if letter not in ["e", "y", "u", "i", "o", "a"]:
                new_word += chr(ord(letter) + self.shift)
        for letter in self.word:
            if letter in ["e", "y", "u", "i", "o", "a"]:
                new_word += chr(ord(letter) + self.shift)
        return Second(new_word, self.shift)

    def __str__(self):
        return "{}(consonants={}, vowels={})".format(self.__class__.__bases__[0].__name__, self.consonants, self.vowels)

