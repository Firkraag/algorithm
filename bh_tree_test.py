#!/usr/bin/env ipython
import unittest
from bh_tree import bh_tree, bh_node


class TestRbTree(unittest.TestCase):
    def test_insert_one(self):
        T = bh_tree([41])
        self.wrap(T, 41, 1)

    def test_insert_two(self):
        T = bh_tree([41, 38])
        self.wrap(T, 41, 1)
        self.wrap(T, 38, 1)

    def test_insert_three(self):
        T = bh_tree([41, 38, 31])
        self.wrap(T, 38, 1)
        self.wrap(T, 31, 1)
        self.wrap(T, 41, 1)

    def test_insert_four(self):
        T = bh_tree([41, 38, 31, 12])
        self.wrap(T, 38, 2)
        self.wrap(T, 31, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 1)

    def test_insert_five(self):
        T = bh_tree([41, 38, 31, 12, 19])
        self.wrap(T, 38, 2)
        self.wrap(T, 19, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 1)
        self.wrap(T, 31, 1)

    def test_insert_six(self):
        T = bh_tree([41, 38, 31, 12, 19, 9])
        self.wrap(T, 38, 2)
        self.wrap(T, 19, 2)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 1)
        self.wrap(T, 31, 1)
        self.wrap(T, 9, 1)

    def test_delete_one(self):
        T = bh_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        self.wrap(T, 38, 2)
        self.wrap(T, 19, 2)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 1)
        self.wrap(T, 31, 1)

    def test_delete_two(self):
        T = bh_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        self.wrap(T, 38, 2)
        self.wrap(T, 19, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 31, 1)

    def test_delete_three(self):
        T = bh_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        self.wrap(T, 38, 2)
        self.wrap(T, 31, 1)
        self.wrap(T, 41, 1)

    def test_delete_four(self):
        T = bh_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        self.wrap(T, 38, 1)
        self.wrap(T, 41, 1)

    def test_delete_five(self):
        T = bh_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        self.wrap(T, 41, 1)

    def test_delete_six(self):
        T = bh_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        T.delete(T.iterative_tree_search(41))
        self.assertEqual(T.root, T.nil)

    def wrap(self, tree, node, bh):
        self.assertEqual(tree.iterative_tree_search(node).bh, bh)


if __name__ == '__main__':
    unittest.main()
