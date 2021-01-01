#!/usr/bin/env python
import unittest
import random
from insertion_sort import insertion_sort, insertion_sort_recursive, insert_with_linear_search, \
    insert_with_binary_search


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_with_linear_search(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            insertion_sort(array, insert_method=insert_with_linear_search)
            self.assertEqual(array, sorted(array_copy))

    def test_insertion_sort_with_binary_search(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            insertion_sort(array, insert_method=insert_with_binary_search)
            self.assertEqual(array, sorted(array_copy))

    def test_insertion_sort_recursive(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            insertion_sort_recursive(array)
            self.assertEqual(array, sorted(array_copy))
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            insertion_sort_recursive(
                array, insert_method=insert_with_binary_search)
            self.assertEqual(array, sorted(array_copy))
