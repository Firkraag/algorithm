#!/usr/bin/env python
import unittest
import random
from merge_sort import merge_sort, merge_with_sentinel, merge_without_sentinel, merge_ins_sort_bottom_to_top, merge_ins_sort_top_to_bottom


class TestMergeSort(unittest.TestCase):
    def test_merge_sort_with_sentinel(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            merge_sort(array, merge_with_sentinel)
            self.assertEqual(array, sorted(array_copy))

    def test_merge_sort_without_sentinel(self):
        for _ in range(100):
            array = [random.randint(1, 10000) for _ in range(0, 100)]
            array_copy = array[:]
            merge_sort(array, merge_without_sentinel)
            self.assertEqual(array, sorted(array_copy))

    def test_merge_ins_sort(self):
        for length in range(100, 200):
            array = [random.randint(1, 10000) for _ in range(length)]
            array_copy = array[:]
            merge_ins_sort_bottom_to_top(array, partition=1)
            self.assertEqual(array, sorted(array_copy))
        for length in range(100, 200):
            array = [random.randint(1, 10000) for _ in range(length)]
            array_copy = array[:]
            merge_ins_sort_top_to_bottom(array, sublist_length=15)
            self.assertEqual(array, sorted(array_copy))
