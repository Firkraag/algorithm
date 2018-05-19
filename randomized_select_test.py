import unittest
from randomized_select import randomized_select


class TestRandSelect(unittest.TestCase):
    def test_randomize_select_distinct(self):
        a = [10, 11, 5, 3, 2, 6, 0, 8, 100, 50]
        self.assertEqual(randomized_select(a, 0, 9, 5), 6)

    def test_randomize_select_duplicate(self):
        a = [10, 11, 5, 8, 2, 6, 8, 8, 100, 50]
        self.assertEqual(randomized_select(a, 0, 9, 4), 8)
        self.assertEqual(randomized_select(a, 0, 9, 5), 8)
        self.assertEqual(randomized_select(a, 0, 9, 6), 8)
