#!/usr/bin/env ipython

from rb_tree import rb_node, rb_tree


class pointer_node(rb_node):
    def __init__(self, key, p, left, right, color, minimum, maximum, predecessor, successor):
        rb_node.__init__(self, key, p, left, right, color)
        self.minimum = minimum
        self.maximum = maximum
        self.predecessor = predecessor
        self.successor = successor


class pointer_tree(rb_tree):
    negative_infinity = pointer_node(float("-Inf"), None, None, None, 1, None, None, None, None)
    positive_infinity = pointer_node(float("Inf"), None, None, None, 1, None, None, None, None)
    nil = pointer_node(None, None, None, None, 1, negative_infinity, positive_infinity, None, None)
    root = nil

    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(pointer_node(i, None, None, None, 0, None, None, None, None))
        else:
            print("Not invalid argument")

    def insert(self, z):
        y = self.nil
        x = self.root

        while x != self.nil:
            y = x
            if z.key <= x.key:
                if z.key < x.minimum.key:
                    x.minimum = z
                # update predecessor attribute of all z's ancestors except z's parent since z inherits the predecessor attribute of z's parent
                if x.left != self.nil:
                    if z.key > x.predecessor.key:
                        x.predecessor = z
                x = x.left
            else:
                if z.key > x.maximum.key:
                    x.maximum = z
                # update successor attribute of all z's ancestors except z's parent since z inherits the successor attribute of z's parent
                if x.right != self.nil:
                    if z.key < x.successor.key:
                        x.successor = z
                x = x.right
        if y == self.nil:
            self.root = z
            z.predecessor = self.negative_infinity
            z.successor = self.positive_infinity
        elif z.key <= y.key:
            y.left = z
            z.successor = y
            z.predecessor = y.predecessor
            y.predecessor = z
        else:
            y.right = z
            z.predecessor = y
            z.successor = y.successor
            y.successor = z
        z.minimum = z
        z.maximum = z
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
        y.minimum = x.minimum
        if x.right == self.nil:
            x.maximum = x
        else:
            x.maximum = x.right.maximum

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
        if y.left == self.nil:
            y.minimum = y
        else:
            y.minimum = y.left.minimum

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
        # After we delete z, the only nodes whose predecessor and successor attributes need to be updated are z's successor and z's predecessor 
        z.predecessor.successor = z.successor
        z.successor.predecessor = z.predecessor
        traverse = x.p
        while traverse != self.nil:
            if traverse.left == self.nil:
                traverse.minimum = traverse
            else:
                traverse.minimum = traverse.left.minimum
            if traverse.right == self.nil:
                traverse.maximum = traverse
            else:
                traverse.maximum = traverse.right.maximum
            traverse = traverse.p
        if y_original_color == 1:
            self.delete_fixup(x)
