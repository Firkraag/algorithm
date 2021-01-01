import unittest
from heap import MaxHeap, MinHeap


class TestHeap(unittest.TestCase):
    #    def test_init(self):
    #        a = heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    #        self.assertEqual(a.__heap, a)
    #        self.assertEqual(a.__length, 10)
    #        self.assertEqual(a.__heap_size, 10)
    def test_max_heapify(self):
        a = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        h = MaxHeap(a)
        h.max_heapify(1)
        self.assertEqual(h, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_build_max_heap(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = MaxHeap(a)
        h.build_max_heap()
        self.assertEqual(h, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_heapsort(self):
        a = [4, 1, 3, 3, 16, 9, 10, 14, 8, 7]
        h = MaxHeap(a)
        h.heapsort()
        self.assertEqual(h, [1, 3, 3, 4, 7, 8, 9, 10, 14, 16])

    def test_min_heapify(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        h = MinHeap(a)
        h.min_heapify(1)
        self.assertEqual(h, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])

    def test_build_min_heap(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        h = MinHeap(a)
        h.build_min_heap()
        self.assertEqual(h, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
