class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def search(self, k):
        x = self.head
        while x and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        self.size = self.size + 1
        x.next = self.head
        if self.head:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        self.size = self.size - 1
        if x.prev:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next:
            x.next.prev = x.prev

    def extract(self, x):
        self.delete(x)
        return x


class LinkedListNode(object):
    def __init__(self, element):
        self.key = element
        self.prev = None
        self.next = None
