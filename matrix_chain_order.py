#!/usr/bin/env ipython

from numpy import zeros


def bottom_up_matrix_chain_order(p):
    n = len(p) - 1
    m = zeros((n + 1, n + 1))
    s = zeros((n + 1, n + 1))
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i, j] = float("Inf")
            for k in range(i, j):
                q = m[i, k] + m[k + 1, j] + p[i - 1] * p[k] * p[j]
                if q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k
    return m, s


def memoized_matrix_chain_order(p):
    n = len(p) - 1
    m = zeros((n + 1, n + 1))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            m[i, j] = float("Inf")
    return lookup_chain(m, p, 1, n)


def lookup_chain(m, p, i, j):
    if m[i, j] < float("Inf"):
        return m[i, j]
    if i == j:
        m[i, j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + lookup_chain(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[i, j]:
                m[i, j] = q
    return m[i, j]


def print_optimal_parens(s, i, j):
    if i == j:
        print("A{}".format(int(i)), )
    else:
        print("(", )
        print_optimal_parens(s, i, s[i, j])
        print_optimal_parens(s, s[i, j] + 1, j)
        print(")", )


# An incorrect greedy approach for matrix chain order problem
def greedy_matrix_chain_order(p):
    n = len(p) - 1
    return greedy_matrix_chain_order_aux(p, 1, n)


def greedy_matrix_chain_order_aux(p, i, j):
    if i == j:
        return 0
    q = float("Inf")
    for k in range(i, j):
        value = p[i - 1] * p[k] * p[j]
        if q > value:
            q = value
            pos = k
    return greedy_matrix_chain_order_aux(p, i, pos) + greedy_matrix_chain_order_aux(p, pos + 1, j) + q
