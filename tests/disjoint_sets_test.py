#!/usr/bin/env ipython

import unittest
import disjoint_sets_linked_list as ds


class TestDisjointSets(unittest.TestCase):
    def test_linked_lists_with_head_and_tail(self):
        pool = [0] * 17
        for i in range(1, 17):
            pool[i] = ds.node(i)
            a = ds.header(pool[i])
            self.assertEqual(a.head, pool[i])
            self.assertEqual(a.tail, pool[i])
        for i in range(1, 16, 2):
            pool[i].union(pool[i + 1])
        for i in range(1, 14, 4):
            pool[i].union(pool[i + 2])
        pool[1].union(pool[5])
        pool[11].union(pool[13])
        pool[1].union(pool[10])
        self.assertTrue(pool[2].find_set() == pool[1])
        self.assertTrue(pool[9].find_set() == pool[1])

    def test_linked_lists_no_tail(self):
        pool = [0] * 17
        for i in range(1, 17):
            pool[i] = ds.node_notail(i)
            ds.header_notail(pool[i])
        for i in range(1, 16, 2):
            pool[i].union(pool[i + 1])
        for i in range(1, 14, 4):
            pool[i].union(pool[i + 2])
        pool[1].union(pool[5])
        pool[11].union(pool[13])
        pool[1].union(pool[10])
        self.assertTrue(pool[2].find_set() == pool[16])
        self.assertTrue(pool[9].find_set() == pool[16])
