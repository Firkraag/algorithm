#!/usr/bin/env python

import unittest
import disjoint_sets_forest as ds


class TestDisjointSets(unittest.TestCase):
    def test_forest(self):
        pool = [0] * 17
        for i in range(1, 17):
            pool[i] = ds.node(i)
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[i])
        for i in range(1, 16, 2):
            pool[i].union(pool[i + 1])
        parent_list = [2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[parent_list[i - 1]])
        for i in range(1, 14, 4):
            pool[i].union(pool[i + 2])
        parent_list = [2, 4, 4, 4, 6, 8, 8, 8, 10, 12, 12, 12, 14, 16, 16, 16]
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[parent_list[i - 1]])
        pool[1].union(pool[5])
        parent_list = [4, 4, 4, 8, 8, 8, 8, 8, 10, 12, 12, 12, 14, 16, 16, 16]
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[parent_list[i - 1]])
        pool[11].union(pool[13])
        parent_list = [4, 4, 4, 8, 8, 8, 8, 8, 10, 12, 12, 16, 16, 16, 16, 16]
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[parent_list[i - 1]])
        pool[1].union(pool[10])
        parent_list = [8, 4, 4, 8, 8, 8, 8, 16, 10, 16, 12, 16, 16, 16, 16, 16]
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[parent_list[i - 1]])
        self.assertTrue(pool[2].find_set() == pool[16])
        parent_list = [8, 16, 4, 16, 8, 8, 8,
                       16, 10, 16, 12, 16, 16, 16, 16, 16]
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[parent_list[i - 1]])
        self.assertTrue(pool[9].find_set() == pool[16])
        parent_list = [8, 16, 4, 16, 8, 8, 8,
                       16, 16, 16, 12, 16, 16, 16, 16, 16]
        for i in range(1, 17):
            self.assertEqual(pool[i].p, pool[parent_list[i - 1]])
