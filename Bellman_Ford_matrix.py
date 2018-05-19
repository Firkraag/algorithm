import numpy as np


def Bellman_Ford_matrix(W, s):
    n = W.shape[0]
    d = [float("Inf")] * n
    p = [None] * n
    d[s - 1] = 0
    for k in range(1, n):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[j - 1] > d[i - 1] + W[i - 1, j - 1]:
                    d[j - 1] = d[i - 1] + W[i - 1, j - 1]
                    p[j - 1] = i
        print(d)
        print(p)
    return d, p


def extend_shortest_paths(L, W):
    n = W.shape[0]
    LW = [float("Inf")] * n
    for j in range(0, n):
        for k in range(0, n):
            LW[j] = min(LW[j], L[k] + W[k, j])
    return LW


def slow_all_pairs_shortest_paths(W, s):
    n = W.shape[0]
    L = [0] * n
    for i in range(0, n):
        if i + 1 == s:
            L[i] = 0
        else:
            L[i] = float("Inf")
    print(L)
    for m in range(1, n):
        L = extend_shortest_paths(L, W)
        print(L)
    return L


def extend_shortest_paths_with_predecessor_subgraph(s, L, P, W):
    n = W.shape[0]
    LW = [float("Inf")] * n
    PP = [None] * n
    for j in range(0, n):
        for k in range(0, n):
            if LW[j] > L[k] + W[k, j]:
                LW[j] = L[k] + W[k, j]
                PP[j] = k + 1
        if LW[j] == L[j]:
            PP[j] = P[j]
    return LW, PP


def slow_all_pairs_shortest_paths_with_predecessor_subgraph(W, s):
    n = W.shape[0]
    L = [float("Inf")] * n
    L[s - 1] = 0
    P = [None] * n
    for m in range(1, n):
        L, P = extend_shortest_paths_with_predecessor_subgraph(s, L, P, W)
        print(L)
        print(P)
    return L, P


def faster_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = W
    m = 1
    while m < n - 1:
        L = extend_shortest_paths(L, L)
        m = 2 * m
        print(m)
        print(L)
    return Ld, p
