#!/usr/bin/env ipython
import unittest
import random
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        for _ in range(100):
            array = sorted([random.randint(1, 10000) for _ in range(0, 100)])
            target = random.randint(1, 10000)
            index = binary_search(target, array)
            if index == -1:
                self.assertNotIn(target, array)
            else:
                self.assertEqual(target, array[index])
