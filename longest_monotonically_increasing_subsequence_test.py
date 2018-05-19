#!/usr/bin/env python
# coding=utf-8
import unittest
from longest_monotonically_increasing_subsequence import longest_monotonically_increasing_subsequence


class TestLMIS(unittest.TestCase):
    def test_longest_monotonically_increasing_subsequence(self):
        X = [5, 4, 1, 3, 2]
        self.assertEqual(longest_monotonically_increasing_subsequence(X), 2)
        X = [1, 3, 4, 2, 5]
        self.assertEqual(longest_monotonically_increasing_subsequence(X), 4)
        X = [1, 3, 10, 5, 3, 4]
        self.assertEqual(longest_monotonically_increasing_subsequence(X), 3)
