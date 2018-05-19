from graph import min_priority_queue, Vertex, Graph
import numpy as np


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

    :param self:
    :param w:
    :param s:
    :return:
    """
    initialize_signle_source(self, s)
    for i in range(1, len(self.vertices)):
        for u, v in self.edges:
            relax(self, u, v, w)
    for u, v in self.edges:
        if v.d > u.d + w[(u, v)]:
            return False
    return True


def initialize_signle_source(self, s):
    for v in self.vertices:
        v.d = float("Inf")
        v.p = None
    s.d = 0


def relax(self, u, v, w):
    if v.d > u.d + w[u, v]:
        v.d = u.d + w[u, v]
        v.p = u


def Dijkstra(self, w, s):
    '''
    Dijkstra's algorithm solves the single-source shortest-paths problem
    on a weighted, directed graph G = (V, E) for the case in which all edge
    weights are nonnegative.
    '''
    initialize_signle_source(self, s)
    S = set()
    Q = min_priority_queue(self.vertices, 'd')
    while Q.heap_size > 1:
        u = Q.heap_extract_min()
        S = S.union({u})
        for v in self.adj[u]:
            if v.d > u.d + w[u, v]:
                v.d = u.d + w[u, v]
                v.p = u
                Q.heap_decrease_key(v.index, u.d + w[u, v])


def Johnson(self, w):
    G = self
    n = len(G.vertices)
    s = Vertex("s")
    GG = Graph(G.vertices.union({s}), G.edges | set((s, v) for v in G.vertices))
    for v in G.vertices:
        w[(s, v)] = 0
    if not Bellman_Ford(GG, w, s):
        print("the input graph contains a negative-weight cycle")
    else:
        h = dict()
        for v in GG.vertices:
            h[v] = v.d
        # for key,value in h.iteritems():
        #   print(( "h({}) = {}".format(key, value)))
        ww = dict()
        for u, v in GG.edges:
            ww[(u, v)] = w[(u, v)] + h[u] - h[v]
        # for key,value in ww.iteritems():
        #   print(( "ww({}) = {}".format(key, value)))
        D = np.empty((n, n))
        for u in G.vertices:
            Dijkstra(G, ww, u)
            for v in G.vertices:
                D[u.key - 1, v.key - 1] = v.d + h[v] - h[u]
        return D
