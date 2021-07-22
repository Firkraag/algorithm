import unittest
from partition import partition, partition2, partition3
from random_array import random_arrays


class TestPartition(unittest.TestCase):
    def test_partition(self):
        for array in random_arrays():
            pivot_index = partition(array, 0, len(array) - 1)
            pivot = array[pivot_index]
            self.assertTrue(all(array[i] <= pivot for i in range(pivot_index)) and all(
                array[i] > pivot for i in range(pivot_index + 1, len(array))))

    def test_partition2(self):
        a = [2, 8, 7, 1, 4, 5, 6, 4]
        partition2(a, 0, 7)
        self.assertEqual(a, [2, 1, 4, 4, 7, 5, 6, 8])

    def test_partition3(self):
        for array in random_arrays():
            pivot_index = partition3(array, 0, len(array) - 1)
            pivot = array[pivot_index]
            self.assertTrue(all(array[i] <= pivot for i in range(pivot_index)) and all(
                array[i] > pivot for i in range(pivot_index + 1, len(array))))
