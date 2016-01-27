#!/usr/bin/env ipython
import unittest
from graph import Vertex, Graph

class TestGraph(unittest.TestCase):
    def testBfs(self):
        s = Vertex('s')
        r = Vertex('r')
        v = Vertex('v')
        w = Vertex('w')
        t = Vertex('t')
        x = Vertex('x')
        u = Vertex('u')
        y = Vertex('y')
        z = Vertex('z')
        vertices = [v,r,s,w,t,x,u,y,z]
        edges = [(s, r), (s, w), (r, v), (r, s), (v, r), (w, s), (w, t), (w, x), (t, w), (t, x), (t, u), (u, t), (u, x), (u, y), (x, w), (x, t), (x, u), (x, y), (y, x), (y, u)]
        g = Graph(vertices, edges)
        #g.printAllEdges()
        #for i in g.vertices:
        #    i.printEdge()
    #        print
        g.bfs(s)
    #    g.printVertices()
        self.assertEquals(s.d, 0)
        self.assertEquals(r.d, 1)
        self.assertEquals(v.d, 2)
        self.assertEquals(w.d, 1)
        self.assertEquals(t.d, 2)
        self.assertEquals(x.d, 2)
        self.assertEquals(u.d, 3)
        self.assertEquals(y.d, 3)
    def testDfs(self):
        s = Vertex('s')
        v = Vertex('v')
        z = Vertex('z')
        w = Vertex('w')
        y = Vertex('y')
        x = Vertex('x')
        t = Vertex('t')
        u = Vertex('u')
        #edges_list = [(z, w), (s, w), (y, w), (x, ), (x, ), (z, ), (v, u), (v, t)]
        #vertices = (s, v, z, w, y, x, t, u)
        #map(lambda vertex, edges: map(lambda vertex, edge: vertex.addEdge(edge), zip([vertex] * len(edges) , edges)),  zip(vertices, edges_list))
        vertices = [s, v, z, w, y, x, t, u]
        edges = [(y, x), (x, z), (z, y), (z, w), (w, x), (s, z), (s, w), (v, w), (v, s), (t, v), (t, u), (u, v), (u, t)]
        g = Graph(vertices, edges)
        g.dfs()
        vertices = (s, v, z, w, y, x, t, u)
#        for u in vertices:
#            print u, u.d, u.f
        #df = [(1, 10), (12, 13), (2, 9), (7, 8), (3, 6), (4, 5), (11, 16), (14, 15)]
        #edges_list = [(z, w), (s, w), (y, w), (x, ), (x, ), (z, ), (v, u), (v, t)]
    def testPathNum(self):
        m = Vertex('m')        
        n = Vertex('n')        
        o = Vertex('o')        
        p = Vertex('p')        
        q = Vertex('q')        
        r = Vertex('r')        
        s = Vertex('s')        
        t = Vertex('t')        
        u = Vertex('u')        
        v = Vertex('v')        
        w = Vertex('w')        
        x = Vertex('x')        
        y = Vertex('y')        
        z = Vertex('z')        
        vertices = [m, n, o, p, q, r, s, t, u, v, w, x, y, z]
        edges = [(m, q), (m, r), (m, x), (n, q), (n, o), (n, u), (o, r), (o, s), (o, v), (p, o), (p, s), (p, z), (q, t), (r, u), (r, y), (s, r), (u, t), (v, w), (v, x), (w, z), (y, v)]
        g = Graph(vertices, edges)
        self.assertEquals(g.path_num(m, v), 1)
        self.assertEquals(g.path_num(n, v), 3)
        self.assertEquals(g.path_num(o, v), 3)
        self.assertEquals(g.path_num(p, v), 4)
        self.assertEquals(g.path_num(q, v), 0)
        self.assertEquals(g.path_num(r, v), 1)
        self.assertEquals(g.path_num(s, v), 1)
        self.assertEquals(g.path_num(t, v), 0)
        self.assertEquals(g.path_num(u, v), 0)
        self.assertEquals(g.path_num(v, v), 1)
        self.assertEquals(g.path_num(w, v), 0)
        self.assertEquals(g.path_num(x, v), 0)
        self.assertEquals(g.path_num(y, v), 1)
        self.assertEquals(g.path_num(z, v), 0)
    def testSCC(self):
        a = Vertex('a')        
        b = Vertex('b')        
        c = Vertex('c')        
        d = Vertex('d')        
        e = Vertex('e')        
        f = Vertex('f')        
        g = Vertex('g')        
        h = Vertex('h')        
        vertices = [a, b, c, d, e, f, g, h]
        edges = [(e, a), (a, b), (b, c), (d, c), (c, d), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h), (h, h)]    
        G = Graph(vertices, edges)
        G.strongly_connected_components()
        self.assertEquals(a.cc, 1)
        self.assertEquals(b.cc, 1)
        self.assertEquals(c.cc, 2)
        self.assertEquals(d.cc, 2)
        self.assertEquals(e.cc, 1)
        self.assertEquals(f.cc, 3)
        self.assertEquals(g.cc, 3)
        self.assertEquals(h.cc, 4)
    def testSimplified(self):
        a = Vertex('a')        
        b = Vertex('b')        
        c = Vertex('c')        
        d = Vertex('d')        
        e = Vertex('e')        
        f = Vertex('f')        
        g = Vertex('g')        
        h = Vertex('h')        
        vertices = [a, b, c, d, e, f, g, h]
        #edges = [(a, c), (b, a), (d, h), (d, f), (e, a), (a, b), (b, c), (d, c), (c, d), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h), (h, h)]    
        edges = [(e, a), (a, b), (b, c), (d, c), (c, d), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h), (h, h)]    
        G = Graph(vertices, edges)
        s = G.simplified()
#        for u in s.vertices:
#            print "u.key: {}, u.cc: {}".format(u.key, u.cc)    
#            s.printEdge(u)
        a = Vertex('a')    
        b = Vertex('b')    
        c = Vertex('c')    
        d = Vertex('d')    
        e = Vertex('e')    
        f = Vertex('f')    
        vertices = [a, b, c, d, e, f]
        edges = [(a, b), (b, a), (b, c), (b, d), (c, b), (d, b), (c, e), (b, e), (d, f), (e, f), (f, e)]
        G = Graph(vertices, edges)
        s = G.simplified()
        #for u in s.vertices:
        #    print "u.key: {}, u.cc: {}".format(u.key, u.cc)    
        #    s.printEdge(u)
    def testComponentGraph(self):
        a = Vertex('a')        
        b = Vertex('b')        
        c = Vertex('c')        
        d = Vertex('d')        
        e = Vertex('e')        
        f = Vertex('f')        
        g = Vertex('g')        
        h = Vertex('h')        
        vertices = [a, b, c, d, e, f, g, h]
        edges = [(e, a), (a, b), (b, c), (d, c), (c, d), (d, h), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h), (h, h)]    
        G = Graph(vertices, edges)
        cg = G.component_graph()
#        print
#        for u in cg.vertices:
#            print "u.key: {}".format(u.key)    
#            cg.printEdge(u)
        a = Vertex('a')    
        b = Vertex('b')    
        c = Vertex('c')    
        d = Vertex('d')    
        e = Vertex('e')    
        f = Vertex('f')    
        vertices = [a, b, c, d, e, f]
        edges = [(a, b), (b, a), (b, c), (b, d), (c, b), (d, b), (c, e), (b, e), (d, f), (e, f), (f, e)]
        G = Graph(vertices, edges)
        cg = G.component_graph()
#        print "www"
#        print
#        for u in cg.vertices:
#            print "u.key: {}".format(u.key)    
#            cg.printEdge(u)
    def testSemiconnected(self):
        a = Vertex('a')        
        b = Vertex('b')        
        c = Vertex('c')        
        d = Vertex('d')        
        e = Vertex('e')        
        f = Vertex('f')        
        g = Vertex('g')        
        h = Vertex('h')        
        vertices = [a, b, c, d, e, f, g, h]
        edges = [(e, a), (a, b), (b, c), (d, c), (c, d), (d, h), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h), (h, h)]    
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), True)
        a = Vertex('a')    
        b = Vertex('b')    
        c = Vertex('c')    
        d = Vertex('d')    
        e = Vertex('e')    
        f = Vertex('f')    
        vertices = [a, b, c, d, e, f]
        edges = [(a, b), (b, a), (b, c), (b, d), (c, b), (d, b), (c, e), (b, e), (d, f), (e, f), (f, e)]
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), True)
        edges = [(a, b), (b, a), (b, c), (b, d), (c, b), (d, b), (e, f)]
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), False)
        abe = Vertex('abe')    
        cd = Vertex('cd')    
        fg = Vertex('fg')    
        h =  Vertex('h')    
        vertices = [abe, cd, fg, h]
        edges = [(abe, fg), (abe, cd), (fg, h), (cd, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), True)
        edges = [(abe, fg), (abe, cd), (fg, h), (cd, h)]
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), False)
        edges = [(abe, fg), (abe, cd), (cd, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), False)
        edges = [(abe, fg), (abe, cd), (fg, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), True)
        edges = [(abe, cd), (fg, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEquals(G.semiconnected(), True)
    def testCut(self):
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        d = Vertex('d')
        e = Vertex('e')
        f = Vertex('f')
        g = Vertex('g')
        h = Vertex('h')
        i = Vertex('i')
        vertices = [a, b, c, d, e, f, g, h, i]
        edges = [(a, b), (b, c), (b, h), (c, i), (d, c), (e, d), (f, d), (f, e), (f, c), (g, f), (g, h), (g, i), (h, a), (h, i)]
        G = Graph(vertices, edges, directed = False)
        #weight = [4, 8, 11, 2, 7, 9, 14, 10, 4, 2, 2, 1, 8, 7]
        weight = [4, 8, 11, 2, 7, 9, 14, 10, 4, 2, 1, 6, 8, 7]
        z = dict()
        for x,y in zip(edges, weight):
            z[x] = y    
            z[(x[1], x[0])] = y
        def w(x, y):
            return z[(x, y)]        
        G.cut(a, h, w)
        r1 = set()
        r2 = set()
        for u in G.vertices:
            if u.root == a:
                r1.add(u)
            else:
                r2.add(u)
        self.assertEquals(r1, set([a, b]))
        self.assertEquals(r2, set([h, i, g, c, f, d, e]))
#        for u in G.vertices:
#            print "u.key: {}, u.root = {}".format(u.key, u.root)
    def testKruskal(self):
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        d = Vertex('d')
        e = Vertex('e')
        f = Vertex('f')
        g = Vertex('g')
        h = Vertex('h')
        i = Vertex('i')
        vertices = [a, b, c, d, e, f, g, h, i]
        edges = [(a, b), (a, h), (b, a), (b, c), (b, h), (c, b), (c, i), (c, f), (c, d), (d, c), (d, e), (d, f), (e, d), (e, f), (f, d), (f, e), (f, c), (f, g), (g, f), (g, h), (g, i), (h, a), (h, b), (h, i), (h, g), (i, c), (i, h), (i, g)]
        G = Graph(vertices, edges)
        weight = [4, 8, 4, 8, 11, 8, 2, 4, 7, 7, 9, 14, 9, 10, 14, 10, 4, 2, 2, 1, 6, 8, 11, 7, 1, 2, 7, 6]
        z = dict()
        for x,y in zip(edges, weight):
            z[x] = y    
            print "{}: {}".format(x, y)
        def w(x, y):
            return z[(x, y)]        
        ls = G.Kruskal(w)
        print ls
    def testPrim(self):
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        d = Vertex('d')
        e = Vertex('e')
        f = Vertex('f')
        g = Vertex('g')
        h = Vertex('h')
        i = Vertex('i')
        vertices = [a, b, c, d, e, f, g, h, i]
        #edges = [(a, b), (a, h), (b, a), (b, c), (b, h), (c, b), (c, i), (c, f), (c, d), (d, c), (d, e), (d, f), (e, d), (e, f), (f, d), (f, e), (f, c), (f, g), (g, f), (g, h), (g, i), (h, a), (h, b), (h, i), (h, g), (i, c), (i, h), (i, g)]
        #weight = [4, 8, 4, 8, 11, 8, 2, 4, 7, 7, 9, 14, 9, 10, 14, 10, 4, 2, 2, 1, 6, 8, 11, 7, 1, 2, 7, 6]
        edges = [(a, b), (b, c), (b, h), (c, i), (d, c), (e, d), (f, d), (f, e), (f, c), (g, f), (g, h), (g, i), (h, a), (h, i)]
        weight = [4, 8, 11, 2, 7, 9, 14, 10, 4, 2, 1, 6, 8, 7]
        G = Graph(vertices, edges, False)
        z = dict()
        for x,y in zip(edges, weight):
            z[x] = y    
            z[(x[1], x[0])] = y
            #print "Prim edges: {}, weight: {}".format(x, y)
        def w(x, y):
            return z[(x, y)]        
        G.Prim(w, i)
        s = set()
        for u in G.vertices:
            s.add((u.p, u))    
#        self.assertEquals(s, set([(g, h), (f, g), (None, i), (c, d), (c, f), (i, c), (h, a), (d, e), (a, b)])) 
    def testBellmanFord(self):
        s = Vertex('s')
        t = Vertex('t')
        y = Vertex('y')
        x = Vertex('x')
        z = Vertex('z')
        vertices = [s, t, y, x, z]
        edges = [(s, t), (s, y), (t, y), (t, x), (t, z), (y, x), (y, z), (x, t), (z, s), (z, x)]
        weight = [6, 7, 8, 5, -4, -3, 9, -2, 2, 7]
        G = Graph(vertices, edges)
        we = dict()
        for x,y in zip(edges, weight):
            we[x] = y    
        def w(x, y):
            return we[(x, y)]        
        G.Bellman_Ford(w, z)
    def testBellmanFordModified(self):
        s = Vertex('s')
        t = Vertex('t')
        u = Vertex('u')
        v = Vertex('v')
        x = Vertex('x')
        y = Vertex('y')
        vertices = [s, t, u, v, x, y]
        edges = [(s, t), (s, v), (s, x), (s, y), (t, u), (v, u)]
        weight = [1, 0, 3, 4, 2, 6]
        G = Graph(vertices, edges)
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
#        G.Bellman_Ford(w, s)
        G.Bellman_Ford_modified(w, s)
        self.assertEquals([i.p for i in vertices], [None, s, t, s, s, s])
        self.assertEquals([i.d for i in vertices], [0, 1, 3, 0, 3, 4])
        r = Vertex('r')    
        s = Vertex('s')    
        t = Vertex('t')    
        x = Vertex('x')    
        y = Vertex('y')    
        z = Vertex('z')    
        vertices = [r, s, t, x, y, z]
        edges = [(r, s), (r, t), (s, t), (s, x), (t, x), (t, y), (t, z), (x, y), (x, z), (y, z)]
        weight = [5, 3, 2, 6, 7, 4, 2, -1, 1, -2]
        G = Graph(vertices, edges)
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
        G.Bellman_Ford_modified(w, s)
        self.assertEquals([i.p for i in vertices], [None, None, s, s, x, y])
        self.assertEquals([i.d for i in vertices], [float("Inf"), 0, 2, 6, 5, 3])
    def testTopologicalSort(self):
        r = Vertex('r')    
        s = Vertex('s')    
        t = Vertex('t')    
        x = Vertex('x')    
        y = Vertex('y')    
        z = Vertex('z')    
        vertices = [r, s, t, x, y, z]
        edges = [(r, s), (r, t), (s, t), (s, x), (t, x), (t, y), (t, z), (x, y), (x, z), (y, z)]
        weight = [5, 3, 2, 6, 7, 4, 2, -1, 1, -2]
        G = Graph(vertices, edges)
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
        l = G.topological_sort()
        self.assertEquals(l, [r, s, t, x, y, z])
    def testDagShortestPaths(self):
        r = Vertex('r')    
        s = Vertex('s')    
        t = Vertex('t')    
        x = Vertex('x')    
        y = Vertex('y')    
        z = Vertex('z')    
        vertices = [r, s, t, x, y, z]
        edges = [(r, s), (r, t), (s, t), (s, x), (t, x), (t, y), (t, z), (x, y), (x, z), (y, z)]
        weight = [5, 3, 2, 6, 7, 4, 2, -1, 1, -2]
        G = Graph(vertices, edges)
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
        G.dag_shortest_paths(w, s)
        self.assertEquals([i.p for i in vertices], [None, None, s, s, x, y])
        self.assertEquals([i.d for i in vertices], [float("Inf"), 0, 2, 6, 5, 3])
        G.dag_shortest_paths(w, r)
        self.assertEquals([i.p for i in vertices], [None, r, r, t, t, t])
        self.assertEquals([i.d for i in vertices], [0, 5, 3, 10, 7, 5])
    def TestDagShortestPathsModified(self):
        u = Vertex('u')
        v = Vertex('v')
        w = Vertex('w')
        z = Vertex('z')
        u.weight = 1
        v.weight = 2
        w.weight = 3
        z.weight = 4
        vertices = [u, v, w, z]
        edges = [(u, v), (v, w), (v, z)]
        G = Graph(vertices, edges)
        self.assertEquals(dag_shortest_paths_modified(G, u), [u, v, z])
    def testTotalPathNumber(self):
        r = Vertex('r')    
        s = Vertex('s')    
        t = Vertex('t')    
        x = Vertex('x')    
        y = Vertex('y')    
        z = Vertex('z')    
        vertices = [r, s, t, x, y, z]
        edges = [(r, s), (r, t), (s, t), (s, x), (t, x), (t, y), (t, z), (x, y), (x, z), (y, z)]
        weight = [5, 3, 2, 6, 7, 4, 2, -1, 1, -2]
        G = Graph(vertices, edges)
        number = G.total_path_number()
        self.assertEquals([i.num for i in vertices], [21, 12, 7, 3, 1, 0])
        self.assertEquals(number, 44)
    def testDijkstra(self):
        s = Vertex('s')
        t = Vertex('t')
        x = Vertex('x')
        y = Vertex('y')
        z = Vertex('z')
        vertices = [s, t, x, y, z]
        edges = [(s, t), (s, y), (t, x), (t, y), (x, z), (y, t), (y, x), (y, z), (z, s), (z, x)]
        g = Graph(vertices, edges)
        weight = [10, 5, 1, 2, 4, 3, 9, 2, 7, 6]
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
        g.Dijkstra(w, s)
        self.assertEquals([i.p for i in vertices], [None, y, t, s, y])
        self.assertEquals([i.d for i in vertices], [0, 8, 9, 5, 7])
        s = Vertex('s')
        t = Vertex('t')
        x = Vertex('x')
        y = Vertex('y')
        z = Vertex('z')
        vertices = [s, t, x, y, z]
        edges = [(s, t), (s, y), (t, x), (t, y), (x, z), (y, t), (y, x), (y, z), (z, s), (z, x)]
        g = Graph(vertices, edges)
        weight = [3, 5, 6, 2, 2, 1, 4, 6, 3, 7]
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
        g.Dijkstra(w, s)
        self.assertEquals([i.p for i in vertices], [None, s, t, s, y])
        self.assertEquals([i.d for i in vertices], [0, 3, 9, 5, 11])
        g.Dijkstra(w, z)
        self.assertEquals([i.p for i in vertices], [z, s, z, s, None])
        self.assertEquals([i.d for i in vertices], [3, 6, 7, 8, 0])
    def testDijkstraModified(self):
        s = Vertex('s')
        t = Vertex('t')
        x = Vertex('x')
        y = Vertex('y')
        z = Vertex('z')
        vertices = [s, t, x, y, z]
        edges = [(s, t), (s, y), (t, x), (t, y), (x, z), (y, t), (y, x), (y, z), (z, s), (z, x)]
        g = Graph(vertices, edges)
        weight = [10, 5, 1, 2, 4, 3, 9, 2, 7, 6]
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
        g.Dijkstra_modified(w, s, 10)
        self.assertEquals([i.p for i in vertices], [None, y, t, s, y])
        self.assertEquals([i.d for i in vertices], [0, 8, 9, 5, 7])
        s = Vertex('s')
        t = Vertex('t')
        x = Vertex('x')
        y = Vertex('y')
        z = Vertex('z')
        vertices = [s, t, x, y, z]
        edges = [(s, t), (s, y), (t, x), (t, y), (x, z), (y, t), (y, x), (y, z), (z, s), (z, x)]
        g = Graph(vertices, edges)
        weight = [3, 5, 6, 2, 2, 1, 4, 6, 3, 7]
        we = dict()
        for i,j in zip(edges, weight):
            we[i] = j    
        def w(x, y):
            return we[(x, y)]        
        g.Dijkstra_modified(w, s, 7)
        self.assertEquals([i.p for i in vertices], [None, s, t, s, y])
        self.assertEquals([i.d for i in vertices], [0, 3, 9, 5, 11])
        g.Dijkstra_modified(w, z, 7)
        self.assertEquals([i.p for i in vertices], [z, s, z, s, None])
        self.assertEquals([i.d for i in vertices], [3, 6, 7, 8, 0])
#    def testJohnson(self):
#        a1 = Vertex(1)
#        a2 = Vertex(2)
#        a3 = Vertex(3)
#        a4 = Vertex(4)
#        a5 = Vertex(5)
#        vertices = [a1, a2, a3, a4, a5]
#        edges = [(a1, a2), (a1, a3), (a1, a5), (a2, a4), (a2, a5), (a3, a2), (a4, a1), (a4, a3), (a5, a4)]
#        g = Graph(vertices, edges)
#        weight = [3, 8, -4, 1, 7, 4, 2, -5, 6]
#        we = dict()
#        for i,j in zip(edges, weight):
#            we[i] = j    
#        def w(x, y):
#            return we[(x, y)]        
#        g.Johnson(w)
