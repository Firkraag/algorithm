#!/usr/bin/env ipython
import unittest
import random
from binary_search import binary_search, bisect_left


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        for _ in range(100):
            array = sorted([random.randint(1, 10000) for _ in range(100)])
            target = random.randint(1, 10000)
            index = binary_search(target, array)
            if index == -1:
                self.assertNotIn(target, array)
            else:
                self.assertEqual(target, array[index])

    def test_bisect_left(self):
        for length in range(10):
            array = sorted([random.randint(1, 10) for _ in range(length)])
            target = random.randint(0, 15)
            index = bisect_left(array, target)
            self.assertTrue(all(val < target for val in array[:index]))
            self.assertTrue(all(val >= target for val in array[index:]))
