# A variant of red black tree that has black_height attribute
# !/usr/bin/env ipython

from rb_tree import rb_node, rb_tree


class bh_node(rb_node):
    def __init__(self, key, p, left, right, color, bh):
        rb_node.__init__(self, key, p, left, right, color)
        self.bh = bh


class bh_tree(rb_tree):
    nil = bh_node(None, None, None, None, 1, 0)
    root = nil

    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(bh_node(i, None, None, None, 0, 1))
        else:
            print("Not invalid argument")

    def insert_fixed(self, z):
        while z.p.color == 0:
            if z.p.p.left == z.p:
                y = z.p.p.right
                if y.color == 0:
                    z.p.color = 1
                    y.color = 1
                    z.p.p.color = 0
                    z = z.p.p
                    z.bh = z.bh + 1
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
                    z.bh = z.bh + 1
                else:
                    if z.p.left == z:
                        z = z.p
                        self.right_rotate(z)
                    z = z.p.p
                    self.left_rotate(z)
                    z.color = 0
                    z.p.color = 1
        self.root.color = 1

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
                    x.bh = x.bh - 1
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
                    w.bh = w.bh + 1
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
                    w.bh = w.bh + 1
                    x = self.root
        x.color = 1
