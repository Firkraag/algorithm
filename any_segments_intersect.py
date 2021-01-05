#!/usr/bin/env python

# we use 0 to mean red, 1 to mean black

from tree import Node, Tree
from heap import MaxHeap
from segment_intersect import segments_intersect


def vertical(a):
    return a[0][0] == a[1][0]


def comparable(a, b, x):
    """
    Given two segments a and b that are comparable at x, determine whether a is above b or not. Assume that neither segment is vertical
    """
    p1 = a[0]
    p2 = a[1]
    p3 = b[0]
    p4 = b[1]
    x4 = p4[0]
    x3 = p3[0]
    if vertical(a) and vertical(b):
        return p1[1] >= p3[1]
    elif vertical(a) and not vertical(b):
        v1 = (p4[0] - p3[0], p4[1] - p3[1])
        v2 = (p4[0] - p1[0], p4[1] - p1[1])
        result = v1[0] * v2[1] - v2[0] * v1[1]
        return result < 0
    elif not vertical(a) and vertical(b):
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p2[0] - p3[0], p2[1] - p3[1])
        result = v1[0] * v2[1] - v2[0] * v1[1]
        return result >= 0
    else:
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = ((x4 - x3) * (p2[0] - p4[0]) + (x4 - x) * (p4[0] - p3[0]),
              (x4 - x3) * (p2[1] - p4[1]) + (x4 - x) * (p4[1] - p3[1]))
        result = v1[0] * v2[1] - v2[0] * v1[1]
        return result >= 0


class segment(tuple):
    def __init__(self, seg):
        super(segment, self).__init__(seg)
        self.pointer = None


class point(list):
    def __init__(self, info, segment):
        super(point, self).__init__(info)
        self.segment = segment


class rb_node(Node):
    def __init__(self, key, p, left, right, color):
        Node.__init__(self, key, p, left, right)
        self.color = color
        if key is not None:
            key.pointer = self

    def minimum(self, nil):
        x = self
        y = x
        while x != nil:
            y = x
            x = x.left
        return y

    def maximum(self, nil):
        x = self
        while x.right != nil:
            x = x.right
        return x


class rb_tree(Tree):
    nil = rb_node(None, None, None, None, 1)
    root = nil

    def __init__(self):
        pass

    def above(self, s):
        x = s.pointer
        if x.right != self.nil:
            return x.right.minimum(self.nil).key
        else:
            while x.p != self.nil and x.p.right == x:
                x = x.p
            return x.p.key

    def below(self, s):
        x = s.pointer
        if x.left != self.nil:
            return x.left.maximum(self.nil).key
        else:
            while x.p != self.nil and x.p.left == x:
                x = x.p
            return x.p.key

    def minimum(self):
        return self.root.minimum(self.nil)

    def __getitem__(self, key):
        return self.iterative_tree_search(key)

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

    def insert(self, z):
        """ the segment z will only be inserted when the left endpoint of z is being processed"""
        # this is the x_coordinate of the left endpoint of z
        x_coordinate = z[0][0]
        z = rb_node(z, None, None, None, 0)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if comparable(z.key, x.key, x_coordinate):
                x = x.right
            else:
                x = x.left
        if y == self.nil:
            self.root = z
        elif comparable(z.key, y.key, x_coordinate):
            y.right = z
        else:
            y.left = z
        z.p = y
        z.left = self.nil
        z.right = self.nil
        z.color = 0  # red
        self.insert_fixed(z)

    def insert_fixed(self, z):
        while z.p.color == 0:
            if z.p.p.left == z.p:
                y = z.p.p.right
                if y.color == 0:
                    z.p.color = 1
                    y.color = 1
                    z.p.p.color = 0
                    z = z.p.p
                else:
                    if z.p.right == z:
                        z = z.p
                        self.left_rotate(z)
                    z = z.p.p
                    self.right_rotate(z)
                    z.color = 0
                    z.p.color = 1
            else:
                y = z.p.p.left
                if y.color == 0:
                    z.p.color = 1
                    y.color = 1
                    z.p.p.color = 0
                    z = z.p.p
                else:
                    if z.p.left == z:
                        z = z.p
                        self.right_rotate(z)
                    z = z.p.p
                    self.left_rotate(z)
                    z.color = 0
                    z.p.color = 1
        self.root.color = 1

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u.p.left == u:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def delete(self, z):
        z = z.pointer
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = z.right.minimum(self.nil)
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
        if y_original_color == 1:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == 1:
            if x == x.p.left:
                w = x.p.right
                if w.color == 0:
                    w.color = 1
                    x.p.color = 0
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.p
                else:
                    if w.left.color == 0 and w.right.color == 1:
                        w.left.color = 1
                        w.color = 0
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 1
                    w.right.color = 1
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 0:
                    w.color = 1
                    x.p.color = 0
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.left.color == 1 and w.right.color == 1:
                    w.color = 0
                    x = x.p
                else:
                    if w.left.color == 1 and w.right.color == 0:
                        w.right.color = 1
                        w.color = 0
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    w.left.color = 1
                    x.p.color = 1
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 1


def any_segments_intersect(S):
    """This algorithm takes as input a set S of n line segments, returning the boolean value TRUE if any pair of segments in S intersects, and FALSE otherwise."""
    T = rb_tree()
    segment_list = []
    point_list = []
    for s in S:
        segment_list.append(segment(s))
    for s in segment_list:
        point_list.append(point([s[0][0], 0, s[0][1]], s))
        point_list.append(point([s[1][0], 1, s[1][1]], s))
    heap_point = MaxHeap(point_list)
    heap_point.heapsort()
    for p in heap_point:
        if p[1] == 0:
            s = p.segment
            T.insert(s)
            a = T.above(s)
            b = T.below(s)
            if (a is not None and segments_intersect(a[0], a[1], s[0], s[1])) or (b is not None and segments_intersect(b[0], b[1], s[0], s[1])):
                return True
        if p[1] == 1:
            s = p.segment
            a = T.above(s)
            b = T.below(s)
#            print( a)
#            print( b)
#            print( type(a))
#            print( type(b))
            if a is not None and b is not None and segments_intersect(a[0], a[1], b[0], b[1]):
                return True
            T.delete(s)
    return False
