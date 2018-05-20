#!/usr/bin/env ipython
import unittest
import random
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            merge_sort(array)
            self.assertEqual(array, sorted(array_copy))

