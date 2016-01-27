#!/usr/bin/env ipython

import random

class Node(object):
    def __init__(self, key, p, left, right):
        self.key = key
        self.p = p
        self.left = left
        self.right = right
    def inorder_tree_walk(self):
            if self.left != None:
                self.left.inorder_tree_walk()
            print self.key,
            if self.right != None:
                self.right.inorder_tree_walk()
    def preorder_tree_walk(self):
            print self.key,
            if self.left != None:
                self.left.preorder_tree_walk()
            if self.right != None:
                self.right.preorder_tree_walk()
    def postorder_tree_walk(self):
            if self.left != None:
                self.left.postorder_tree_walk()
            if self.right != None:
                self.right.postorder_tree_walk()
            print self.key,
    def inorder_tree_walk_stack(self):
        s = []
        s.append({"data": self, "status": 0})
        while len(s) != 0:
            record = s.pop()
            if record["status"] == 0:
                x = record["data"]
                if x.right != None:
                    s.append({"data": x.right, "status": 0})
                s.append({"data": x, "status": 1})
                if x.left != None:
                    s.append({"data": x.left, "status": 0})
            else:
                print record["data"].key,
        print
    def iterative_tree_search(self, k):
        x = self
        while x != None and x.key != k:
            if x.key < k:
                x = x.right
            else:
                x = x.left
        return x
    def minimum(self):
        x = self
        while x.left != None:
            x = x.left
        return x
    def maximum(self):
        x = self
        while x.right != None:
            x = x.right
        return x
    def successor(self):
        x = self
        if x.right != None:
            return x.right.minimum()
        else:
            while x.p != None and x.p.right == x:
                x = x.p
            return x.p
    def predecessor(self):
        x = self
        if x.left != None:
            return x.left.maximum()
        else:
            while x.p != None and x.p.left == x:
                x = x.p
            return x.p
class Tree(object):
    root = None
    def __init__(self, values):
        if isinstance(values, list):
            for i in values:
                self.insert(Node(i, None, None, None))
        else:
            print "Not invalid argument"
    def minimum(self):
        return self.root.minimum()
    def __getitem__(self, key):
        return self.root.iterative_tree_search(key)
    def insert(self, node):
        y = None
        x = self.root
        while x != None:
            y = x
            if node.key <= x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if y == None:
            self.root = node
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node
    def iterative_tree_search(self, k):
        pass
    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p
    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = z.right.minimum()
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
#A = [random.randint(1, 100) for i in range(0, 15)]
#A = [29, 81, 53, 51, 28, 31, 57, 30, 22, 62, 6, 50, 7, 2, 24, 55, 54, 56, 98]
#print A
#T = Tree(A)
#T.delete(T.root.iterative_tree_search(57))
#T.delete(T.root.iterative_tree_search(81))
#T.root.postorder_tree_walk()
#print "maximum: %d" % (T.root.maximum().key)
#inorder_tree_walk_stack(T.root)
#T.root.inorder_tree_walk_stack()
#T.root.inorder_tree_walk()
print
#T.root.preorder_tree_walk()
print
#T.root.postorder_tree_walk()
#x = T.root.iterative_tree_search(50)
#if x == None:
#    print "None"
#else:
#    print x.key
#print T.root.mimimum().key
#
#su = T.root.successor()
#if su:
#    print su.key
#pr = T.root.predecessor()
#if pr:
#    print "predecessor of root is %d " % (pr.key)
