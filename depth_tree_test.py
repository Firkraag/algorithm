#!/usr/bin/env ipython
import unittest
from depth_tree import depth_tree, depth_node


class TestRbtree(unittest.TestCase):
    def test_insert_one(self):
        T = depth_tree([41])
        self.wrap(T, 41, 0)
    def test_insert_two(self):
        T = depth_tree([41, 38])
        self.wrap(T, 41, 0)
        self.wrap(T, 38, 1)
    def test_insert_three(self):
        T = depth_tree([41, 38, 31])
        self.wrap(T, 38, 0)
        self.wrap(T, 31, 1)
        self.wrap(T, 41, 1)
    def test_insert_four(self):
        T = depth_tree([41, 38, 31, 12])
        self.wrap(T, 38, 0)
        self.wrap(T, 31, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 2)
    def test_insert_five(self):
        T = depth_tree([41, 38, 31, 12, 19])
        self.wrap(T, 38, 0)
        self.wrap(T, 19, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 2)
        self.wrap(T, 31, 2)
    def test_insert_six(self):
        T = depth_tree([41, 38, 31, 12, 19, 9])
        self.wrap(T, 38, 0)
        self.wrap(T, 19, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 2)
        self.wrap(T, 31, 2)
        self.wrap(T, 9, 3)
    def test_delete_one(self):
        T = depth_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        self.wrap(T, 38, 0)
        self.wrap(T, 19, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 12, 2)
        self.wrap(T, 31, 2)
    def test_delete_two(self):
        T = depth_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        self.wrap(T, 38, 0)
        self.wrap(T, 19, 1)
        self.wrap(T, 41, 1)
        self.wrap(T, 31, 2)
    def test_delete_three(self):
        T = depth_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        self.wrap(T, 38, 0)
        self.wrap(T, 31, 1)
        self.wrap(T, 41, 1)
    def test_delete_four(self):
        T = depth_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        self.wrap(T, 38, 0)
        self.wrap(T, 41, 1)
    def test_delete_five(self):
        T = depth_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        self.wrap(T, 41, 0)
    def test_delete_six(self):
        T = depth_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        T.delete(T.iterative_tree_search(41))
        self.assertEquals(T.nil.depth, -1)
    def wrap(self, tree, node, depth):
        self.assertEquals(tree.iterative_tree_search(node).depth, depth)
if __name__ == '__main__':
    unittest.main()
