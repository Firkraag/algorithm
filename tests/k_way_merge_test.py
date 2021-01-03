#!/usr/bin/env python
import unittest
import random
from k_way_merge import k_way_merge


class TestKWayMerge(unittest.TestCase):
    def test_k_way_merge(self):
        for j in range(10000):
            A = [random.randint(1, 10000) for _ in range(100)]
            lists = [None] * 10
            for i in range(10):
                lists[i] = A[10 * i: (i + 1) * 10]
                lists[i].sort()
            A.sort()
            self.assertEqual(k_way_merge(lists), A)
