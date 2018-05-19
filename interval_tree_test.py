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
        self.assertEqual(T.nil.maximum, float("-Inf"))

    def test_interval_search(self):
        intervals = []
        values = [41, 41, 38, 52, 43, 48]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        i = interval(50, 51)
        t = T.closed_interval_search(i)
        self.assertEqual(T.root.left, t)
        i = interval(58, 60)
        t = T.closed_interval_search(i)
        self.assertEqual(T.nil, t)
        i = interval(38, 48)
        t = T.closed_interval_search(i)
        self.assertEqual(T.root, t)

    def test_interval_search_minimum_low_end(self):
        intervals = []
        values = [41, 41, 38, 52, 43, 48]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        i = interval(22, 51)
        t = T.closed_interval_search_minimum_low_end(i)
        self.assertEqual(T.root.left, t)
        i = interval(58, 60)
        t = T.closed_interval_search_minimum_low_end(i)
        self.assertEqual(T.nil, t)
        i = interval(38, 48)
        t = T.closed_interval_search_minimum_low_end(i)
        self.assertEqual(T.root.left, t)

    def test_list_all_overlapping_intervals(self):
        intervals = []
        values = [41, 41, 38, 52, 43, 48]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        i = interval(22, 51)
        t = T.list_all_overlapping_intervals(i)
        i = interval(58, 60)
        t = T.list_all_overlapping_intervals(i)
        i = interval(38, 48)
        t = T.list_all_overlapping_intervals(i)
        i = interval(38, 41)
        t = T.list_all_overlapping_intervals(i)
        i = interval(42, 42)
        t = T.list_all_overlapping_intervals(i)

    def test_interval_search_exactly(self):
        intervals = []
        values = [41, 41, 38, 52, 43, 48]
        for i in range(0, len(values), 2):
            intervals.append(interval(values[i], values[i + 1]))
        T = interval_tree(intervals)
        i = interval(22, 51)
        t = T.interval_search_exactly(i)
        self.assertEqual(t, T.nil)
        i = interval(41, 41)
        t = T.interval_search_exactly(i)
        self.assertEqual(t, T.root)
        i = interval(38, 52)
        t = T.interval_search_exactly(i)
        self.assertEqual(t, T.root.left)
        i = interval(43, 48)
        t = T.interval_search_exactly(i)
        self.assertEqual(t, T.root.right)
        i = interval(43, 49)
        t = T.interval_search_exactly(i)
        self.assertEqual(t, T.nil)
        i = interval(20, 50)
        t = T.interval_search_exactly(i)
        self.assertEqual(t, T.nil)
        i = interval(39, 41)
        t = T.interval_search_exactly(i)
        self.assertEqual(t, T.nil)

    def wrap(self, tree, node, maximum):
        self.assertEqual(tree.iterative_tree_search(node).maximum, maximum)


if __name__ == '__main__':
    unittest.main()
