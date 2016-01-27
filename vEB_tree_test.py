#!/usr/bin/env ipython

import unittest
from vEB_tree import vEB_node

class testVEB(unittest.TestCase):
    def test_vEB(self):
        v = vEB_node(2 ** 8)
        l = [1, 4, 50, 30, 100, 201]
        for i in l:
            v.insert(i)
        for i in l:
            self.assertEquals(v.member(i), True)
        self.assertEquals(v.member(2), False)
        self.assertEquals(v.member(3), False)
        v.delete(1)
        self.assertEquals(v.member(1), False)
        v.delete(100)
        self.assertEquals(v.member(100), False)
