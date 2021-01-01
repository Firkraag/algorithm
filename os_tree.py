#!/usr/bin/env python

from rb_tree import rb_node, rb_tree


class OSNode(rb_node):
    def __init__(self, key, p, left, right, color, size):
        rb_node.__init__(self, key, p, left, right, color)
        self.size = size

    def select_recursive(self, i):
        r = self.left.size + 1
        if i == r:
            return self
        elif i < r:
            return self.left.select_recursive(i)
        else:
            return self.right.select_recursive(i - r)

    def select_iterative(self, i):
        x = self
        while True:
            r = x.left.size + 1
            if i == r:
                return x
            elif i < r:
                x = x.left
            else:
                x = x.right
                i = i - r

    def key_rank(self, k):
        r = self.left.size + 1
        if k == self.key:
            return r
        elif k < self.key:
            return self.left.key_rank(k)
        else:
            return r + self.right.key_rank(k)

    def ith_successor(self, i):
        if i == 0:
            return self
        r = self.right.size
        if i <= r:
            return self.right.select_recursive(i)
        else:
            x = self
            y = self.p
            while y.size != 0 and y.right == x:
                x = y
                y = y.p
            if y.size != 0:
                return y.ith_successor(i - r - 1)


class os_tree(rb_tree):
    nil = OSNode(None, None, None, None, 1, 0)
    root = nil

    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(OSNode(i, None, None, None, 0, 1))
        else:
            print("Not invalid argument")

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            x.size = x.size + 1
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                x = x.right
        if y == self.nil:
            self.root = z
        elif z.key <= y.key:
            y.left = z
        else:
            y.right = z
        z.p = y
        z.left = self.nil
        z.right = self.nil
        z.color = 0  # red
        self.insert_fixed(z)

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        traverse = x.p
        while traverse != self.nil:
            traverse.size = traverse.size - 1
            traverse = traverse.p
        if y_original_color == 1:
            self.delete_fixup(x)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x.p.left == x:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y.p.right == y:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x
        x.size = y.size
        y.size = y.left.size + y.right.size + 1

    def rank(self, x):
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y.p.right == y:
                r = r + y.p.left.size + 1
            y = y.p
        return r
