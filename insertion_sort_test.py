#!/usr/bin/env ipython
import unittest
import random
from insertion_sort import insertion_sort, insertion_sort_recursive


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            insertion_sort(array)
            self.assertEqual(array, sorted(array_copy))

    def test_insertion_sort_recursive(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            insertion_sort_recursive(array)
            self.assertEqual(array, sorted(array_copy))
