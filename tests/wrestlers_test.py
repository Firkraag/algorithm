#!/usr/bin/env ipython
import unittest
from wrestlers import wrestlers


class TestWrestler(unittest.TestCase):
    def testBfs(self):
        wrestlersList = [1, 2, 3, 4, 5, 6, 7, 8]
        rivalriesList = [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6),
                         (5, 6), (5, 7), (5, 8), (6, 8), (7, 8)]
        self.assertEqual(wrestlers(wrestlersList, rivalriesList), False)
        rivalriesList = [(1, 2), (1, 3), (2, 4), (3, 5),
                         (3, 6), (5, 7), (5, 8), (6, 8), (7, 8)]
        self.assertEqual(wrestlers(wrestlersList, rivalriesList), False)
        rivalriesList = [(1, 2), (1, 3), (2, 4), (3, 5),
                         (3, 6), (5, 7), (5, 8), (6, 8)]
        self.assertEqual(wrestlers(wrestlersList, rivalriesList), True)
