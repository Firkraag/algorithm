# The variant of os_tree that use rank instead of size
# !/usr/bin/env python

from rb_tree import RbNode, RbTree


class rank_node(RbNode):
    def __init__(self, key, p, left, right, color, rank):
        RbNode.__init__(self, key, p, left, right, color)
        self.rank = rank

    def update_rank_whole_tree(self, amount):
        if self.rank != 0:
            self.rank = self.rank + amount
            self.left.update_rank_whole_tree(amount)
            self.right.update_rank_whole_tree(amount)

    def decrease_all_successors(self, amount):
        self.rank = self.rank - amount
        self.right.update_rank_whole_tree(-1 * amount)
        y = self.p
        x = self
        while y.rank != 0 and y.right == x:
            x = y
            y = y.p
        if y.rank != 0:
            y.decrease_all_successors(amount)


class rank_tree(RbTree):
    nil = rank_node(None, None, None, None, 1, 0)
    root = nil

    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(rank_node(i, None, None, None, 0, 1))
        else:
            print("Not invalid argument")

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key <= x.key:
                x.rank = x.rank + 1
                x.right.update_rank_whole_tree(1)
                x = x.left
            else:
                x = x.right
        if y == self.nil:
            self.root = z
            z.rank = 1
        elif z.key <= y.key:
            y.left = z
            z.rank = y.rank - 1
        else:
            y.right = z
            z.rank = y.rank + 1
        z.p = y
        z.left = self.nil
        z.right = self.nil
        z.color = 0  # red
        self.insert_fixed(z)

    def delete(self, z):
        z.decrease_all_successors(1)  # z is counted as a successor
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
        if y_original_color == 1:
            self.delete_fixup(x)
