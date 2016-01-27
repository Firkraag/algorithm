class max_heap(list):
    def __init__(self, data):
        list.__init__(self, data)
        self.length = len(data)
        self.heap_size = self.length
        self.build_max_heap()
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2
    def parent(self, i):
        return (i - 1) / 2
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= (self.heap_size - 1)) and (self[l] > self[i]):
            largest = l
        else:
            largest = i
        if (r <= (self.heap_size - 1)) and (self[r] > self[largest]):
            largest = r
        if     largest != i:
            self[i],self[largest] = self[largest],self[i]
            self.max_heapify(largest)
    def build_max_heap(self):
        self.heap_size = self.length
        for i in range(self.length / 2 - 1, -1, -1):
            self.max_heapify(i)
    def heapsort(self):
        self.build_max_heap()
        for i in range(self.length - 1, 0, -1):
            self[0],self[i] = self[i],self[0]
            self.heap_size = self.heap_size - 1
            self.max_heapify(0)
class min_heap(list):
    def __init__(self, data):
        list.__init__(self, data)
        self.length = len(data)
        self.heap_size = self.length
        self.build_min_heap()
    def __contains__(self, y):
        return y in self[0:self.heap_size]
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2
    def parent(self, i):
        return (i - 1) / 2
    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= (self.heap_size - 1)) and (self[l] < self[i]):
            smallest = l
        else:
            smallest = i
        if (r <= (self.heap_size - 1)) and (self[r] < self[smallest]):
            smallest = r
        if     smallest != i:
            self[i],self[smallest] = self[smallest],self[i]
            self.min_heapify(smallest)
    def build_min_heap(self):
        self.heap_size = self.length
        for i in range(self.length / 2 - 1, -1, -1):
            self.min_heapify(i)
