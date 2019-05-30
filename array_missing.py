from arrays import Array
import random


class ArrayMissing:
    def __init__(self, size):
        self._size = size
        self.items = Array(size)
        items = []
        cho = list(range(1, size + 3))
        for i in range(size):
            item = random.choice(cho)
            cho.remove(item)
            items.append(item)
        items = sorted(items)
        for i in range(size):
            self.items[i] = items[i]

    def find_min_missing(self):
        for i in range(self._size):
            if i + 1 != self.items[i]:
                return i + 1
        return self._size + 1

    def __str__(self):
        s = ""
        for i in self.items:
            s += str(i) + " "
        return s


a = ArrayMissing(5)
print(a)
print(a.find_min_missing())




