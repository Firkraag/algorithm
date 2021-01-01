#!/usr/bin/env python
# encoding: utf-8

import unittest
import random
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        for size in range(20):
            array = [random.randint(1, 10000) for _ in range(size)]
            sorted_array = sorted(array)
            selection_sort(array)
            self.assertEqual(array, sorted_array)
