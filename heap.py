class MaxHeap(list):
    def __init__(self, data):
        super(MaxHeap, self).__init__(data)
        self.length = len(self)
        self.heap_size = self.length
        self.build_max_heap()

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if (left <= (self.heap_size - 1)) and (self[left] > self[i]):
            largest = left
        else:
            largest = i
        if (right <= (self.heap_size - 1)) and (self[right] > self[largest]):
            largest = right
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_size = self.length
        for i in range(self.length // 2 - 1, -1, -1):
            self.max_heapify(i)

    def heapsort(self):
        self.build_max_heap()
        for i in range(self.length - 1, 0, -1):
            self[0], self[i] = self[i], self[0]
            self.heap_size = self.heap_size - 1
            self.max_heapify(0)


class MinHeap(list):
    def __init__(self, data):
        super(MinHeap, self).__init__(data)
        self.length = len(self)
        self.heap_size = self.length
        self.build_min_heap()

    def __contains__(self, y):
        return y in self[:self.heap_size]

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= (self.heap_size - 1)) and (self[l] < self[i]):
            smallest = l
        else:
            smallest = i
        if (r <= (self.heap_size - 1)) and (self[r] < self[smallest]):
            smallest = r
        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self.min_heapify(smallest)

    def build_min_heap(self):
        self.heap_size = self.length
        for i in range(self.length // 2 - 1, -1, -1):
            self.min_heapify(i)
