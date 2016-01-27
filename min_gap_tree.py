#!/usr/bin/env ipython

from rb_tree import rb_node, rb_tree

class min_gap_node(rb_node):
    def __init__(self, key, p, left, right, color, successor, min_gap):
        rb_node.__init__(self, key, p, left, right, color)
        self.successor = successor
        self.min_gap = min_gap
class min_gap_tree(rb_tree):
    positive_infinity = min_gap_node(float("Inf"), None, None, None, 1, None, float("Inf"))
    nil = min_gap_node(None, None, None, None, 1, positive_infinity, float("Inf"))
    root = nil
    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(min_gap_node(i, None, None, None, 0, None, None))
        else:
            print "Not invalid argument"
    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key <= x.key:
                x = x.left
            else:
                # update successor attribute of all z's ancestors except z's parent since z inherits the successor attribute of z's parent
                if x.right != self.nil:
                    if z.key < x.successor.key:
                        x.successor = z
                x = x.right
        if y == self.nil:
            self.root = z
            z.successor = self.positive_infinity
        elif z.key <= y.key:
            y.left = z
            z.successor = y
        else:
            y.right = z
            z.successor = y.successor
            y.successor = z
        z.p = y
        z.left = self.nil
        z.right = self.nil
        z.color = 0 #red
        traverse = z
        while traverse != self.nil:
            traverse.min_gap = min(traverse.left.min_gap, traverse.successor.key - traverse.key, traverse.right.min_gap)
            traverse = traverse.p
        self.insert_fixed(z)
    def delete(self, z):
        traverse = self.predecessor(z)
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
        # After we delete z, the only nodes whose successor attributes need to be updated are z's successor and z's predecessor 
        traverse.successor = z.successor
        while traverse != self.nil:
            traverse.min_gap = min(traverse.left.min_gap, traverse.successor.key - traverse.key, traverse.right.min_gap)
            traverse = traverse.p
        traverse = x.p
        while traverse != self.nil:
            traverse.min_gap = min(traverse.left.min_gap, traverse.successor.key - traverse.key, traverse.right.min_gap)
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
        y.min_gap = x.min_gap
        x.min_gap = min(x.left.min_gap, x.successor.key - x.key, x.right.min_gap)
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
        x.min_gap = y.min_gap
        y.min_gap = min(y.left.min_gap, y.successor.key - y.key, y.right.min_gap)
    def predecessor(self, x):
        if x.left != self.nil:
            return x.left.maximum()
        else:
            while x.p != self.nil and x.p.left == x:
                x = x.p
            return x.p
