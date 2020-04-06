#!/usr/bin/env ipython

import unittest
from contains import contains


class TestContains(unittest.TestCase):
    def test_contains(self):
        x = [1, 1.5, 3.5, 2.3, 10.01]
        self.assertEqual(contains(x, 5), {(1, 2), (2.3, 3.3), (3.5, 4.5), (10.01, 11.01)})
        x = [3.5, 5.2, -1.1, -4, -12, -11.33]
        self.assertEqual(contains(x, 6), {(-12, -11), (-4, -3), (-1.1, -0.10000000000000009), (3.5, 4.5), (5.2, 6.2)})
