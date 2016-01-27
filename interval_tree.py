#!/usr/bin/env ipython

from rb_tree import rb_node, rb_tree

class interval(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high
class interval_node(rb_node):
    def __init__(self, key, p, left, right, color, interval, maximum):
        rb_node.__init__(self, key, p, left, right, color)
        self.interval = interval
        self.maximum = maximum
class interval_tree(rb_tree):
    nil = interval_node(None, None, None, None, 1, None, float("-Inf"))
    root = nil
    def __init__(self, intervals):
        if isinstance(intervals, list):
            for i in intervals:
                self.insert(interval_node(i.low, None, None, None, 0, i, i.high))
        else:
            print "Not invalid argument"
    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if x.maximum < z.maximum:
                x.maximum = z.maximum
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
        z.color = 0 #red
        self.insert_fixed(z)
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
        y.maximum = x.maximum
        x.maximum = max(x.left.maximum, x.interval.high, x.right.maximum)
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
        x.maximum = y.maximum
        y.maximum = max(y.left.maximum, y.interval.high, y.right.maximum)
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
            traverse.maximum = max(traverse.left.maximum, traverse.interval.high, traverse.right.maximum)
            traverse = traverse.p
        if y_original_color == 1:
            self.delete_fixup(x)
    def closed_interval_search(self, interval):
        x = self.root
        while x != self.nil and (x.interval.high < interval.low or interval.high < x.interval.low):
            if x.left != self.nil and interval.low <= x.left.maximum:
                x = x.left
            else:
                x = x.right
        return x
    def open_interval_search(self, interval):
        x = self.root
        while x != self.nil and (x.interval.high <= interval.low or interval.high <= x.interval.low):
            if x.left != self.nil and interval.low < x.left.maximum:
                x = x.left
            else:
                x = x.right
        return x
# A more straightforward implemention of interval search compared to the one on the textbook
    def closed_interval_serach_straightforward(self, interval):
        x = self.root
        while x != self.nil:
            if x.interval.low > interval.high:
                x = x.left
            elif interval.low > x.interval.high:
                x = x.right
            # if x.interval.low <= interval.high and interval.low <= x.interval.high, then x overlaps interval
            else:
                return x
        return self.nil
    def list_all_overlapping_intervals(self, i):
        if    self.root == self.nil:
            return
        s = []
        s.append(self.root)
        while len(s) != 0:
            x = s.pop()
            if x.interval.low > i.high:
                if x.left != self.nil:
                    s.append(x.left)
            elif i.low > x.interval.high:
                if x.right != self.nil:
                    s.append(x.right)
            else:
                if x.left != self.nil:
                    s.append(x.left)
                if x.right != self.nil:
                    s.append(x.right)
                print x.interval.low, x.interval.high
