import unittest
from partition import partition, partition2, partition3
import random
from quicksort import quicksort, randomized_quicksort


class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(100)]
            array_copy = array[:]
            quicksort(array, 0, len(array) - 1, partition)
            array_copy.sort()
            self.assertEqual(array, array_copy)
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(100)]
            array_copy = array[:]
            quicksort(array, 0, len(array) - 1, partition2)
            array_copy.sort()
            self.assertEqual(array, array_copy)
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(100)]
            array_copy = array[:]
            quicksort(array, 0, len(array) - 1, partition3)
            array_copy.sort()
            self.assertEqual(array, array_copy)

    def test_randomized_quicksort(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(100)]
            array_copy = array[:]
            randomized_quicksort(array, 0, len(array) - 1)
            array_copy.sort()
            self.assertEqual(array, array_copy)
