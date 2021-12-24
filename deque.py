from Queue import Queue, FullException, EmptyException


class Deque(Queue):
    """
    whereas a Queue allows insertion at one end and deletion at the other end,
    a Deque(double-ended Queue) allows insertion and deletion at both ends
    """

    def __init__(self, size):
        super().__init__(size)

    def enqueue_tail(self, x):
        self.enqueue(x)

    def dequeue_head(self):
        return self.dequeue()

    def enqueue_head(self, x):
        if self.full():
            raise FullException()
        else:
            if self.head == 0:
                self.head = self.size - 1
            else:
                self.head = self.head - 1
            self.data[self.head] = x

    def dequeue_tail(self):
        if self.empty():
            raise EmptyException()
        else:
            if self.tail == 0:
                self.tail = self.size - 1
            else:
                self.tail = self.tail - 1

            return self.data[self.tail]
