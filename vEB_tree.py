#!/usr/bin/env ipython

import math

class vEB_node(object):
    def __init__(self, u):
        '''u must be exact power of 2, as required by CLRS; otherwise, the behavior is undefined'''
        self.u = u
        self.min = None
        self.max = None
        if u > 2:
            self.root = int(math.sqrt(u))
            self.cluster = [0] * self.root
            self.summary = vEB_node(self.root)
            for i in range(0, self.root):
                self.cluster[i] = vEB_node(self.root)
    def high(self, x):
        return x / self.root
    def low(self, x):
        return x % self.root
    def index(self, x, y):
        return x * self.root + y
    def member(self, x):
        if self.min == x or self.max == x:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))
    def successor(self, x):
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min != None and x < self.min:
            return self.min
        else:
            max_low = self.cluster[self.high(x)].max
            if max_low != None and self.low(x) < max_low:
                offset = self.cluster[self.high(x)].successor(self.low(x))
                return self.index(self.high(x), offset)
            else:
                succ_cluster = self.summary.successor(self.high(x))
                if succ_cluster == None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].min
                    return self.index(succ_cluster, offset)
    def empty_tree_insert(self, x):
        self.min = x
        self.max = x
    def insert(self, x):
        if self.min == None:
            self.empty_tree_insert(x)
        elif (x == self.min) or (x == self.max):
            return
        else:
            if x < self.min:
                x,self.min = self.min,x
            if self.u > 2:
                if self.cluster[self.high(x)].min == None:
                    self.summary.insert(self.high(x))
                    self.cluster[self.high(x)].empty_tree_insert(self.low(x))
                else:
                    self.cluster[self.high(x)].insert(self.low(x))
            if x > self.max:
                self.max = x
    def delete(self, x):
#        print "u = {}, x = {}".format(self.u, x)
        if self.min == self.max:
 #           print "min = {}, max = {}".format(self.min, self.max)
            if x == self.min:
                self.min = None
                self.max = None
        elif self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.max = 0
        elif x < self.min:
            return
        else:
            if x == self.min:
                first_cluster = self.summary.min
                x = self.index(first_cluster, self.cluster[first_cluster].min)
                self.min = x
            self.cluster[self.high(x)].delete(self.low(x))
            if self.cluster[self.high(x)].min == None:
                self.summary.delete(self.high(x))
                if x == self.max:
                    summary_max = self.summary.max
                    if summary_max == None:
                        self.max = self.min
                    else:
                        self.max = self.index(summary_max, self.cluster[summary_max].max)
            elif x == self.max:
                self.max = self.index(self.high(x), self.cluster[self.high(x)].max)
    def print_veb(self):
        if self.u == 2:
            print "u = {}, min = {}, max = {}".format(self.u, self.min, self.max)
        else:
            print "u = {}, min = {}, max = {}".format(self.u, self.min, self.max)
            print "Summary: \t",
            self.summary.print_veb()
            print
            for i in range(0, self.root):
                self.cluster[i].print_veb()
                print
