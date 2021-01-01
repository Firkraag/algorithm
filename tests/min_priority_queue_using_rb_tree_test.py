#!/usr/bin/env python
import unittest
from min_priority_queue_using_rb_tree import min_priority_queue
from rb_tree import rb_node


class TestMinPriorityQueue(unittest.TestCase):
    def test_extract_min(self):
        q = min_priority_queue([41, 38, 31, 12, 19, 9])
        self.assertEqual(q.heap_extract_min().key, 9)
        self.assertEqual(q.heap_extract_min().key, 12)
        self.assertEqual(q.heap_extract_min().key, 19)
        self.assertEqual(q.heap_extract_min().key, 31)
        self.assertEqual(q.heap_extract_min().key, 38)
        self.assertEqual(q.heap_extract_min().key, 41)

    def test_heap_decrease_key(self):
        q = min_priority_queue([41, 38, 31, 12, 19, 9])
        q.heap_decrease_key(q.iterative_tree_search(9), 5)
        q.heap_decrease_key(q.iterative_tree_search(38), 5)
        self.assertEqual(q.heap_extract_min().key, 5)
        self.assertEqual(q.heap_extract_min().key, 5)
        self.assertEqual(q.heap_extract_min().key, 12)
        self.assertEqual(q.heap_extract_min().key, 19)
        self.assertEqual(q.heap_extract_min().key, 31)
        self.assertEqual(q.heap_extract_min().key, 41)

    def test_heap_insert(self):
        q = min_priority_queue([41, 38, 31, 12, 19, 9])
        q.min_heap_insert(rb_node(5, None, None, None, 0))
        q.min_heap_insert(rb_node(38, None, None, None, 0))
        q.min_heap_insert(rb_node(50, None, None, None, 0))
        self.assertEqual(q.heap_extract_min().key, 5)
        self.assertEqual(q.heap_extract_min().key, 9)
        self.assertEqual(q.heap_extract_min().key, 12)
        self.assertEqual(q.heap_extract_min().key, 19)
        self.assertEqual(q.heap_extract_min().key, 31)
        self.assertEqual(q.heap_extract_min().key, 38)
        self.assertEqual(q.heap_extract_min().key, 38)
        self.assertEqual(q.heap_extract_min().key, 41)
        self.assertEqual(q.heap_extract_min().key, 50)


if __name__ == '__main__':
    unittest.main()
