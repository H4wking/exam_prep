from arrays import DynamicArray


class ColorStack:
    def __init__(self):
        self.items = DynamicArray()
        self.red = DynamicArray() # indexes of red elements
        self.blue = DynamicArray() # indexes of blue elements

    def isEmpty(self):
        return (len(self.items) == 0) and (len(self.red) == 0) and (len(self.blue) == 0)

    def red_isEmpty(self):
        return len(self.red) == 0

    def blue_isEmpty(self):
        return len(self.blue) == 0

    def push(self, item, color):
        if color == "red":
            self.red.append(len(self))
        elif color == "blue":
            self.blue.append(len(self))
        else:
            raise ValueError("The color of element must be red or blue!")

        self.items.append(item)
        if len(self.red) + len(self.blue) != len(self):
            raise Warning("Something went wrong: sum of lenghts of blue and red elments massives is not equal to stack length!")

    def red_push(self, item):
        self.push(item, "red")

    def blue_push(self, item):
        self.push(item, "blue")

    def pop(self):
        if len(self.red ) != 0:
            if self.red[-1] == len(self) - 1:
                return self.pop_red()
        elif len(self.blue) != 0:
            if self.blue[-1] == len(self) - 1:
                return self.pop_blue()
        else:
            raise Warning("Something went wrong: value of last element of red or blue massive is not equal to last index of items!")

    def pop_red(self):
        last_red = self.red.pop()
        return self.items.pop(last_red)

    def pop_blue(self):
        last_blue = self.blue.pop()
        return self.items.pop(last_blue)

    def __len__(self, color=None):
        return len(self.items)

    def len_red(self):
        return len(self.red)

    def len_blue(self):
        return len(self.blue)

    def peek(self):
        if self.red[-1] == len(self) - 1:
            color = "red"
        elif self.blue[-1] == len(self) - 1:
            color = "blue"
        else:
            raise  Warning("Something went wrong: value of last element of red or blue massive is not equal to last index of items!")
        return self.items[-1], color

    def peek_red(self):
        if self.red:
            return self.items[self.red[-1]]
        return None

    def peek_blue(self):
        if self.blue:
            return self.items[self.blue[-1]]
        return None


