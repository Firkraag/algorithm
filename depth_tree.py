#!/usr/bin/env ipython

# A variant of red black tree that has depth attribute

from rb_tree import rb_node, rb_tree

class depth_node(rb_node):
    def __init__(self, key, p, left, right, color, depth):
        rb_node.__init__(self, key, p, left, right, color)
        self.depth = depth
    def update_depth_whole_tree(self, amount):
        if self.depth != -1:
            self.left.update_depth_whole_tree(amount)
            self.depth = self.depth + amount
            self.right.update_depth_whole_tree(amount)
class depth_tree(rb_tree):
    nil = depth_node(None, None, None, None, 1, -1)
    root = nil
    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(depth_node(i, None, None, None, 0, 0))
        else:
            print "Not invalid argument"
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
        x.depth = x.depth + 1
        y.depth = y.depth - 1
        x.left.update_depth_whole_tree(1)
        y.right.update_depth_whole_tree(-1)
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
        x.depth = x.depth - 1
        y.depth = y.depth + 1
        x.left.update_depth_whole_tree(-1)
        y.right.update_depth_whole_tree(1)
    def insert(self, z):
        y = self.nil
        x = self.root
        depth = 0
        while x != self.nil:
            depth = depth + 1
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                x = x.right
        z.depth = depth
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
        y.depth = z.depth
        if x != self.nil:
            x.update_depth_whole_tree(-1)
        if y_original_color == 1:
            self.delete_fixup(x)
