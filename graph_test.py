#!/usr/bin/env ipython
import unittest
from graph import Vertex, Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graphs = []
        v1 = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)
        v4 = Vertex(4)
        v5 = Vertex(5)
        v6 = Vertex(6)
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.v5 = v5
        self.v6 = v6
        vertices = [v1, v2, v3, v4, v5, v6]
        edges = [(v1, v2), (v1, v3), (v2, v3), (v2, v4), (v2, v5), (v3, v4), (v3, v6), (v4, v5), (v5, v6)]
        self.graphs.append(Graph(vertices, edges))
        edges = [(v1, v2), (v2, v3), (v3, v4), (v4, v2), (v3, v5), (v2, v4), (v4, v3), (v1, v6)]
        self.graphs.append(Graph([v1, v2, v3, v4, v5, v6], edges))

    def tearDown(self):
        pass

    def _buildGraph(self, keys, pairs, directed):
        d = dict()
        vertices = [None] * len(keys)
        edges = [None] * len(pairs)
        for i in range(len(vertices)):
            vertices[i] = Vertex(keys[i])
            d[keys[i]] = vertices[i]

        for i in range(len(edges)):
            w1, w2 = pairs[i]
            edges[i] = (d[w1], d[w2])
        return Graph(vertices, edges, directed)

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
        vertices = [v, r, s, w, t, x, u, y, z]
        edges = [(s, r), (s, w), (r, v), (r, s), (v, r), (w, s), (w, t), (w, x), (t, w), (t, x), (t, u), (u, t), (u, x),
                 (u, y), (x, w), (x, t), (x, u), (x, y), (y, x), (y, u)]
        g = Graph(vertices, edges)
        # g.print(AllEdges())
        # for i in g.vertices:
        #    i.print(Edge())
        #        print()
        g.bfs(s)
        #    g.print(Vertices())
        self.assertEqual(s.d, 0)
        self.assertEqual(r.d, 1)
        self.assertEqual(v.d, 2)
        self.assertEqual(w.d, 1)
        self.assertEqual(t.d, 2)
        self.assertEqual(x.d, 2)
        self.assertEqual(u.d, 3)
        self.assertEqual(y.d, 3)

    def testDfs(self):
        s = Vertex('s')
        v = Vertex('v')
        z = Vertex('z')
        w = Vertex('w')
        y = Vertex('y')
        x = Vertex('x')
        t = Vertex('t')
        u = Vertex('u')
        # edges_list = [(z, w), (s, w), (y, w), (x, ), (x, ), (z, ), (v, u), (v, t)]
        # vertices = (s, v, z, w, y, x, t, u)
        # map(lambda vertex, edges: map(lambda vertex, edge: vertex.addEdge(edge), zip([vertex] * len(edges) , edges)),  zip(vertices, edges_list))
        vertices = [s, v, z, w, y, x, t, u]
        edges = [(y, x), (x, z), (z, y), (z, w), (w, x), (s, z), (s, w), (v, w), (v, s), (t, v), (t, u), (u, v), (u, t)]
        g = Graph(vertices, edges)
        g.dfs()
        vertices = (s, v, z, w, y, x, t, u)

    #        for u in vertices:
    #            print( u, u.d, u.f)
    # df = [(1, 10), (12, 13), (2, 9), (7, 8), (3, 6), (4, 5), (11, 16), (14, 15)]
    # edges_list = [(z, w), (s, w), (y, w), (x, ), (x, ), (z, ), (v, u), (v, t)]
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
        edges = [(m, q), (m, r), (m, x), (n, q), (n, o), (n, u), (o, r), (o, s), (o, v), (p, o), (p, s), (p, z), (q, t),
                 (r, u), (r, y), (s, r), (u, t), (v, w), (v, x), (w, z), (y, v)]
        g = Graph(vertices, edges)
        self.assertEqual(g.path_num(m, v), 1)
        self.assertEqual(g.path_num(n, v), 3)
        self.assertEqual(g.path_num(o, v), 3)
        self.assertEqual(g.path_num(p, v), 4)
        self.assertEqual(g.path_num(q, v), 0)
        self.assertEqual(g.path_num(r, v), 1)
        self.assertEqual(g.path_num(s, v), 1)
        self.assertEqual(g.path_num(t, v), 0)
        self.assertEqual(g.path_num(u, v), 0)
        self.assertEqual(g.path_num(v, v), 1)
        self.assertEqual(g.path_num(w, v), 0)
        self.assertEqual(g.path_num(x, v), 0)
        self.assertEqual(g.path_num(y, v), 1)
        self.assertEqual(g.path_num(z, v), 0)

        g = self.graphs[0]
        self.assertEqual(g.path_num(self.v1, self.v2), 1)
        self.assertEqual(g.path_num(self.v1, self.v3), 2)
        self.assertEqual(g.path_num(self.v1, self.v4), 3)
        self.assertEqual(g.path_num(self.v1, self.v5), 4)
        self.assertEqual(g.path_num(self.v1, self.v6), 6)
        self.assertEqual(g.path_num(self.v2, self.v1), 0)
        self.assertEqual(g.path_num(self.v2, self.v3), 1)
        self.assertEqual(g.path_num(self.v2, self.v4), 2)
        self.assertEqual(g.path_num(self.v2, self.v5), 3)
        self.assertEqual(g.path_num(self.v2, self.v6), 4)
        g = self.graphs[1]
        self.assertEqual(g.path_num(self.v1, self.v5), 1)

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
        self.assertEqual(a.cc, 1)
        self.assertEqual(b.cc, 1)
        self.assertEqual(c.cc, 2)
        self.assertEqual(d.cc, 2)
        self.assertEqual(e.cc, 1)
        self.assertEqual(f.cc, 3)
        self.assertEqual(g.cc, 3)
        self.assertEqual(h.cc, 4)

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
        # edges = [(a, c), (b, a), (d, h), (d, f), (e, a), (a, b), (b, c), (d, c), (c, d), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h), (h, h)]
        edges = [(e, a), (a, b), (b, c), (d, c), (c, d), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h), (h, h)]
        G = Graph(vertices, edges)
        s = G.simplified()
        #        for u in s.vertices:
        #            print( "u.key: {}, u.cc: {}".format(u.key, u.cc)    )
        #            s.print(Edge(u))
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
        # for u in s.vertices:
        #    print( "u.key: {}, u.cc: {}".format(u.key, u.cc)    )
        #    s.print(Edge(u))

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
        edges = [(e, a), (a, b), (b, c), (d, c), (c, d), (d, h), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h),
                 (h, h)]
        G = Graph(vertices, edges)
        cg = G.component_graph()
        #        print()
        #        for u in cg.vertices:
        #            print( "u.key: {}".format(u.key)    )
        #            cg.print(Edge(u))
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

    #        print( "www")
    #        print()
    #        for u in cg.vertices:
    #            print( "u.key: {}".format(u.key)    )
    #            cg.print(Edge(u))
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
        edges = [(e, a), (a, b), (b, c), (d, c), (c, d), (d, h), (b, e), (e, f), (b, f), (g, f), (f, g), (c, g), (g, h),
                 (h, h)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), True)
        a = Vertex('a')
        b = Vertex('b')
        c = Vertex('c')
        d = Vertex('d')
        e = Vertex('e')
        f = Vertex('f')
        vertices = [a, b, c, d, e, f]
        edges = [(a, b), (b, a), (b, c), (b, d), (c, b), (d, b), (c, e), (b, e), (d, f), (e, f), (f, e)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), True)
        edges = [(a, b), (b, a), (b, c), (b, d), (c, b), (d, b), (e, f)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), False)
        abe = Vertex('abe')
        cd = Vertex('cd')
        fg = Vertex('fg')
        h = Vertex('h')
        vertices = [abe, cd, fg, h]
        edges = [(abe, fg), (abe, cd), (fg, h), (cd, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), True)
        edges = [(abe, fg), (abe, cd), (fg, h), (cd, h)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), False)
        edges = [(abe, fg), (abe, cd), (cd, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), False)
        edges = [(abe, fg), (abe, cd), (fg, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), True)
        edges = [(abe, cd), (fg, h), (cd, fg)]
        G = Graph(vertices, edges)
        self.assertEqual(G.semiconnected(), True)

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
        edges = [(a, b), (b, c), (b, h), (c, i), (d, c), (e, d), (f, d), (f, e), (f, c), (g, f), (g, h), (g, i), (h, a),
                 (h, i)]
        G = Graph(vertices, edges, directed=False)
        # weight = [4, 8, 11, 2, 7, 9, 14, 10, 4, 2, 2, 1, 8, 7]
        weight = [4, 8, 11, 2, 7, 9, 14, 10, 4, 2, 1, 6, 8, 7]
        z = dict()
        for x, y in zip(edges, weight):
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
        self.assertEqual(r1, set([a, b]))
        self.assertEqual(r2, set([h, i, g, c, f, d, e]))

    #        for u in G.vertices:
    #            print( "u.key: {}, u.root = {}".format(u.key, u.root))
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
        edges = [(a, b), (a, h), (b, a), (b, c), (b, h), (c, b), (c, i), (c, f), (c, d), (d, c), (d, e), (d, f), (e, d),
                 (e, f), (f, d), (f, e), (f, c), (f, g), (g, f), (g, h), (g, i), (h, a), (h, b), (h, i), (h, g), (i, c),
                 (i, h), (i, g)]
        G = Graph(vertices, edges)
        weight = [4, 8, 4, 8, 11, 8, 2, 4, 7, 7, 9, 14, 9, 10, 14, 10, 4, 2, 2, 1, 6, 8, 11, 7, 1, 2, 7, 6]
        z = dict()
        for x, y in zip(edges, weight):
            z[x] = y
            print("{}: {}".format(x, y))

        def w(x, y):
            return z[(x, y)]

        ls = G.Kruskal(w)
        print(ls)

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
        # edges = [(a, b), (a, h), (b, a), (b, c), (b, h), (c, b), (c, i), (c, f), (c, d), (d, c), (d, e), (d, f), (e, d), (e, f), (f, d), (f, e), (f, c), (f, g), (g, f), (g, h), (g, i), (h, a), (h, b), (h, i), (h, g), (i, c), (i, h), (i, g)]
        # weight = [4, 8, 4, 8, 11, 8, 2, 4, 7, 7, 9, 14, 9, 10, 14, 10, 4, 2, 2, 1, 6, 8, 11, 7, 1, 2, 7, 6]
        edges = [(a, b), (b, c), (b, h), (c, i), (d, c), (e, d), (f, d), (f, e), (f, c), (g, f), (g, h), (g, i), (h, a),
                 (h, i)]
        weight = [4, 8, 11, 2, 7, 9, 14, 10, 4, 2, 1, 6, 8, 7]
        G = Graph(vertices, edges, False)
        z = dict()
        for x, y in zip(edges, weight):
            z[x] = y
            z[(x[1], x[0])] = y
            # print( "Prim edges: {}, weight: {}".format(x, y))

        def w(x, y):
            return z[(x, y)]

        G.Prim(w, i)
        s = set()
        for u in G.vertices:
            s.add((u.p, u))
        #        self.assertEqual(s, set([(g, h), (f, g), (None, i), (c, d), (c, f), (i, c), (h, a), (d, e), (a, b)]))

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
        for x, y in zip(edges, weight):
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
        for i, j in zip(edges, weight):
            we[i] = j

        def w(x, y):
            return we[(x, y)]

        #        G.Bellman_Ford(w, s)
        G.Bellman_Ford_modified(w, s)
        self.assertEqual([i.p for i in vertices], [None, s, t, s, s, s])
        self.assertEqual([i.d for i in vertices], [0, 1, 3, 0, 3, 4])
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
        for i, j in zip(edges, weight):
            we[i] = j

        def w(x, y):
            return we[(x, y)]

        G.Bellman_Ford_modified(w, s)
        self.assertEqual([i.p for i in vertices], [None, None, s, s, x, y])
        self.assertEqual([i.d for i in vertices], [float("Inf"), 0, 2, 6, 5, 3])

    def testTopologicalSort(self):
        r = Vertex('r')
        s = Vertex('s')
        t = Vertex('t')
        x = Vertex('x')
        y = Vertex('y')
        z = Vertex('z')
        vertices = [r, s, t, x, y, z]
        edges = [(r, s), (r, t), (s, t), (s, x), (t, x), (t, y), (t, z), (x, y), (x, z), (y, z)]
        G = Graph(vertices, edges)
        l = G.topological_sort()
        self.assertEqual(l, [r, s, t, x, y, z])

        result = []
        l = [self.v1, self.v2, self.v3, self.v4, self.v5, self.v6]
        result.append(l)
        for i in range(len(self.graphs)):
            self.assertEqual(self.graphs[i].topological_sort(), l)

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
        for i, j in zip(edges, weight):
            we[i] = j

        def w(x, y):
            return we[(x, y)]

        G.dag_shortest_paths(w, s)
        self.assertEqual([i.p for i in vertices], [None, None, s, s, x, y])
        self.assertEqual([i.d for i in vertices], [float("Inf"), 0, 2, 6, 5, 3])
        G.dag_shortest_paths(w, r)
        self.assertEqual([i.p for i in vertices], [None, r, r, t, t, t])
        self.assertEqual([i.d for i in vertices], [0, 5, 3, 10, 7, 5])

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
        self.assertEqual(dag_shortest_paths_modified(G, u), [u, v, z])

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
        self.assertEqual([i.num for i in vertices], [21, 12, 7, 3, 1, 0])
        self.assertEqual(number, 44)

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
        for i, j in zip(edges, weight):
            we[i] = j

        def w(x, y):
            return we[(x, y)]

        g.Dijkstra(w, s)
        self.assertEqual([i.p for i in vertices], [None, y, t, s, y])
        self.assertEqual([i.d for i in vertices], [0, 8, 9, 5, 7])
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
        for i, j in zip(edges, weight):
            we[i] = j

        def w(x, y):
            return we[(x, y)]

        g.Dijkstra(w, s)
        self.assertEqual([i.p for i in vertices], [None, s, t, s, y])
        self.assertEqual([i.d for i in vertices], [0, 3, 9, 5, 11])
        g.Dijkstra(w, z)
        self.assertEqual([i.p for i in vertices], [z, s, z, s, None])
        self.assertEqual([i.d for i in vertices], [3, 6, 7, 8, 0])

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
        for i, j in zip(edges, weight):
            we[i] = j

        def w(x, y):
            return we[(x, y)]

        g.Dijkstra_modified(w, s, 10)
        self.assertEqual([i.p for i in vertices], [None, y, t, s, y])
        self.assertEqual([i.d for i in vertices], [0, 8, 9, 5, 7])
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
        for i, j in zip(edges, weight):
            we[i] = j

        def w(x, y):
            return we[(x, y)]

        g.Dijkstra_modified(w, s, 7)
        self.assertEqual([i.p for i in vertices], [None, s, t, s, y])
        self.assertEqual([i.d for i in vertices], [0, 3, 9, 5, 11])
        g.Dijkstra_modified(w, z, 7)
        self.assertEqual([i.p for i in vertices], [z, s, z, s, None])
        self.assertEqual([i.d for i in vertices], [3, 6, 7, 8, 0])

    def testSingleEdge(self):
        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        d = Vertex(4)
        vertices = [a, b, c, d]
        edges = [(a, b), (b, a), (a, c), (d, d)]
        G = Graph(vertices, edges)
        G2 = G.single_edge()
        edges = set([(a, b), (b, a), (a, c), (c, a)])
        vertices = set(vertices)
        self.assertEqual(G2.vertices, vertices)
        self.assertEqual(G2.edges, edges)
        self.assertEqual(G2.adj[a], {b, c})
        self.assertEqual(G2.adj[b], {a})
        self.assertEqual(G2.adj[c], {a})
        self.assertEqual(G2.adj[d], set())

    def testUnion(self):
        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        d = Vertex(4)
        G1 = Graph([a, b, c], [(a, b), (a, c)])
        G2 = Graph([c, d], [(c, d)])
        G3 = G1.union(G2)
        self.assertEqual(G3.vertices, {a, b, c, d})
        self.assertEqual(G3.edges, {(a, b), (a, c), (c, d)})
        self.assertEqual(G3.adj[a], {b, c})
        self.assertEqual(G3.adj[b], set())
        self.assertEqual(G3.adj[c], {d})
        self.assertEqual(G3.adj[d], set())
        G1 = Graph([a, b, c], [(a, b), (a, c)], directed=False)
        G2 = Graph([c, d], [(c, d)], directed=False)
        G3 = G1.union(G2)
        self.assertEqual(G3.vertices, {a, b, c, d})
        self.assertEqual(G3.edges, {(a, b), (b, a), (a, c), (c, a), (c, d), (d, c)})
        self.assertEqual(G3.adj[a], {b, c})
        self.assertEqual(G3.adj[b], {a})
        self.assertEqual(G3.adj[c], {d, a})
        self.assertEqual(G3.adj[d], {c})

    def testCopy(self):
        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        G1 = Graph([a, b, c], [(a, b), (a, c)])
        G2 = G1.copy()
        self.assertEqual(G1, G2)

    def testSquareGraph(self):
        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        d = Vertex(4)
        G = Graph([a, b, c, d], [(a, b), (a, c), (c, d)])
        sqrt = G.square()
        self.assertEqual(sqrt.vertices, {a, b, c, d})
        self.assertEqual(sqrt.edges, {(a, b), (a, c), (a, d), (c, d)})
        self.assertEqual(sqrt.adj[a], {b, c, d})
        self.assertEqual(sqrt.adj[b], set())
        self.assertEqual(sqrt.adj[c], {d})
        self.assertEqual(sqrt.adj[d], set())
        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        G = Graph([a, b, c], [(a, b), (b, c), (a, c)])
        sqrt = G.square()
        self.assertEqual(G, sqrt)

    def testMht(self):
        print("start mht")
        g = self.graphs[0]
        g.mht()
        print("height")
        print(self.v1.h)
        print(self.v2.h)
        print(self.v3.h)
        print(self.v4.h)
        print(self.v5.h)
        print(self.v6.h)
        print("height")
        print(self.v1.mh)
        print(self.v2.mh)
        print(self.v3.mh)
        print(self.v4.mh)
        print(self.v5.mh)
        print(self.v6.mh)
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
