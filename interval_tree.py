#!/usr/bin/env python

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

    def list_all_overlapping_intervals(self, T, i):
        x = self
        if x.interval.high >= i.low and i.high >= x.interval.low:
            print(x.interval.low, x.interval.high)
        if x.left != T.nil and x.left.maximum >= i.low:
            self.left.list_all_overlapping_intervals(T, i)
            self.right.list_all_overlapping_intervals(T, i)
        elif x.right != T.nil:
            self.right.list_all_overlapping_intervals(T, i)

    def interval_search_exactly(self, T, i):
        if self.interval.low == i.low and self.interval.high == i.high:
            return self
        if self.interval.low > i.low:
            if self.left != T.nil:
                return self.left.interval_search_exactly(T, i)
            else:
                return T.nil
        else:
            if self.right != T.nil:
                return self.right.interval_search_exactly(T, i)
            else:
                return T.nil


class interval_tree(rb_tree):
    nil = interval_node(None, None, None, None, 1, None, float("-Inf"))
    root = nil

    def __init__(self, intervals):
        if isinstance(intervals, list):
            for i in intervals:
                self.insert(interval_node(
                    i.low, None, None, None, 0, i, i.high))
        else:
            print("Not invalid argument")

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
        z.color = 0  # red
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
            traverse.maximum = max(
                traverse.left.maximum, traverse.interval.high, traverse.right.maximum)
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

    def closed_interval_search_minimum_low_end(self, interval):
        '''given an interval, returns an interval over-
        lapping i that has the minimum low endpoint, or T.nil if no such interval exists'''
        x = self.root
        overlap = False
        i = self.nil
        while x != self.nil:
            if x.interval.high >= interval.low and interval.high >= x.interval.low:
                overlap = True
                i = x
            if x.left != self.nil and interval.low <= x.left.maximum:
                x = x.left
            elif not overlap:
                x = x.right
            else:
                break
        return i

    def open_interval_search(self, interval):
        x = self.root
        while x != self.nil and (x.interval.high <= interval.low or interval.high <= x.interval.low):
            if x.left != self.nil and interval.low < x.left.maximum:
                x = x.left
            else:
                x = x.right
        return x

    def list_all_overlapping_intervals(self, i):
        if self.root == self.nil:
            return
        else:
            self.root.list_all_overlapping_intervals(self, i)
            print()

    def interval_search_exactly(self, i):
        if self.root == self.nil:
            return self.nil
        else:
            return self.root.interval_search_exactly(self, i)
