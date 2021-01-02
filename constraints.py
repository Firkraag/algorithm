from graph import Vertex, Graph
from random import sample


def Bellman_Ford(G, w, s):
    """A variant to the original Bellman_Ford algorithm
    that we use to solve a system of difference constraints
    with m inequalities on n unknowns. The running time is
    O(nm), faster than O(n * n + nm) of the original Bellman-Ford
    algorithm.
    """
    edges = G.edges - set([(s, v) for v in G.adj[s]])
    G.initialize_signle_source(s)
    j = 1
    for i in range(1, len(G.vertices)):
        if j == 1:
            for u, v in G.edges:
                G.relax(u, v, w)
        else:
            for u, v in edges:
                G.relax(u, v, w)
        j = j + 1
    for u, v in G.edges:
        if v.d > u.d + w(u, v):
            return False
    return True


def initialize_signle_source(self, s):
    for v in self.vertices:
        v.d = float("Inf")
        v.p = None
    s.d = 0


def difference_constraints(A, b):
    """A algorithm to solve a system of difference constraints Ax <= b
    by solving a single-source shortest-paths problem using Bellman-Ford
    algorithm.  Each row of the linear-programming matrix A contains
    one 1 and one 1, and all other entries of A are 0.

    Calling convention: A is a two-dimensional list, b is a list.
    Return value: This function returns a list representing x if
    there exists feasible solution; otherwise, this function returns None.
    """

    row = len(A)
    col = len(A[0])
    vertices_num = col
    vertices = []
    edges = []
    weights = dict()
    for i in range(0, vertices_num + 1):
        vertices.append(Vertex(i))
    for i in range(1, vertices_num + 1):
        edges.append((vertices[0], vertices[i]))
        weights[(vertices[0], vertices[i])] = 0
    for i in range(0, row):
        u = A[i].index(-1) + 1
        v = A[i].index(1) + 1
        edges.append((vertices[u], vertices[v]))
        weights[(vertices[u], vertices[v])] = b[i]
    G = Graph(vertices, edges)
    if G.Bellman_Ford(lambda x, y: weights[(x, y)], vertices[0]):
        return [v.d for v in vertices[1:]]
    else:
        return None


def difference_constraints_with_arbitrary_weight(A, b):
    """ An variant to the above difference constraints function
    that the weight of the edge from the auxiliary vertex to any
    other vertex can be arbitrary value.
    """
    row = len(A)
    col = len(A[0])
    vertices_num = col
    vertices = []
    edges = []
    weights = dict()
    distribute = sample(range(-10, 10), vertices_num)
    for i in range(0, vertices_num + 1):
        vertices.append(Vertex(i))
    for i in range(1, vertices_num + 1):
        edges.append((vertices[0], vertices[i]))
        weights[(vertices[0], vertices[i])] = distribute[i - 1]
    for i in range(0, row):
        u = A[i].index(-1) + 1
        v = A[i].index(1) + 1
        edges.append((vertices[u], vertices[v]))
        weights[(vertices[u], vertices[v])] = b[i]
    G = Graph(vertices, edges)
    if G.Bellman_Ford(lambda x, y: weights[(x, y)], vertices[0]):
        return [v.d for v in vertices[1:]]
    else:
        return None


def equality_constraints(A, b):
    row = len(A)
    col = len(A[0])
    vertices_num = col
    vertices = []
    edges = []
    weights = dict()
    for i in range(0, vertices_num + 1):
        vertices.append(Vertex(i))
    for i in range(1, vertices_num + 1):
        edges.append((vertices[0], vertices[i]))
        weights[(vertices[0], vertices[i])] = 0
    for i in range(0, row):
        u = A[i].index(-1) + 1
        v = A[i].index(1) + 1
        edges.append((vertices[u], vertices[v]))
        weights[(vertices[u], vertices[v])] = b[i]
        edges.append((vertices[v], vertices[u]))
        weights[(vertices[v], vertices[u])] = -1 * b[i]
    G = Graph(vertices, edges)
    if G.Bellman_Ford(lambda x, y: weights[(x, y)], vertices[0]):
        return [v.d for v in vertices[1:]]
    else:
        return None


def difference_constraints_without_aux_vertex(A, b):
    row = len(A)
    col = len(A[0])
    vertices_num = col
    vertices = []
    edges = []
    weights = dict()
    for i in range(vertices_num):
        vertices.append(Vertex(i + 1))
    for i in range(0, row):
        u = A[i].index(-1)
        v = A[i].index(1)
        edges.append((vertices[u], vertices[v]))
        weights[(vertices[u], vertices[v])] = b[i]
    G = Graph(vertices, edges)
    if Bellman_Ford_without_aux_vertex(G, lambda x, y: weights[(x, y)]):
        return [v.d for v in vertices]
    else:
        return None


def Bellman_Ford_without_aux_vertex(G, w):
    initialize_signle_source_without_aux_vertex(G)
    for i in range(1, len(G.vertices)):
        for u, v in G.edges:
            G.relax(u, v, w)
    for u, v in G.edges:
        if v.d > u.d + w(u, v):
            return False
    return True


def initialize_signle_source_without_aux_vertex(G):
    for v in G.vertices:
        v.d = 0
        v.p = None


def single_variable_constraints(A, b):
    row = len(A)
    col = len(A[0])
    vertices_num = col
    vertices = []
    edges = []
    weights = dict()
    for i in range(0, vertices_num + 1):
        vertices.append(Vertex(i))
    for i in range(0, row):
        for j in range(0, len(A[i])):
            if A[i][j] == 1:
                edges.append((vertices[0], vertices[j + 1]))
                weights[(vertices[0], vertices[j + 1])] = b[i]
                break
            elif A[i][j] == -1:
                edges.append((vertices[j + 1], vertices[0]))
                weights[(vertices[j + 1], vertices[0])] = b[i]
                break
    G = Graph(vertices, edges)
    if G.Bellman_Ford(lambda x, y: weights[(x, y)], vertices[0]):
        return [v.d for v in vertices[1:]]
    else:
        return None
