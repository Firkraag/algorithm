class FullException(Exception):
    def __init__(self):
        Exception.__init__(self)


class EmptyException(Exception):
    def __init__(self):
        Exception.__init__(self)


class Queue:
    def __init__(self, size):
        self.data = [0] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if self.full():
            raise FullException()
        self.data[self.tail] = x
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        if self.empty():
            raise EmptyException()
        x = self.data[self.head]
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head = self.head + 1
        return x

    def empty(self):
        return self.tail == self.head

    def full(self):
        return (self.tail + 1) % self.size == self.head

    def capacity(self):
        return self.size - 1
