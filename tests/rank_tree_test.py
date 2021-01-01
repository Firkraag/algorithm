#!/usr/bin/env python
import unittest
from rank_tree import rank_tree, rank_node


class TestOstree(unittest.TestCase):
    def test_insert_one(self):
        T = rank_tree([41])
        print(T.root.iterative_tree_search(41).p.key)
        self.assertEqual(T.root, T.root.iterative_tree_search(41))
        self.assertEqual(T.nil.rank, 0)
        self.wrap(T, 41, -1, -1, -1, 1, 1)

    def test_insert_two(self):
        T = rank_tree([41, 38])
        self.assertEqual(T.root, T.iterative_tree_search(41))
        self.assertEqual(T.nil.rank, 0)
        self.wrap(T, 41, 38, -1, -1, 1, 2)
        self.wrap(T, 38, -1, -1, 41, 0, 1)

    def test_insert_three(self):
        T = rank_tree([41, 38, 31])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.rank, 0)
        self.wrap(T, 38, 31, 41, -1, 1, 2)
        self.wrap(T, 31, -1, -1, 38, 0, 1)
        self.wrap(T, 41, -1, -1, 38, 0, 3)

    def test_insert_four(self):
        T = rank_tree([41, 38, 31, 12])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.rank, 0)
        self.wrap(T, 38, 31, 41, -1, 1, 3)
        self.wrap(T, 31, 12, -1, 38, 1, 2)
        self.wrap(T, 41, -1, -1, 38, 1, 4)
        self.wrap(T, 12, -1, -1, 31, 0, 1)

    def test_insert_five(self):
        T = rank_tree([41, 38, 31, 12, 19])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.rank, 0)
        self.wrap(T, 38, 19, 41, -1, 1, 4)
        self.wrap(T, 19, 12, 31, 38, 1, 2)
        self.wrap(T, 41, -1, -1, 38, 1, 5)
        self.wrap(T, 12, -1, -1, 19, 0, 1)
        self.wrap(T, 31, -1, -1, 19, 0, 3)

    def test_insert_six(self):
        T = rank_tree([41, 38, 31, 12, 19, 9])
        self.assertEqual(T.root, T.iterative_tree_search(38))
        self.assertEqual(T.nil.rank, 0)
        self.wrap(T, 38, 19, 41, -1, 1, 5)
        self.wrap(T, 19, 12, 31, 38, 0, 3)
        self.wrap(T, 41, -1, -1, 38, 1, 6)
        self.wrap(T, 12, 9, -1, 19, 1, 2)
        self.wrap(T, 31, -1, -1, 19, 1, 4)
        self.wrap(T, 9, -1, -1, 12, 0, 1)

    def test_delete_one(self):
        T = rank_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        self.wrap(T, 38, 19, 41, -1, 1, 4)
        self.wrap(T, 19, 12, 31, 38, 0, 2)
        self.wrap(T, 41, -1, -1, 38, 1, 5)
        self.wrap(T, 12, -1, -1, 19, 1, 1)
        self.wrap(T, 31, -1, -1, 19, 1, 3)

    def test_delete_two(self):
        T = rank_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        self.wrap(T, 38, 19, 41, -1, 1, 3)
        self.wrap(T, 19, -1, 31, 38, 1, 1)
        self.wrap(T, 41, -1, -1, 38, 1, 4)
        self.wrap(T, 31, -1, -1, 19, 0, 2)

    def test_delete_three(self):
        T = rank_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        self.wrap(T, 38, 31, 41, -1, 1, 2)
        self.wrap(T, 31, -1, -1, 38, 1, 1)
        self.wrap(T, 41, -1, -1, 38, 1, 3)

    def test_delete_four(self):
        T = rank_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        self.wrap(T, 38, -1, 41, -1, 1, 1)
        self.wrap(T, 41, -1, -1, 38, 0, 2)

    def test_delete_five(self):
        T = rank_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        self.wrap(T, 41, -1, -1, -1, 1, 1)

    def test_delete_six(self):
        T = rank_tree([41, 38, 31, 12, 19, 9])
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        T.delete(T.iterative_tree_search(41))
        self.assertEqual(T.root, T.nil)
        self.assertEqual(T.nil.rank, 0)

    def wrap(self, tree, node, left, right, p, color, rank):
        self.assertEqual(tree.iterative_tree_search(
            node).left, tree.iterative_tree_search(left))
        self.assertEqual(tree.iterative_tree_search(
            node).right, tree.iterative_tree_search(right))
        self.assertEqual(tree.iterative_tree_search(
            node).p, tree.iterative_tree_search(p))
        self.assertEqual(tree.iterative_tree_search(node).color, color)
        self.assertEqual(tree.iterative_tree_search(node).rank, rank)


if __name__ == '__main__':
    unittest.main()
