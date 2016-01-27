#!/usr/bin/env ipython
import unittest
from interval_tree import interval, interval_tree, interval_node


class TestIntervalTree(unittest.TestCase):
    def test_insert_one(self):
        intervals = []
        values = [16, 21, 8, 9, 25, 30, 5, 8, 15, 23, 17, 19, 26, 26, 0, 3, 6, 10, 19, 20]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        values = [16, 30, 8, 23, 25, 30, 5, 10, 15, 23, 17, 20, 26, 26, 0, 3, 6, 10, 19, 20]
        for i in range(0, len(values), 2):
            self.wrap(T, values[i], values[i + 1])
        values = [41, 41, 38, 42, 31, 35, 12, 45, 19, 23, 9, 21]
        intervals = []
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        values = [38, 45, 19, 45, 41, 41, 12, 45, 31, 35, 9, 21]
        for i in range(0, len(values), 2):
            self.wrap(T, values[i], values[i + 1])
    def test_delete_one(self):
        intervals = []
        values = [41, 41, 38, 42, 31, 35, 12, 45, 19, 23, 9, 21]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        T.delete(T.iterative_tree_search(9))
        values = [38, 45, 19, 45, 41, 41, 12, 45, 31, 35]
        for i in range(0, len(values), 2):
            self.wrap(T, values[i], values[i + 1])
    def test_delete_two(self):
        intervals = []
        values = [41, 41, 38, 42, 31, 35, 12, 45, 19, 23, 9, 21]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        values = [38, 42, 19, 35, 41, 41, 31, 35]
        for i in range(0, len(values), 2):
            self.wrap(T, values[i], values[i + 1])
    def test_delete_three(self):
        intervals = []
        values = [41, 41, 38, 42, 31, 35, 12, 45, 19, 23, 9, 21]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        values = [38, 42, 31, 35, 41, 41]
        for i in range(0, len(values), 2):
            self.wrap(T, values[i], values[i + 1])
    def test_delete_four(self):
        intervals = []
        values = [41, 41, 38, 42, 31, 35, 12, 45, 19, 23, 9, 21]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        values = [38, 42, 41, 41]
        for i in range(0, len(values), 2):
            self.wrap(T, values[i], values[i + 1])
    def test_delete_five(self):
        intervals = []
        values = [41, 41, 38, 42, 31, 35, 12, 45, 19, 23, 9, 21]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        values = [41, 41]
        for i in range(0, len(values), 2):
            self.wrap(T, values[i], values[i + 1])
    def test_delete_six(self):
        intervals = []
        values = [41, 41, 38, 42, 31, 35, 12, 45, 19, 23, 9, 21]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        T.delete(T.iterative_tree_search(9))
        T.delete(T.iterative_tree_search(12))
        T.delete(T.iterative_tree_search(19))
        T.delete(T.iterative_tree_search(31))
        T.delete(T.iterative_tree_search(38))
        T.delete(T.iterative_tree_search(41))
        self.assertEquals(T.nil.maximum, float("-Inf"))
    def wrap(self, tree, node, maximum):
        self.assertEquals(tree.iterative_tree_search(node).maximum, maximum)
if __name__ == '__main__':
    unittest.main()
