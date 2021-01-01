import unittest

from linkedlist import LinkedList, LinkedListNode
from min_heap_with_linked_list import MinHeap, MinPriorityQueue


class TestHeap(unittest.TestCase):
    def test_min_heapify(self):
        L1 = LinkedList(1)
        L2 = LinkedList(2)
        L2.insert(LinkedListNode(2))
        L2.insert(LinkedListNode(2))
        L3 = LinkedList(3)
        L3.insert(LinkedListNode(3))
        L3.insert(LinkedListNode(3))
        L4 = LinkedList(4)
        L4.insert(LinkedListNode(4))
        L5 = LinkedList(5)
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        h = MinHeap([L5, L1, L2, L3, L4])
        h.min_heapify(0)
        self.assertEqual(h, [L1, L3, L2, L5, L4])

    def test_build_min_heap(self):
        L1 = LinkedList(1)
        L2 = LinkedList(2)
        L2.insert(LinkedListNode(2))
        L2.insert(LinkedListNode(2))
        L3 = LinkedList(3)
        L3.insert(LinkedListNode(3))
        L3.insert(LinkedListNode(3))
        L4 = LinkedList(4)
        L4.insert(LinkedListNode(4))
        L5 = LinkedList(5)
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        h = MinHeap([L3, L4, L5, L2, L1])
        h.build_min_heap()
        self.assertEqual(h, [L1, L2, L5, L3, L4])

    def test_heap_minimum(self):
        L1 = LinkedList(1)
        L1.insert(LinkedListNode(1))
        L1.insert(LinkedListNode(1))
        L2 = LinkedList(2)
        L2.insert(LinkedListNode(2))
        L2.insert(LinkedListNode(2))
        L3 = LinkedList(3)
        L3.insert(LinkedListNode(3))
        L3.insert(LinkedListNode(3))
        L4 = LinkedList(4)
        L4.insert(LinkedListNode(4))
        L5 = LinkedList(5)
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        q = MinPriorityQueue([L1, L2, L3, L4, L5])
        self.assertEqual(q.heap_minimum().key, 1)

    def test_heap_extract_min(self):
        L1 = LinkedList(1)
        L1.insert(LinkedListNode(1))
        L1.insert(LinkedListNode(1))
        L2 = LinkedList(2)
        L2.insert(LinkedListNode(2))
        L2.insert(LinkedListNode(2))
        L3 = LinkedList(3)
        L3.insert(LinkedListNode(3))
        L3.insert(LinkedListNode(3))
        L4 = LinkedList(4)
        L4.insert(LinkedListNode(4))
        L5 = LinkedList(5)
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        L3.insert(LinkedListNode(5))
        q = MinPriorityQueue([L1, L2, L3, L4, L5])
        self.assertEqual(q.heap_extract_min().key, 1)
        self.assertEqual(q, [L1, L2, L3, L4, L5])
        self.assertEqual(q.heap_extract_min().key, 1)
        self.assertEqual(q, [L2, L4, L3, L5, L5])
#    def test_heap_decrease_key(self):
#        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
#        q = min_priority_queue(a)
#        q.heap_decrease_key(8, 1)
#        self.assertEqual(q, [1, 1, 3, 2, 7, 8, 9, 10, 4, 16])
#    def test_heap_insert(self):
#        a = [1, 10, 3, 2, 7, 8, 9, 4, 14, 16]
#        q = min_priority_queue(a)
#        q.heap_extract_min()
#        q.min_heap_insert(0)
#        self.assertEqual(q, [0, 2, 3, 10, 4, 8, 9, 16, 14, 7])
