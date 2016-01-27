import unittest
from heap import max_heap, min_heap

class TestHeap(unittest.TestCase):
#    def test_init(self):
#        a = heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
#        self.assertEquals(a.__heap, a)
#        self.assertEquals(a.__length, 10)
#        self.assertEquals(a.__heap_size, 10)
    def test_max_heapify(self):
        a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        h = max_heap(a)
        h.max_heapify(1)
        self.assertEquals(h, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    def test_build_max_heap(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = max_heap(a)
        h.build_max_heap()
        self.assertEquals(h, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
    def test_heapsort(self):
        a = [4, 1, 3, 3, 16, 9, 10, 14, 8, 7]
        h = max_heap(a)
        h.heapsort()
        self.assertEquals(h, [1, 3, 3, 4, 7, 8, 9, 10, 14, 16])
    def test_min_heapify(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        h = min_heap(a)
        h.min_heapify(1)
        self.assertEquals(h, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
    def test_build_min_heap(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        h = min_heap(a)
        h.build_min_heap()
        self.assertEquals(h, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
