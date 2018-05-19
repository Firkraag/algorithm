#!/usr/bin/env ipython

class node(object):
    def __init__(self, key, right):
        self.right = right
        self.key = key


class graph(object):
    def __init__(self, data, option=0):
        if option == 0:
            self.vertices_number = len(data)
            self.vertices = [None] * self.vertices_number
            self.edges_number = 0
            for i in range(0, self.vertices_number):
                for j in data[i]:
                    self.insert_edge(i + 1, j)
        elif option == 1:
            self.vertices_number = data
            self.vertices = [None] * self.vertices_number
            self.edges_number = 0

    def transpose(self):
        t = graph(self.vertices_number, 1)
        for i in range(0, self.vertices_number):
            j = self.vertices[i]
            while j is not None:
                t.insert_edge(j.key, i + 1)
                j = j.right
        return t

    def union(self, g):
        u = graph(self.vertices_number, 1)
        for i in range(0, self.vertices_number):
            j = self.vertices[i]
            while j is not None:
                u.insert_edge(i + 1, j.key)
                j = j.right
        for i in range(0, g.vertices_number):
            j = g.vertices[i]
            while j is not None:
                u.insert_edge(i + 1, j.key)
                j = j.right
        return u

    def single_edge(self):
        g = self.union(self.transpose())
        single = graph(g.vertices_number, 1)
        s = [0] * g.vertices_number
        for u in range(0, g.vertices_number):
            v = g.vertices[u]
            while v:
                if (u + 1) != v.key and s[v.key - 1] == 0:
                    single.insert_edge(u + 1, v.key)
                    s[v.key - 1] = 1
                v = v.right
            v = g.vertices[u]
            while v:
                if s[v.key - 1] == 1:
                    s[v.key - 1] = 0
                v = v.right
            s[u] = 2
        return single

    def insert_edge(self, u, v):
        a = node(v, self.vertices[u - 1])
        self.vertices[u - 1] = a
        self.edges_number = self.edges_number + 1

    def print_graph(self):
        for i in range(0, self.vertices_number):
            j = self.vertices[i]
            print('{}: '.format(i + 1), )
            while j is not None:
                print(j.key, )
                j = j.right
            print()

    def square(self):
        grandchild = graph(self.vertices_number, 1)
        descendent = graph(self.vertices_number, 1)
        s = [0] * self.vertices_number
        # generate grandchild graph
        for i in range(0, self.vertices_number):
            j = self.vertices[i]
            while j is not None:
                k = self.vertices[j.key - 1]
                while k is not None:
                    if s[k.key - 1] == 0:
                        grandchild.insert_edge(i + 1, k.key)
                        s[k.key - 1] = 1
                        k = k.right
                j = j.right
            j = grandchild.vertices[i]
            while j is not None:
                s[j.key - 1] = 0
                j = j.right
        # generate great grandchild graph
        for i in range(0, grandchild.vertices_number):
            j = grandchild.vertices[i]
            while j is not None:
                k = self.vertices[j.key - 1]
                while k is not None:
                    if s[k.key - 1] == 0:
                        descendent.insert_edge(i + 1, k.key)
                        k = k.right
                j = j.right
            j = descendent.vertices[i]
            while j is not None:
                s[j.key - 1] = 0
                j = j.right
        square = graph(self.vertices_number, 1)
        for i in range(0, self.vertices_number):
            j = self.vertices[i]
            print(j)
            while j is not None:
                square.insert_edge(i + 1, j.key)
                s[j.key - 1] = 1
                j = j.right
            j = grandchild.vertices[i]
            while j is not None:
                if s[j.key - 1] == 0 and (i + 1) != j.key:
                    square.insert_edge(i + 1, j.key)
                    s[j.key - 1] = 1
                j = j.right
            j = descendent.vertices[i]
            while j is not None:
                if s[j.key - 1] == 0 and (i + 1) != j.key:
                    square.insert_edge(i + 1, j.key)
                    s[j.key - 1] = 1
                j = j.right

            j = square.vertices[i]
            while j is not None:
                s[j.key - 1] = 0
                j = j.right
        #        self.print(_graph())
        #        grandchild.print(_graph())
        #        print()
        #        descendent.print(_graph())
        return square

    def grandchild(self):
        pass
