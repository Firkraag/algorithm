import unittest
from linked_list import linked_list, linked_list_node


class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        L = linked_list()
        a = linked_list_node(1)
        b = linked_list_node(4)
        c = linked_list_node(16)
        d = linked_list_node(9)
        e = linked_list_node(25)
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
        L = linked_list()
        a = linked_list_node(1)
        b = linked_list_node(4)
        c = linked_list_node(16)
        d = linked_list_node(9)
        e = linked_list_node(25)
        L.insert(a)
        L.insert(b)
        L.insert(c)
        L.insert(d)
        L.insert(e)
        self.assertEqual(L.search(4), b)

    def test_delete(self):
        L = linked_list()
        a = linked_list_node(1)
        b = linked_list_node(4)
        c = linked_list_node(16)
        d = linked_list_node(9)
        e = linked_list_node(25)
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
