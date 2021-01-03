import unittest
from counting_sort import counting_sort


class TestHeap(unittest.TestCase):
    def test_counting_sort(self):
        A = [2, 5, 3, 0, 2, 3, 0, 3]
        B = []
        for i in range(len(A)):
            B.append(0)
        counting_sort(A, B, 5)
        self.assertEqual(B, [0, 0, 2, 2, 3, 3, 3, 5])
        self.assertEqual(A, [2, 5, 3, 0, 2, 3, 0, 3])
