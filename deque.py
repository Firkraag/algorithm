from Queue import Queue, FullException, EmptyException


def deque(Queue):
    """
    whereas a Queue allows insertion at one end and deletion at the other end, a deque(double-ended Queue allows insertion and deletion at both ends
    """

    def __init__(self, size):
        super(deque, self).__init__(size)

    def enqueue_tail(self, x):
        self.enqueue(x)

    def dequeue_head(self):
        return self.dequeue()

    def enqueue_head(self, x):
        if self.full():
            raise FullException("This double-ended Queue is full")
        else:
            if self.head == 0:
                self.head = self.length - 1
            else:
                self.head = self.head - 1
            self[self.head] = x

    def dequeue_tail(self):
        if self.emtpy():
            raise EmptyException("This double-ended Queue is empty")
        else:
            if self.tail == 0:
                self.tail = self.length - 1
            else:
                self.tail = self.tail - 1

            return self[self.tail]
