#!/usr/bin/env ipython

# we use 0 to mean red, 1 to mean black

from tree import Node, Tree


class rb_node(Node):
    def __init__(self, key, p, left, right, color):
        Node.__init__(self, key, p, left, right)
        self.color = color

    def minimum(self, nil):
        x = self
        y = x
        while x != nil:
            y = x
            x = x.left
        return y


class rb_tree(Tree):
    nil = rb_node(None, None, None, None, 1)
    root = nil

    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(rb_node(i, None, None, None, 0))
        else:
            print("Not invalid argument")

    def minimum(self):
        return self.root.minimum(self.nil)

    def __getitem__(self, key):
        return self.iterative_tree_search(key)

    def left_rotate(self, x):
        y = x.right
        z = y.left
        p = x.p
        x.right = z
        x.p = y
        y.left = x
        y.p = p
        if z != self.nil:
            z.p = x
        if p == self.nil:
            self.root = y
        elif p.left == x:
            p.left = y
        else:
            p.right = y

    def right_rotate(self, y):
        x = y.left
        z = x.right
        p = y.p
        y.left = z
        y.p = x
        x.right = y
        x.p = p
        if z != self.nil:
            z.p = y
        if p == self.nil:
            self.root = x
        elif p.left == y:
            p.left = x
        else:
            p.right = x

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
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

    def iterative_tree_search(self, k):
        x = self.root
        while x != self.nil and x.key != k:
            if x.key < k:
                x = x.right
            else:
                x = x.left
        return x

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u.p.left == u:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

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
