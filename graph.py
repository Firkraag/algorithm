from queue import Queue
import disjoint_sets_forest as dsf
import sys
from typing import Iterable, Optional, Tuple, Set, Dict
from enum import Enum

Color = Enum('Color', ('WHITE', 'GREY', 'BLACK'))


class Vertex:
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return f"Vertex({self.key})"

    def print_path(self, v):
        """
        print out the vertices on a shortest path from s to
        v, assuming that BFS has already computed a breadth-first tree
        """
        if self == v:
            print(self)
        elif v.p is None:
            print("No path from {} to {} exists".format(self.key, v.key))
        else:
            self.print_path(v.p)
            print(v)


Vertices = Optional[Iterable[Vertex]]
Edge = Tuple[Vertex, Vertex]
Edges = Optional[Iterable[Edge]]


class Graph:
    def __init__(self, vertices: Optional[Vertices] = None,
                 edges: Optional[Edges] = None, directed: bool = True):
        self.directed: bool = directed
        self.vertices: Set[Vertex] = set() if vertices is None else set(vertices)
        self.edges: Set[Edge] = set()
        self.adj: Dict[Vertex, Set[Vertex]] = dict()
        self._time: int = 0
        for u in self.vertices:
            self.adj[u] = set()
        if edges is not None:
            for u, v in edges:
                self._add_edge(u, v)

    def __eq__(self, graph2: 'Graph'):
        graph1 = self
        return (graph1.directed == graph2.directed) and (graph1.vertices == graph2.vertices) and (
                graph1.edges == graph2.edges)

    def _add_edge(self, u: Vertex, v: Vertex):
        if self.directed:
            self.adj[u].add(v)
            self.edges.add((u, v))
        elif u != v:  # undirected graph does not allow self loop
            self.adj[u].add(v)
            self.edges.add((u, v))
            self.adj[v].add(u)
            self.edges.add((v, u))

    def _add_vertex(self, u: Vertex, edges: Optional[Edges] = None):
        self.vertices.add(u)
        if edges is not None:
            for u, v in edges:
                self._add_edge(u, v)

    def copy(self):
        return Graph(self.vertices, self.edges, self.directed)

    def transpose(self):
        return Graph(self.vertices, [(v, u) for u, v in self.edges], self.directed)

    def bfs(self, s: Vertex):
        for u in self.vertices:
            u.distance = float("Inf")
            u.color = Color.WHITE
            u.parent = None
        s.color = Color.GREY
        s.distance = 0
        s.parent = None
        queue = Queue()
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            for v in self.adj[u]:
                if v.color == Color.WHITE:
                    v.color = Color.GREY
                    v.distance = u.distance + 1
                    v.parent = u
                    queue.put(v)
            u.color = Color.BLACK

    def dfs(self):
        self._time = 0
        for u in self.vertices:
            u.color = Color.WHITE
            u.p = None
        for u in self.vertices:
            if u.color == Color.WHITE:
                self._dfs_visit(u)

    def _dfs_visit(self, u: Vertex):
        self._time += 1
        u.d = self._time
        u.color = Color.GREY
        for v in self.adj[u]:
            if v.color == Color.WHITE:
                v.p = u
                self._dfs_visit(v)
        u.color = Color.BLACK
        self._time += 1
        u.f = self._time

    def is_cyclic(self):
        for u in self.vertices:
            u.color = Color.WHITE
        for u in self.vertices:
            if u.color == Color.WHITE:
                if self._is_cyclic_aux(u):
                    return True
        return False

    def _is_cyclic_aux(self, u):
        u.color = Color.GREY
        for v in self.adj[u]:
            if v.color == Color.WHITE:
                if self._is_cyclic_aux(v):
                    return True
            elif v.color == Color.GREY:
                return True
        u.color = Color.BLACK
        return False

    def topological_sort(self):
        """
        Perform topological sort for dag

        A topological sort of a dag(directed acyclic graph) G = (V, E) is a linear ordering of all the vertices
        such that if G contains an edge (u, v), then u appears before v in the ordering.
        """
        assert (not self.is_cyclic()) and self.directed
        self.dfs()
        return sorted(self.vertices, key=lambda x: x.f, reverse=True)

    def print_all_edges(self):
        s = next(iter(self.vertices))
        self.bfs(s)
        self._print_all_edges_aux(s)

    def _print_all_edges_aux(self, u):
        for v in self.adj[u]:
            if u == v.p:
                print((u, v))
                self._print_all_edges_aux(v)
                print((v, u))
            else:
                pass

    def printAllEdges(self):
        self.status = dict()
        s = next(iter(self.vertices))
        print("key of s is {}".format(s.key))
        self.printAllEdges_aux(s)

    def printAllEdges_aux(self, u):
        for v in self.adj[u]:
            try:
                status = self.status[(u, v)]
            except KeyError:
                self.status[(u, v)] = 1
                self.status[(v, u)] = 1
                print((u, v))
                self.printAllEdges_aux(v)
                print((v, u))

    def path_num(self, s, t):
        """
        A linear-time algorithm that takes as input a directed acyclic graph
        G = (V, E) and two vertices s and t, and returns the number of simple
        paths from s to t in G.
        """
        for u in self.vertices:
            u.color = 0
            u.num = 0
        t.color = 2
        t.num = 1
        return self._path_num_aux(s, t)

    def _path_num_aux(self, s, t):
        s.color = 1
        for v in self.adj[s]:
            if v.color == 2:
                s.num = s.num + v.num
            elif v.color == 0:
                s.num = s.num + self._path_num_aux(v, t)
        s.color = 2
        return s.num

    def strongly_connected_components(self):
        global time, cc
        self.dfs()
        t = self.transpose()
        for u in t.vertices:
            u.color = 0
            u.p = None
        time = 0
        cc = 0
        for u in sorted(self.vertices, key=lambda u: u.f, reverse=True):
            if u.color == 0:
                cc = cc + 1
                t.strongly_connected_components_dfs_visit(u)

    def strongly_connected_components_dfs_visit(self, u):
        global time, cc
        u.cc = cc
        time = time + 1
        u.d = time
        u.color = 1
        for v in self.adj[u]:
            if v.color == 0:
                v.p = u
                self.strongly_connected_components_dfs_visit(v)
        u.color = 2
        time = time + 1
        u.f = time

    def simplified(self):
        """
        create a simplified graph that has the same strong
        connected components and component graph as G and that is as small 
        as possible
        """
        self.dfs()
        t = self.transpose()
        return t.simplified_dfs()

    def simplified_dfs(self):
        global time, cc, status
        status = dict()
        s = Graph(self.vertices)
        for u in self.vertices:
            u.color = 0
            u.p = None
        time = 0
        cc = 0
        for u in sorted(self.vertices, key=lambda u: u.f, reverse=True):
            if u.color == 0:
                stack = []
                cc = cc + 1
                self.simplified_dfs_visit(u, stack, s)
                for i in range(len(stack) - 1):
                    s._add_edge(stack[i], stack[i + 1])
                if len(stack) > 1:
                    s._add_edge(stack[len(stack) - 1], stack[0])
        return s

    def simplified_dfs_visit(self, u, stack, s):
        global time, cc, status
        stack.append(u)
        u.cc = cc
        time = time + 1
        u.d = time
        u.color = 1
        for v in self.adj[u]:
            if v.color == 0:
                v.p = u
                self.simplified_dfs_visit(v, stack, s)
            elif v.color == 2 and v.cc < u.cc:
                try:
                    st = status[(v.cc, u.cc)]
                except KeyError:
                    status[(v.cc, u.cc)] = 1
                    s._add_edge(v, u)
        u.color = 2
        time = time + 1
        u.f = time

    def component_graph(self):
        """
        compute the component graph of a directed graph
        there is at most one edge between two vertices in the component graph
        :return:
        """
        global time, cc, cg, status, vertices_list
        self.dfs()
        t = self.transpose()
        for u in t.vertices:
            u.color = 0
            u.p = None
        time = 0
        cc = 0
        status = dict()
        vertices_list = list()
        cg = Graph()
        for u in sorted(self.vertices, key=lambda u: u.f, reverse=True):
            if u.color == 0:
                cc = cc + 1
                vertices_list.append(Vertex(cc))
                cg._add_vertex(vertices_list[cc - 1])
                t.component_graph_dfs_visit(u)
        return cg

    def component_graph_dfs_visit(self, u):
        global time, cc, cg, vertices_list
        u.cc = cc
        time = time + 1
        u.d = time
        u.color = 1
        for v in self.adj[u]:
            if v.color == 0:
                v.p = u
                self.component_graph_dfs_visit(v)
            elif v.color == 2 and v.cc < u.cc:
                try:
                    st = status[(v.cc, u.cc)]
                except KeyError:
                    status[(v.cc, u.cc)] = 1
                    cg._add_edge(
                        vertices_list[v.cc - 1],
                        vertices_list[u.cc - 1])
        u.color = 2
        time = time + 1
        u.f = time

    def semiconnected(self):
        cg = self.component_graph()
        vertices_list = sorted(cg.vertices, key=lambda u: u.key, reverse=False)
        for i in range(len(vertices_list) - 1):
            if vertices_list[i + 1] not in cg.adj[vertices_list[i]]:
                return False
        return True

    def cut(self, x, y, w):
        """
        For a given edge (x, y) contained in some minimum spanning tree,
        form a minimum spanning tree that contains (x, y) using a method like Prim's algorithm,
        and construct a cut (S, V - S) such that (x, y) is the light edge crossing
        the cut, S = {u: u.root = x}
        """
        for v in self.vertices:
            v.weight = float("Inf")
            v.p = None
            v.root = None
        x.weight = 0
        y.weight = 0
        x.root = x
        y.root = y
        q = min_priority_queue(self.vertices, 'weight')
        while q.heap_size > 0:
            u = q.heap_extract_min()
            for v in self.adj[u]:
                if v in q and w(u, v) < v.weight:
                    v.root = u.root
                    q.heap_decrease_key(v.index, w(u, v))
                    v.p = u

    def alledges_undirected_dfs(self):
        global time, l
        for u in self.vertices:
            u.color = 0
            u.p = None
        time = 0
        l = []
        for u in self.vertices:
            if u.color == 0:
                self.alledges_undirected_dfs_visit(u)
        return l

    def alledges_undirected_dfs_visit(self, u):
        global time, l
        time = time + 1
        u.d = time
        u.color = 1
        for v in self.adj[u]:
            if v.color == 0:
                l.append((u, v))
                v.p = u
                self.alledges_undirected_dfs_visit(v)
            elif v.color == 1 and u.p != v:
                l.append((u, v))
        u.color = 2
        time = time + 1
        u.f = time

    def Kruskal(self, w):
        A = set()
        for v in self.vertices:
            DfsNode(v)
        #        ls = self.alledges_undirected_dfs()
        for u, v in sorted(self.edges, key=lambda x: w(x[0], x[1]), reverse=False):
            if u.index.find_set() != v.index.find_set():
                A = A.union({(u, v)})
                u.index.union(v.index)
        return A

    def Prim(self, w, r):
        """
        G.Prim(weight, root) -- Given weight function
        and an arbitrary vertex root of the graph G, 
        compute minimum spanning tree using Prim's algorithm
        """
        for v in self.vertices:
            v.weight = float("Inf")
            v.p = None
        r.weight = 0
        q = min_priority_queue(self.vertices, 'weight')
        while q.heap_size > 0:
            u = q.heap_extract_min()
            for v in self.adj[u]:
                if v in q and w(u, v) < v.weight:
                    v.p = u
                    q.heap_decrease_key(v.index, w(u, v))

    #    def Prim_vEB(self, w, r, bound):
    #        """G.Prim(weight, root) -- Given weight function
    #        and an arbitrary vertex root of the graph G,
    #        compute minimum spanning tree using Prim's algorithm"""
    #        for v in self.vertices:
    #            v.weight = bound - 1
    #            v.p = None
    #        r.weight = 0
    #        t = vEB_node(bound)
    #        for u in self.vertices:
    #            t.insert(u)
    #        while t.size > 0:
    #            u = t.minimum()
    #            t.delete(u)
    #            for v in self.adj[u]:
    #                if t.member(v) and w(u, v) < v.weight:
    #                    v.p = u
    #                    t.delete(v)
    #                    v.weight = w(u, v)
    #                    t.insert(v)
    def Bellman_Ford(self, w, s):
        """
        The Bellman-Ford algorithm solves the single-source
        shortest-paths problem in the general case in which edge
        weights may be negative.
        If there is a negative-weight cycle that is reachable from 
        the source s, this function returns False and indicates that
        no solution exists.
        If there is no such cycle, this function returns True and produces
        the shortest paths and their weights.
        """
        self.initialize_signle_source(s)
        for i in range(1, len(self.vertices)):
            for u, v in self.edges:
                self.relax(u, v, w)
        for u, v in self.edges:
            if v.d > u.d + w(u, v):
                return False
        return True

    def initialize_signle_source(self, s):
        for v in self.vertices:
            v.d = float("Inf")
            v.p = None
        s.d = 0

    def relax(self, u, v, w):
        if v.d > u.d + w(u, v):
            v.d = u.d + w(u, v)
            v.p = u

    def Bellman_Ford_modified(self, w, s):
        """
        Given a weighted, directed graph G = (V, E) with
        no negative-weight cycles, let m be the maximum
        over all vertices v of the minimum number of edges
        in a shortest path from the source s to v. This variant to
        the Bellman-Ford algorithm terminates in m + 1 passes, even
        if m is not known in advance.
        """
        modified = True
        number = 0
        self.initialize_signle_source(s)
        for i in range(1, len(self.vertices)):
            if modified:
                for u, v in self.edges:
                    number = self.relax_modified(u, v, w) + number
                if number == 0:
                    modified = False
                number = 0
            else:
                break
        for u, v in self.edges:
            if v.d > u.d + w(u, v):
                return False
        return True

    def relax_modified(self, u, v, w):
        if v.d > u.d + w(u, v):
            v.d = u.d + w(u, v)
            v.p = u
            return 1
        else:
            return 0

    def dag_shortest_paths(self, w, s):
        """
        compute shortest paths from a single source
        s for a directed acyclic graph with a weight function w
        """
        l = self.topological_sort()
        self.initialize_signle_source(s)
        for u in l:
            for v in self.adj[u]:
                self.relax(u, v, w)

    def dag_shortest_paths_modified(self, s):
        """
        In the PERT chart analysis, vertices repre
        sent jobs and edges represent sequencing
        contraints; that is, edge (u, v) would
        indicate that job u must be performed
        before job v. The weight attribute of
        every vertex represent the time to 
        perform the job. This variant to 
        DAG-SHORTEST-PATHS algorithm gives a 
        solution to find a longest path in a
        directed acyclic graph with weighted
        vertices in linear time.
        This function return a list of vertices in
        a longest path
        """
        sink = Vertex("sink")
        vertices = self.vertices.union({sink})
        edges = self.edges.union(set([(v, sink) for v in G.vertices]))
        Ga = Graph(vertices, edges)
        Ga.dag_shortest_paths(lambda u, v: -u.weight, s)
        u = sink
        l = []
        while u.p is not None:
            l.append(u.p)
            u = u.p
        return l[::-1]

    def total_path_number(self):
        """
        A algorithm to count the total number of paths in
        a directed acyclic graph
        """
        number = 0
        self._total_path_number_dfs()
        for v in self.vertices:
            number = number + v.num
        return number

    def _total_path_number_dfs(self):
        global time
        for u in self.vertices:
            u.color = 0
            u.p = None
            u.num = 0
        time = 0
        for u in self.vertices:
            if u.color == 0:
                self._total_path_number_dfs_visit(u)

    def _total_path_number_dfs_visit(self, u):
        global time
        time = time + 1
        u.d = time
        u.color = 1
        for v in self.adj[u]:
            if v.color == 0:
                v.p = u
                self._total_path_number_dfs_visit(v)
            u.num = u.num + v.num + 1
        u.color = 2
        time = time + 1
        u.f = time

    def Dijkstra(self, w, s):
        """
        Dijkstra's algorithm solves the single-source shortest-paths problem
        on a weighted, directed graph G = (V, E) for the case in which all edge
        weights are nonnegative.
        """
        self.initialize_signle_source(s)
        S = set()
        Q = min_priority_queue(self.vertices, 'd')
        while Q.heap_size > 1:
            u = Q.heap_extract_min()
            S = S.union({u})
            for v in self.adj[u]:
                if v.d > u.d + w(u, v):
                    v.d = u.d + w(u, v)
                    v.p = u
                    Q.heap_decrease_key(v.index, u.d + w(u, v))

    def Dijkstra_modified(self, w, s, W):
        """
        A algorithm to the the case when the values of 
        the weight function w is in the range {0, 1, ..., W}
        for some nonnegative integer W.
        """
        self.initialize_signle_source(s)
        A = []
        for i in range(W * len(self.vertices) + 1):
            A.append(set())
        A[0].add(s)
        i = 0
        S = set()
        while True:
            while i <= W * len(self.vertices) and len(A[i]) == 0:
                i = i + 1
            if i > W * len(self.vertices):
                break
            print("i = {}".format(i))
            u = A[i].pop()
            print(u)
            print(A[i])
            S.add(u)
            for v in self.adj[u]:
                if v.d > u.d + w(u, v):
                    if v.d < float("Inf"):
                        A[int(v.d)].remove(v)
                    v.d = u.d + w(u, v)
                    A[int(v.d)].add(v)
                    v.p = u

    def single_edge(self):
        """
        An algorithm that given an adjacency-list representation
        of a multigraph G = (V, E), compute the adjacency-list 
        representation of the "equivalent" undirected graph 
        G2 = (V, E2), where E2 consists of
        the edges in E with all multiple edges between two vertices
        replaced by a single edge and with all self-loops removed
        """
        return Graph(self.vertices, self.edges, directed=False)

    def union(self, G2):
        if self.directed != G2.directed:
            print("The two graphs must be either both directed graphs or both undirected graphs")
            return None
        vertices = self.vertices | G2.vertices
        edges = self.edges | G2.edges
        return Graph(vertices, edges, directed=self.directed)

    def square(self):
        """
        The square of a directed graph G = (V, E) is the graph 
        G^2 = (V, E^2) such that (u, v) belongs to E^2 
        if and only if G contains a path with at most 
        two edges between u and v.
        """
        sqrt = self.copy()
        for u in self.vertices:
            for v in self.adj[u]:
                for w in self.adj[v]:
                    sqrt._add_edge(u, w)
        return sqrt

    def height(self, u):
        maximum = 0
        print(u.key)
        for v in self.adj[u]:
            if v.p == u:
                maximum = max(maximum, self.height(v) + 1)
        u.h = maximum
        print(u.key, u.h)
        return u.h

    def mht(self):
        s = next(iter(self.vertices))
        self.bfs(s)
        self.height(s)
        s.mh = s.h
        for u in self.adj[s]:
            self._mht_aux(u)

    def _mht_aux(self, u):
        u.mh = max(u.h, u.p.mh + 1)
        for v in self.adj[u]:
            if v.p == u:
                self._mht_aux(v)


class DfsNode(dsf.node):
    def __init__(self, key):
        self.key = key
        key.index = self
        self.p = self
        self.rank = 0
        self.child = []


class max_heap(list):
    def __init__(self, data, attr):
        list.__init__(self, data)
        for i in range(len(data)):
            self[i].index = i
        self.length = len(data)
        self.attr = attr
        self.heap_size = self.length
        self.build_max_heap()

    def __contains__(self, y):
        return y in self[0:self.heap_size]

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= (self.heap_size - 1)) and (self[l].__dict__[self.attr] > self[i].__dict__[self.attr]):
            largest = l
        else:
            largest = i
        if (r <= (self.heap_size - 1)) and (self[r].__dict__[self.attr] > self[largest].__dict__[self.attr]):
            largest = r
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self[i].index = i
            self[largest].index = largest
            self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_size = self.length
        for i in range(self.length // 2 - 1, -1, -1):
            self.max_heapify(i)


class max_priority_queue(max_heap):
    def heap_maximum(self):
        return self[0]

    def heap_extract_max(self):
        if self.heap_size < 1:
            sys.exit("heap underflow")
        maximum = self[0]
        self[0] = self[self.heap_size - 1]
        self[0].index = 0
        self.heap_size = self.heap_size - 1
        self.max_heapify(0)
        return maximum

    def heap_increase_key(self, i, key):
        if key < self[i].__dict__[self.attr]:
            sys.exit("new key is smaller than current key")
        self[i].__dict__[self.attr] = key
        while i > 0 and self[self.parent(i)].__dict__[self.attr] < self[i].__dict__[self.attr]:
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            self[i].index = i
            self[self.parent(i)].index = self.parent(i)
            i = self.parent(i)

    def max_heap_insert(self, element):
        if self.heap_size >= self.length:
            sys.exit("heap overflow")
        self.heap_size = self.heap_size + 1
        self[self.heap_size - 1] = element
        element.index = self.heap_size - 1
        key = element.__dict__[self.attr]
        element.__dict__[self.attr] = float("-Inf")
        self.heap_increase_key(self.heap_size - 1, key)


class min_heap(list):
    def __init__(self, data, attr):
        """
        data: input data for heap
        attr: the attribute of input date used as compare key
        """
        list.__init__(self, data)
        for i in range(len(data)):
            self[i].index = i
        self.attr = attr
        self.length = len(data)
        self.heap_size = self.length
        self.build_min_heap()

    def __contains__(self, y):
        return y in self[0:self.heap_size]

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= (self.heap_size - 1)) and (self[l].__dict__[self.attr] < self[i].__dict__[self.attr]):
            smallest = l
        else:
            smallest = i
        if (r <= (self.heap_size - 1)) and (self[r].__dict__[self.attr] < self[smallest].__dict__[self.attr]):
            smallest = r
        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self[i].index = i
            self[smallest].index = smallest
            self.min_heapify(smallest)

    def build_min_heap(self):
        self.heap_size = self.length
        for i in range(self.length // 2 - 1, -1, -1):
            self.min_heapify(i)


class min_priority_queue(min_heap):
    def heap_minimum(self):
        return self[0]

    def heap_extract_min(self):
        if self.heap_size < 1:
            sys.exit("heap underflow")
        minimum = self[0]
        self[0] = self[self.heap_size - 1]
        self[0].index = 0
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return minimum

    def heap_decrease_key(self, i, key):
        if key > self[i].__dict__[self.attr]:
            sys.exit("new key is larger than current key")
        self[i].__dict__[self.attr] = key
        while i > 0 and self[self.parent(i)].__dict__[self.attr] > self[i].__dict__[self.attr]:
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            self[i].index = i
            self[self.parent(i)].index = self.parent(i)
            i = self.parent(i)

    def min_heap_insert(self, element):
        if self.heap_size >= self.length:
            sys.exit("heap overflow")
        self.heap_size = self.heap_size + 1
        self[self.heap_size - 1] = element
        element.index = self.heap_size - 1
        key = element.__dict__[self.attr]
        element.__dict__[self.attr] = float("Inf")
        self.heap_decrease_key(self.heap_size - 1, key)
