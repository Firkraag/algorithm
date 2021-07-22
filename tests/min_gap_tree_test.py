#!/usr/bin/env python
import unittest
from min_gap_tree import MinGapTree, MinGapNode


class TestMinGapTree(unittest.TestCase):
    def test_insert_one(self):
        T = MinGapTree([50])
        self.wrap(T, 50, float("Inf"))

    def test_insert_two(self):
        T = MinGapTree([50, 38])
        self.wrap(T, 50, 12)
        self.wrap(T, 38, 12)

    def test_insert_three(self):
        T = MinGapTree([50, 38, 31])
        self.wrap(T, 38, 7)
        self.wrap(T, 31, 7)
        self.wrap(T, 50, float("Inf"))

    def test_insert_four(self):
        T = MinGapTree([50, 38, 31, 12])
        self.wrap(T, 38, 7)
        self.wrap(T, 31, 7)
        self.wrap(T, 50, float("Inf"))
        self.wrap(T, 12, 19)

    def test_insert_five(self):
        T = MinGapTree([50, 38, 31, 12, 19])
        self.wrap(T, 38, 7)
        self.wrap(T, 19, 7)
        self.wrap(T, 50, float("Inf"))
        self.wrap(T, 12, 7)
        self.wrap(T, 31, 7)

    def test_insert_six(self):
        T = MinGapTree([50, 38, 31, 12, 19, 9])
        self.wrap(T, 38, 3)
        self.wrap(T, 19, 3)
        self.wrap(T, 50, float("Inf"))
        self.wrap(T, 12, 3)
        self.wrap(T, 31, 7)
        self.wrap(T, 9, 3)

    def test_delete_one(self):
        T = MinGapTree([50, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        self.wrap(T, 38, 7)
        self.wrap(T, 19, 7)
        self.wrap(T, 50, float("Inf"))
        self.wrap(T, 12, 7)
        self.wrap(T, 31, 7)

    def test_delete_two(self):
        T = MinGapTree([50, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        self.wrap(T, 38, 7)
        self.wrap(T, 19, 7)
        self.wrap(T, 50, float("Inf"))
        self.wrap(T, 31, 7)

    def test_delete_three(self):
        T = MinGapTree([50, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        self.wrap(T, 38, 7)
        self.wrap(T, 31, 7)
        self.wrap(T, 50, float("Inf"))

    def test_delete_four(self):
        T = MinGapTree([50, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        self.wrap(T, 38, 12)
        self.wrap(T, 50, float("Inf"))

    def test_delete_five(self):
        T = MinGapTree([50, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        self.wrap(T, 50, float("Inf"))

    def test_delete_six(self):
        T = MinGapTree([50, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        T.delete(T.iterative_tree_search(50))
        self.assertEqual(T.root, T.nil)

    def wrap(self, tree, node, min_gap):
        self.assertEqual(tree.iterative_tree_search(node).min_gap, min_gap)


if __name__ == '__main__':
    unittest.main()
