class fibonacci_node(object):
    degree = 0
    p = None
    child = None
    mark = False
    left = None
    right = None
    def __init__(self, k):
        self.key = k
    def __iter__(self):
        '''generate a list of children of the node for iteration'''
        self.children = []
        self.index = 0
        if self.child != None:
            child = self.child
            while True:
                self.children.append(child)
                if child != self.child.left:
                    child = child.right
                else:
                    break
        return self
    def next(self):
        if self.index < len(self.children):
            self.index = self.index + 1
            return self.children[self.index - 1]
        else:
            raise StopIteration
    def insert(self, x):
        '''insert x to the left of node'''
        x.left = self.left
        x.right = self
        self.left.right = x
        self.left = x    
    def concatenate(self, x):
        '''concatenate two lists represented by the node and x,
        x mustn't be None'''
        self.left.right = x.right
        x.right.left = self.left
        self.left = x
        x.right = self
    def remove(self):
        self.left.right = self.right    
        self.right.left = self.left
    def add_child(self, y):
        self.degree = self.degree + 1
        y.mark = False
        y.p = self
        if self.child == None:
            self.child = y
            y.left = y
            y.right = y
        else:
            self.child.insert(y)    
            print "y.left.key = {}, y.right.key = {}".format(y.left.key, y.right.key)
    def remove_child(self, y):
        self.degree = self.degree - 1
        if y.right == y:
            self.child = None
        elif y == self.child:
            self.child = y.left
            y.remove()
        else:
            y.remove()
class fibonacci_heap(object):
    def __init__(self):
        self.n = 0
        self.minimum = None
    def __iter__(self):
        '''generate a list of children of the node for iteration'''
        self.root_list = []
        self.index = 0
        if self.minimum != None:
            root = self.minimum
            while True:
                self.root_list.append(root)
                if root != self.minimum.left:
                    root = root.right
                else:
                    break
        return self
    def next(self):
        if self.index < len(self.root_list):
            self.index = self.index + 1
            return self.root_list[self.index - 1]
        else:
            raise StopIteration
    def __repr__(self):
        s = ''
        x = self.minimum
        if x != None:
            while True:
                s = s + '\t' + str(x.key)    
                if x == self.minimum.left:
                    break
                else:
                    x = x.right
            return s
        else:
            return ''
    def insert(self, x):
        '''insert the node x into the root list of fibonacci heap'''
        x.p = None
        if self.minimum == None:
            self.minimum = x
            x.left = x
            x.right = x
        else:
            self.minimum.insert(x)
            if x.key < self.minimum.key:
                self.minimum = x
        self.n = self.n + 1
    def minimum(self):
        return self.minimum
    def union(self, h):
        cat = fibonacci_heap()
        if self.minimum == None:
            return h
        elif h.minimum == None:
            return self
        else:
            self.minimum.concatenate(h.minimum)
            if self.minimum.key <= h.minimum.key:
                cat.minimum = self.minimum
            else:
                cat.minimum = h.minimum
        cat.n = self.n + h.n
        return cat
    def extract_min(self):
        z = self.minimum
        if z != None:
            for child in z:
                self.insert(child)
            z.remove()
            if z == z.right:
                self.minimum = None
            else:
                self.minimum = z.right
                self.consolidate()
            self.n = self.n - 1
        return z
    def consolidate(self):
        D = self.n / 2
        A = [None] * (D + 1)
        left = self.minimum.left
        w = self.minimum
        for w in self:
            x = w
            d = x.degree
            print 'w.key = {}'.format(w.key)
            print 'w.degree = {}'.format(w.degree)
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
                    x,y = y,x
                self.link(y, x)
                A[d] = None
                d = d + 1
            A[d] = x
        self.minimum = None
        for i in A:
            if i != None:
                self.insert(i)
    def link(self, y, x):
        y.remove()
        x.add_child(y)
    def decrease_key(self, x, k):
        if k > x.key:
            print "new key is greater than current key"
            return
        x.key = k
        y = x.p
        if y != None and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.key < self.minimum.key:
            self.minimum = x
    def cut(self, x, y):
        y.remove_child(x)
        x.mark = False
        self.insert(x)
    def cascading_cut(self, y):
        z = y.p
        if z != None:
            if y.mark == False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)
    def delete(self, x):
        self.decrease_key(x, float("-Inf"))
        self.extract_min()
