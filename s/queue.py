class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):#add
        self.items.insert(0,item)

    def dequeue(self):#pop
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]