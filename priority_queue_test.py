import unittest
from priority_queue import max_priority_queue, min_priority_queue


class TestMaxPriorityQueue(unittest.TestCase):
    def test_init(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        q = max_priority_queue(a)
        self.assertEqual(q, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_heap_maximum(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        self.assertEqual(max_priority_queue(a).heap_maximum(), 16)

    def test_heap_extract_max(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = max_priority_queue(a)
        self.assertEqual(h.heap_extract_max(), 16)
        self.assertEqual(h, [14, 8, 10, 4, 7, 9, 3, 2, 1, 1])

    def test_heap_increase_key(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = max_priority_queue(a)
        h.heap_increase_key(8, 15)
        self.assertEqual(h, [16, 15, 10, 14, 7, 9, 3, 2, 8, 1])

    def test_heap_insert(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        queue = max_priority_queue(a)
        queue.heap_extract_max()
        queue.max_heap_insert(100)
        self.assertEqual(queue, [100, 14, 10, 4, 8, 9, 3, 2, 1, 7])

    def test_heap_delete(self):
        a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        h = max_priority_queue(a)
        h.heap_delete(4)
        self.assertEqual(h[0:h.heap_size], [16, 14, 10, 8, 1, 9, 3, 2, 4])
        h.heap_delete(2)
        self.assertEqual(h[0:h.heap_size], [16, 14, 9, 8, 1, 4, 3, 2])
        h.heap_delete(0)
        self.assertEqual(h[0:h.heap_size], [14, 8, 9, 2, 1, 4, 3])
        h.heap_delete(5)
        self.assertEqual(h[0:h.heap_size], [14, 8, 9, 2, 1, 3])
        h.heap_delete(3)
        self.assertEqual(h[0:h.heap_size], [14, 8, 9, 3, 1])
        h.heap_delete(1)
        self.assertEqual(h[0:h.heap_size], [14, 3, 9, 1])
        h.heap_delete(3)
        self.assertEqual(h[0:h.heap_size], [14, 3, 9])
        h.heap_delete(2)
        self.assertEqual(h[0:h.heap_size], [14, 3])
        h.heap_delete(1)
        self.assertEqual(h[0:h.heap_size], [14])
        h.heap_delete(0)
        self.assertEqual(h[0:h.heap_size], [])


class TestMinPriorityQueue(unittest.TestCase):
    def test_init(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        q = min_priority_queue(a)
        self.assertEqual(q, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])

    def test_heap_minimum(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        self.assertEqual(min_priority_queue(a).heap_minimum(), 1)

    def test_heap_extract_min(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        q = min_priority_queue(a)
        self.assertEqual(q.heap_extract_min(), 1)
        self.assertEqual(q, [2, 4, 3, 10, 7, 8, 9, 16, 14, 16])

    def test_heap_decrease_key(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        q = min_priority_queue(a)
        q.heap_decrease_key(8, 1)
        self.assertEqual(q, [1, 1, 3, 2, 7, 8, 9, 10, 4, 16])

    def test_heap_insert(self):
        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
        q = min_priority_queue(a)
        q.heap_extract_min()
        q.min_heap_insert(0)
        self.assertEqual(q, [0, 2, 3, 10, 4, 8, 9, 16, 14, 7])
