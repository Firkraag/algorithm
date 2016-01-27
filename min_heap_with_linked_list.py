from linked_list import linked_list_node, linked_list

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
        if (l <= (self.heap_size - 1)) and (self[l].key < self[i].key):
            smallest = l
        else:
            smallest = i
        if (r <= (self.heap_size - 1)) and (self[r].key < self[smallest].key):
            smallest = r
        if     smallest != i:
            self[i],self[smallest] = self[smallest],self[i]
            self.min_heapify(smallest)
    def build_min_heap(self):
        self.heap_size = self.length
        for i in range(self.length / 2 - 1, -1, -1):
            self.min_heapify(i)
class min_priority_queue(min_heap):
    def heap_minimum(self):
        return self[0].head
    def heap_extract_min(self):
        if self.heap_size < 1:
            sys.exit("heap underflow")
        minimum = self[0].extract(self[0].head)
        if self[0].empty():
            self[0] = self[self.heap_size - 1]
            self.heap_size = self.heap_size - 1
            self.min_heapify(0)
        return minimum
    def heap_decrease_key(self, i, element, key):
        if key > self[i]:
            sys.exit("new key is larger than current key")
        self[i] = key
        while i > 0 and self[self.parent(i)] > self[i]:
            tmp = self[self.parent(i)]
            self[self.parent(i)] = self[i]
            self[i] = tmp    
            i = self.parent(i)
    def min_heap_insert(self, key):
        if self.heap_size >= self.length:
            sys.exit("heap overflow")
        self.heap_size = self.heap_size + 1
        self[self.heap_size - 1] = float("Inf")
        self.heap_decrease_key(self.heap_size - 1, key)
