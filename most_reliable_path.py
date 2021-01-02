from graph import max_priority_queue


def most_reliable_path(G, r, s):
    """
    We are given a directed graph G = (V, E) on which
    each edge (u, v) that belongs to E has an associated
    value r(u, v), which is a real number in the range
    0 <= r(u, v) <= 1 that represents the reliability
    of a communication channel from vertex u to vertex v.
    We interpret r(u, v) as the probability that the channel
     from u to v will not fail, and we assume that these
     probabilities are independent.
     This is an algorithm to find the most reliable
     path from the source to other vertices.

     s: the source
     r: the function that returns the probability that the
     channel from u to v will not fail.
    """
    initialize_single_source(G, s)
    S = set()
    Q = max_priority_queue(G.vertices, 'r')
    while Q.heap_size > 0:
        u = Q.heap_extract_max()
        S = S.union({u})
        for v in G.adj[u]:
            if v.r < u.r * r(u, v):
                v.r = u.r * r(u, v)
                v.p = u
                Q.heap_increase_key(v.index, u.r * r(u, v))


def initialize_single_source(G, s):
    for v in G.vertices:
        v.r = 0
        v.p = None
    s.r = 1
