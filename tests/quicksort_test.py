import unittest
from partition import partition, partition2, partition3
import random
from quicksort import quicksort, randomized_quicksort


class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        for i in range(100):
            A = [random.randint(1, 10000) for i in range(100)]
            B = A[:]
            quicksort(A, 0, len(A) - 1, partition)
            B.sort()
            self.assertEqual(A, B)
        for i in range(100):
            A = [random.randint(1, 10000) for i in range(100)]
            B = A[:]
            quicksort(A, 0, len(A) - 1, partition2)
            B.sort()
            self.assertEqual(A, B)
        for i in range(100):
            A = [random.randint(1, 10000) for i in range(100)]
            B = A[:]
            quicksort(A, 0, len(A) - 1, partition3)
            B.sort()
            self.assertEqual(A, B)

    def test_randomized_quicksort(self):
        for i in range(100):
            A = [random.randint(1, 10000) for i in range(100)]
            B = A[:]
            randomized_quicksort(A, 0, len(A) - 1)
            B.sort()
            self.assertEqual(A, B)
