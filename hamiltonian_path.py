#!/usr/bin/env python


def hamiltonian_path(G, u, v):
    """
    An algorithm to the hamiltonian-path problem on directed acyclic graphs
    """
    we = dict()
    for i in G.edges:
        we[i] = -1

    def w(x, y):
        return we[(x, y)]

    G.dag_shortest_paths(w, u)
    if abs(v.d) == len(G.vertices) - 1:
        return True
    else:
        return False
