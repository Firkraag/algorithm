#!/usr/bin/env python
# encoding: utf-8
import unittest
import random
from inversion import inversion_with_insertion_sort, inversion_with_merge_sort


class TestInversion(unittest.TestCase):
    def test_inversion_with_insertion_sort(self):
        for _ in range(100):
            array = [random.randint(0, 100) for _ in range(100)]
            expected_result = 0
            for i in range(len(array)):
                for j in range(i + 1, len(array)):
                    if array[i] > array[j]:
                        expected_result += 1
            self.assertEqual(inversion_with_insertion_sort(array), expected_result)

    def test_inversion_with_merge_sort(self):
        for _ in range(100):
            array = [random.randint(0, 100) for _ in range(100)]
            expected_result = 0
            for i in range(len(array)):
                for j in range(i + 1, len(array)):
                    if array[i] > array[j]:
                        expected_result += 1
            self.assertEqual(inversion_with_merge_sort(array), expected_result)
