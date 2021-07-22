#!/usr/bin/env python


class b_tree_node:
    def __init__(self, t, leaf, n):
        self.leaf = leaf
        self.n = n
        self.t = t
        self.key = [0] * (2 * t - 1)
        self.c = [0] * (2 * t)

    def split_child(self, i):
        y = self.c[i - 1]
        t = y.t
        z = b_tree_node(t, y.leaf, t - 1)
        for j in range(1, t):
            z.key[j - 1] = y.key[j + t - 1]
        if not y.leaf:
            for j in range(1, t + 1):
                z.c[j - 1] = y.c[j + t - 1]
        y.n = t - 1
        for j in range(self.n + 1, i, -1):
            self.c[j] = self.c[j - 1]
        self.c[i] = z
        for j in range(self.n, i - 1, -1):
            self.key[j] = self.key[j - 1]
        self.key[i - 1] = y.key[t - 1]
        self.n = self.n + 1

    def insert_nonfull(self, k):
        i = self.n
        t = self.t
        if self.leaf:
            while i >= 1 and k < self.key[i - 1]:
                self.key[i] = self.key[i - 1]
                i = i - 1
            self.key[i] = k
            self.n = self.n + 1
        else:
            while i >= 1 and k < self.key[i - 1]:
                i = i - 1
            i = i + 1
            if self.c[i - 1].n == 2 * t - 1:
                self.split_child(i)
                if k > self.key[i - 1]:
                    i = i + 1
            self.c[i - 1].insert_nonfull(k)

    def search(self, k):
        i = 1
        while i <= self.n and k > self.key[i - 1]:
            i = i + 1
        if i <= self.n and k == self.key[i - 1]:
            return self, i
        elif self.leaf:
            return None
        else:
            return self.c[i - 1].search(k)

    def print_inorder(self):
        if self.leaf:
            for i in range(1, self.n + 1):
                print(self.key[i - 1], )
        else:
            for i in range(1, self.n + 1):
                self.c[i - 1].print_inorder()
                print(self.key[i - 1], )
            self.c[self.n].print_inorder()

    def print_child_first(self):
        if not self.leaf:
            for i in range(1, self.n + 2):
                self.c[i - 1].print_child_first()
        for i in range(1, self.n + 1):
            print(self.key[i - 1], )

    def delete(self, tree, k):
        t = self.t
        i = 1
        while i <= self.n and k > self.key[i - 1]:
            i = i + 1
        if i <= self.n and k == self.key[i - 1]:
            if self.leaf:
                for j in range(i, self.n):
                    self.key[j - 1] = self.key[j]
                self.n = self.n - 1
            else:
                y = self.c[i - 1]
                z = self.c[i]
                if y.n >= t:
                    p = y
                    while not p.leaf:
                        p = p.c[p.n]
                    key = p.key[p.n - 1]
                    y.delete(tree, key)
                    self.key[i - 1] = key
                elif z.n >= t:
                    s = z
                    while not s.leaf:
                        s = s.c[0]
                    key = s.key[0]
                    z.delete(tree, key)
                    self.key[i - 1] = key
                else:
                    self.merge(tree, i)
                    y.delete(tree, k)
        elif self.leaf:
            return None
        elif self.c[i - 1].n <= t - 1:
            if i <= self.n and self.c[i].n >= t:
                a = self.c[i - 1]
                b = self.c[i]
                a.key[a.n] = self.key[i - 1]
                self.key[i - 1] = b.key[0]
                for j in range(2, b.n + 1):
                    b.key[j - 2] = b.key[j - 1]
                a.c[a.n + 1] = b.c[0]
                for j in range(1, b.n + 1):
                    b.c[j - 1] = b.c[j]
                a.n = a.n + 1
                b.n = b.n - 1
                a.delete(tree, k)
            elif i == self.n + 1 and self.c[i - 2].n >= t:
                b = self.c[i - 2]
                a = self.c[i - 1]
                for j in range(1, a.n + 1):
                    a.key[j] = a.key[j - 1]
                a.key[0] = self.key[i - 2]
                self.key[i - 2] = b.key[b.n - 1]
                for j in range(1, a.n + 2):
                    a.c[j] = a.c[j - 1]
                a.c[0] = b.c[b.n]
                b.n = b.n - 1
                a.n = a.n + 1
                a.delete(tree, k)
            elif i <= self.n:
                self.merge(tree, i)
                self.c[i - 1].delete(tree, k)
            else:
                self.merge(tree, i - 1)
                self.c[i - 2].delete(tree, k)
        else:
            self.c[i - 1].delete(tree, k)

    def merge(self, tree, i):
        y = self.c[i - 1]
        z = self.c[i]
        t = y.t
        yn = y.n
        zn = z.n
        y.key[t - 1] = self.key[i - 1]
        for j in range(1, zn + 1):
            y.key[j + yn] = z.key[j - 1]
        if not y.leaf:
            for j in range(1, zn + 2):
                y.c[j + yn] = z.c[j - 1]
        y.n = yn + zn + 1
        for j in range(i, self.n):
            self.key[j - 1] = self.key[j]
        for j in range(i + 1, self.n + 1):
            self.c[j - 1] = self.c[j]
        self.n = self.n - 1
        if tree.root == self and self.n == 0:
            tree.root = y


class b_tree:
    def __init__(self, t):
        self.t = t
        self.root = b_tree_node(t, True, 0)

    def insert(self, k):
        r = self.root
        t = self.t
        if r.n == 2 * t - 1:
            s = b_tree_node(t, False, 0)
            self.root = s
            s.c[0] = r
            s.split_child(1)
            s.insert_nonfull(k)
        else:
            r.insert_nonfull(k)

    def print_b_tree(self):
        r = self.root
        r.print_inorder()

    #    def predecessor(self, k):
    #        m = []
    #        x = self.root
    #        while not x.leaf:
    #            i = 1
    #            while i <= x.n and k > x.key[i - 1]:
    #                i = i + 1
    #            if i <= x.n and k == x.key[i - 1]:
    #                x = x.c[i - 1]
    #                while not x.leaf:
    #                    x = x.c[x.n]
    #                return x.key[x.n - 1]
    #            else:
    #                x = x.c[i - 1]
    #                if i > 1:
    #                    m.append(x.key[i - 1])
    #        i = 1
    #        while i <= x.n and k != x.key[i - 1]:
    #            i = i + 1
    #        if i > x.n or len(m) == 0:
    #            return None
    #        elif i > 1:
    #            return x.key[i - 2]
    #        else:
    #            return max(m)
    def predecessor(self, k):
        s = []
        x = self.root
        while True:
            i = 1
            while i <= x.n and k > x.key[i - 1]:
                i = i + 1
            if i > 1:
                s.append(x.key[i - 2])
            if x.leaf:
                break
            else:
                x = x.c[i - 1]
        if len(s) == 0:
            return None
        else:
            return max(s)
