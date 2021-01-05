#!/usr/bin/env python
import unittest
from k_way_merge import k_way_merge
from random_array import random_arrays


class TestKWayMerge(unittest.TestCase):
    def test_k_way_merge(self):
        for array in random_arrays():
            lists = []
            for i in range(10):
                lists.append(array[10 * i: (i + 1) * 10])
                lists[-1].sort()
            self.assertEqual(k_way_merge(lists), sorted(array))
