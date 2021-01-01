import unittest
from linkedlist import LinkedList, LinkedListNode


class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        L = LinkedList()
        a = LinkedListNode(1)
        b = LinkedListNode(4)
        c = LinkedListNode(16)
        d = LinkedListNode(9)
        e = LinkedListNode(25)
        L.insert(a)
        L.insert(b)
        L.insert(c)
        L.insert(d)
        L.insert(e)
        l = []
        x = L.head
        while x:
            l.append(x)
            x = x.next
        self.assertEqual(l, [e, d, c, b, a])

    def test_search(self):
        L = LinkedList()
        a = LinkedListNode(1)
        b = LinkedListNode(4)
        c = LinkedListNode(16)
        d = LinkedListNode(9)
        e = LinkedListNode(25)
        L.insert(a)
        L.insert(b)
        L.insert(c)
        L.insert(d)
        L.insert(e)
        self.assertEqual(L.search(4), b)

    def test_delete(self):
        L = LinkedList()
        a = LinkedListNode(1)
        b = LinkedListNode(4)
        c = LinkedListNode(16)
        d = LinkedListNode(9)
        e = LinkedListNode(25)
        L.insert(a)
        L.insert(b)
        L.insert(c)
        L.insert(d)
        L.insert(e)
        L.delete(b)
        l = []
        x = L.head
        while x:
            l.append(x)
            x = x.next
        self.assertEqual(l, [e, d, c, a])
