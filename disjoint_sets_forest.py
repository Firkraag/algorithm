#!/usr/bin/env python


class node:
    def __init__(self, key):
        self.key = key
        # key.index = self
        self.p = self
        self.rank = 0
        self.child = []

    def union(self, y):
        self.find_set().link(y.find_set())

    def link(self, y):
        x = self
        if x.rank > y.rank:
            x.child.append(y)
            y.p = x
        else:
            y.child.append(x)
            x.p = y
            if x.rank == y.rank:
                y.rank = y.rank + 1

    def find_set(self):
        y = self
        x = self
        while y != y.p:
            y = y.p
        while x != x.p:
            z = x
            x = x.p
            z.p = y
        #        print( y.key)
        return y

    def print_set(self):
        x = self
        while x != x.p:
            x = x.p
        x.print_set_aux()

    def print_set_aux(self):
        print(self.key)
        if len(self.child) == 0:
            return
        for child in self.child:
            child.print_set_aux()
