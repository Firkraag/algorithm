import unittest
import random
from two_sum import two_sum


class TestInsertionSort(unittest.TestCase):
    def test_two_sum(self):
        for _ in range(1000):
            array = [random.randint(1, 20) for _ in range(10)]
            x = random.randint(1, 100)
            n = len(array)
            result = False
            for i in range(n):
                for j in range(i + 1, n):
                    if array[i] + array[j] == x:
                        result = True
            self.assertEqual(two_sum(x, array), result)
