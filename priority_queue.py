import sys
from heap import MaxHeap, MinHeap


class MaxPriorityQueue(MaxHeap):
    def heap_maximum(self):
        return self[0]

    def heap_extract_max(self):
        if self.heap_size < 1:
            sys.exit("heap underflow")
        maximum = self[0]
        self[0] = self[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        self.max_heapify(0)
        return maximum

    def heap_increase_key(self, i, key):
        if key < self[i]:
            sys.exit("new key is smaller than current key")
        self[i] = key
        while i > 0 and self[self.parent(i)] < self[i]:
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            i = self.parent(i)

    def max_heap_insert(self, key):
        if self.heap_size >= self.length:
            sys.exit("heap overflow")
        self.heap_size = self.heap_size + 1
        self[self.heap_size - 1] = float("-Inf")
        self.heap_increase_key(self.heap_size - 1, key)

    def heap_delete(self, i):
        self.heap_increase_key(i, float("Inf"))
        self[0], self[self.heap_size - 1] = self[self.heap_size - 1], self[0]
        self.heap_size = self.heap_size - 1
        self.max_heapify(0)


class MinPriorityQueue(MinHeap):
    def heap_minimum(self):
        return self[0]

    def heap_extract_min(self):
        if self.heap_size < 1:
            sys.exit("heap underflow")
        minimum = self[0]
        self[0] = self[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return minimum

    def heap_decrease_key(self, i, key):
        if key > self[i]:
            sys.exit("new key is larger than current key")
        self[i] = key
        while i > 0 and self[self.parent(i)] > self[i]:
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            i = self.parent(i)

    def min_heap_insert(self, key):
        if self.heap_size >= self.length:
            sys.exit("heap overflow")
        self.heap_size = self.heap_size + 1
        self[self.heap_size - 1] = float("Inf")
        self.heap_decrease_key(self.heap_size - 1, key)
