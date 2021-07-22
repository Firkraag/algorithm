import unittest
from random_array import random_arrays
import random
from two_sum import two_sum


class TestInsertionSort(unittest.TestCase):
    def test_two_sum(self):
        for array in random_arrays(array_num=1000, array_size=10, array_lowerbound=1, array_upperbound=20):
            x = random.randint(1, 100)
            n = len(array)
            result = False
            for i in range(n):
                for j in range(i + 1, n):
                    if array[i] + array[j] == x:
                        result = True
            self.assertEqual(two_sum(x, array), result)
