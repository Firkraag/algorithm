#!/usr/bin/env ipython

def universal_sink(M):
    '''
    An algorithm to determine whether a directed graph G contains
    a universal sink---a vertex with in-degree |V| - 1 and
    out-degree 0---in time O(V), given an adjacency matrix for G
    
    M: numpy matrix, the adjacency matrix for the graph
    rtype: vertex index if G contains a universal sink, otherwise, return None
    '''

    return universal_sink_aux(M, 1)

def universal_sink_aux(M, i):
    '''
    M: numpy matrix
    i: vertex index
    '''
    size = M.shape[0]
    j = i
    while True:
        if j > size or M[i - 1][j - 1] != 0:
            break
        j = j + 1
    if j > size:
        for j in range(1, i):
            if M[i - 1][j - 1] != 0:
                return None
        for j in range(1, size + 1):
            if M[j - 1][i - 1] == 0 and j != i:
                return None
        return  i
    else:
        return universal_sink_aux(M, j)
