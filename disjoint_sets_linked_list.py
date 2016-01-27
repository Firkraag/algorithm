#!/usr/bin/env ipython

class node(object):
    def __init__(self, key):
        self.key = key
        self.set = None
        self.next = None
    def find_set(self):
        return self.set.head
    def union(self, y):
        if self.set.length < y.set.length:
            x = y
            y = self
        else:
            x = self
        xs = x.set
        ys = y.set
        xs.tail.next = ys.head
        element = ys.head
        for i in range(1, ys.length + 1):
            element.set = xs
            element = element.next
        xs.tail = ys.tail
        xs.length = xs.length + ys.length
        return x
class header(object):
    def __init__(self, element):
        self.length = 1
        self.head = element
        element.set = self
        self.tail = self.head
class node_notail(node):
    def union(self, y):
        if self.set.length < y.set.length:
            x = y
            y = self
        else:
            x = self
        xs = x.set
        ys = y.set
        element = ys.head
        for i in range(1, ys.length + 1):
            element.set = xs
            tail = element
            element = element.next
        tail.next = xs.head
        xs.head = ys.head
        xs.length = xs.length + ys.length
        return y
class header_notail(object):
    def __init__(self, element):
        self.length = 1
        self.head = element
        element.set = self
