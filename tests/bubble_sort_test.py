#!/usr/bin/env ipython
import unittest
import random
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            bubble_sort(array)
            self.assertEqual(array, sorted(array_copy))
