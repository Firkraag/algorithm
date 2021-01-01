class FullException(Exception):
    pass


class EmptyException(Exception):
    pass


class Stack(list):
    def __init__(self, size):
        super(Stack, self).__init__([None] * size)
        self.top = -1
        self.size = len(size)

    def push(self, x):
        if self.full():
            raise FullException("This stack is full")
        else:
            self.top = self.top + 1
            self[self.top] = x

    def pop(self, *args, **kwargs):
        if self.empty():
            raise EmptyException('This stack is empty')
        else:
            self.top = self.top - 1
            return self[self.top + 1]

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top == self.size - 1

#    def multipop(self, k):
#        l = []
#        while not self.empty() and k > 0:
#
#            l.append(self.pop())
#        return l
