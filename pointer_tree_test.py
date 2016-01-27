#!/usr/bin/env ipython
import unittest
from pointer_tree import pointer_tree, pointer_node


class TestOstree(unittest.TestCase):
    def test_insert_one(self):
        T = pointer_tree([41])
        self.wrap(T, 41, 41, 41, float("-Inf"), float("Inf"))
    def test_insert_two(self):
        T = pointer_tree([41, 38])
        self.wrap(T, 41, 38, 41, 38, float("Inf"))
        self.wrap(T, 38, 38, 38, float("-Inf"), 41)
    def test_insert_three(self):
        T = pointer_tree([41, 38, 31])
        self.wrap(T, 38, 31, 41, 31, 41)
        self.wrap(T, 31, 31, 31, float("-Inf"), 38)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
    def test_insert_four(self):
        T = pointer_tree([41, 38, 31, 12])
        self.wrap(T, 38, 12, 41, 31, 41)
        self.wrap(T, 31, 12, 31, 12, 38)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
        self.wrap(T, 12, 12, 12, float("-Inf"), 31)
    def test_insert_five(self):
        T = pointer_tree([41, 38, 31, 12, 19])
        self.wrap(T, 38, 12, 41, 31, 41)
        self.wrap(T, 19, 12, 31, 12, 31)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
        self.wrap(T, 12, 12, 12, float("-Inf"), 19)
        self.wrap(T, 31, 31, 31, 19, 38)
    def test_insert_six(self):
        T = pointer_tree([41, 38, 31, 12, 19, 9])
        self.wrap(T, 38, 9, 41, 31, 41)
        self.wrap(T, 19, 9, 31, 12, 31)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
        self.wrap(T, 12, 9, 12, 9, 19)
        self.wrap(T, 31, 31, 31, 19, 38)
        self.wrap(T, 9, 9, 9, float("-Inf"), 12)
    def test_delete_one(self):
        T = pointer_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        self.wrap(T, 38, 12, 41, 31, 41)
        self.wrap(T, 19, 12, 31, 12, 31)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
        self.wrap(T, 12, 12, 12, float("-Inf"), 19)
        self.wrap(T, 31, 31, 31, 19, 38)
    def test_delete_two(self):
        T = pointer_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        self.wrap(T, 38, 19, 41, 31, 41)
        self.wrap(T, 19, 19, 31, float("-Inf"), 31)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
        self.wrap(T, 31, 31, 31, 19, 38)
    def test_delete_three(self):
        T = pointer_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        self.wrap(T, 38, 31, 41, 31, 41)
        self.wrap(T, 31, 31, 31, float("-Inf"), 38)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
    def test_delete_four(self):
        T = pointer_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        self.wrap(T, 38, 38, 41, float("-Inf"), 41)
        self.wrap(T, 41, 41, 41, 38, float("Inf"))
    def test_delete_five(self):
        T = pointer_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        self.wrap(T, 41, 41, 41, float("-Inf"), float("Inf")) 
    def test_delete_six(self):
        T = pointer_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        T.delete(T.iterative_tree_search(41))
        self.assertEquals(T.root, T.nil)
    def wrap(self, tree, node, minimum, maximum, predecessor, successor):
        self.assertEquals(tree.iterative_tree_search(node).minimum.key, minimum)
        self.assertEquals(tree.iterative_tree_search(node).maximum.key, maximum)
        self.assertEquals(tree.iterative_tree_search(node).predecessor.key, predecessor)
        self.assertEquals(tree.iterative_tree_search(node).successor.key, successor)
if __name__ == '__main__':
    unittest.main()
