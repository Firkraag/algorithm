#!/usr/bin/env python
# encoding: utf-8

import unittest
from random_array import random_arrays
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        for array in random_arrays():
            sorted_array = sorted(array)
            selection_sort(array)
            self.assertEqual(array, sorted_array)
