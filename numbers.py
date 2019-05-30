class First:
    def __init__(self, *args):
        self._args = args
        self.evens = sorted([i for i in args if i % 2 == 0])
        self.odds = [i for i in args if i % 2 == 1]

    def __str__(self):
        return "{}(evens={}, odds={})".format(self.__class__.__name__, str(self.evens), str(self.odds))

    def __eq__(self, other):
        if not isinstance(other, First):
            return False
        return self.evens == other.evens

    def del_odds(self):
        self.odds = []

    def deleted_odds(self):
        new = First(*self._args)
        new.del_odds()
        return new


class Second(First):
    def __init__(self, f, l):
        super().__init__(*list(range(f, l+1)))
        self.f = f
        self.l = l

    def __str__(self):
        return "{}(evens={}, odds={})".format(self.__class__.__bases__[0].__name__, str(self.evens), str(self.odds))

    def transform(self, n):
        return Second(self.f + n, self.l + n)
