#!/usr/bin/env ipython

import sys


def pivot(N, B, A, b, c, v, l, e):
    new_A = dict()
    new_b = dict()
    new_c = dict()
    # Compute the coefficients of the equation for new basic variable
    new_b[e] = b[l] / A[l][e]
    new_A[e] = dict()
    for j in N - {e}:
        new_A[e][j] = A[l][j] / A[l][e]
    new_A[e][l] = 1 / A[l][e]
    # Compute the coefficients of the remaining constraints
    for i in B - {l}:
        new_A[i] = dict()
        new_b[i] = b[i] - A[i][e] * new_b[e]
        for j in N - {e}:
            new_A[i][j] = A[i][j] - A[i][e] * new_A[e][j]
        new_A[i][l] = -1 * A[i][e] * new_A[e][l]
    # Compute the objective function
    new_v = v + c[e] * new_b[e]
    for j in N - {e}:
        new_c[j] = c[j] - c[e] * new_A[e][j]
    new_c[l] = -1 * c[e] * new_A[e][l]
    # Compute new sets of basic and nonbasic variables
    new_N = (N - {e}).union({l})
    new_B = (B - {l}).union({e})
    return new_N, new_B, new_A, new_b, new_c, new_v


def simplex(A, b, c):
    N, B, A, b, c, v = initialize_simplex(A, b, c)
    while True:
        e = None
        for j in sorted(N):
            if c[j] > 0:
                e = j
                break
        if not e:
            break
        minimum = float("Inf")
        for i in sorted(B):
            if A[i][e] > 0:
                delta = b[i] / A[i][e]
                if minimum > delta:
                    l = i
                    minimum = delta
        if minimum == float("Inf"):
            return "unbounded"
        else:
            (N, B, A, b, c, v) = pivot(N, B, A, b, c, v, l, e)
    print(N, B, A, b, c, v)
    n = len(N)
    x = [0] * n
    for i in range(1, n + 1):
        if i in B:
            x[i - 1] = b[i]
    return x


def initialize_simplex(A, b, c):
    m = len(b)
    n = len(c)
    minimum = float("Inf")
    for i in range(0, m):
        if minimum > b[i]:
            k = i + 1
            minimum = b[i]
    if minimum >= 0:
        new_A = dict()
        new_b = dict()
        new_c = dict()
        for i in range(n + 1, n + m + 1):
            new_A[i] = dict()
            for j in range(1, n + 1):
                new_A[i][j] = A[i - n - 1][j - 1]
        for i in range(n + 1, n + m + 1):
            new_b[i] = b[i - n - 1]
        for j in range(1, n + 1):
            new_c[j] = c[j - 1]
        return (set(range(1, n + 1)), set(range(n + 1, n + m + 1)), new_A, new_b, new_c, 0)
    c_original = c
    new_b = dict()
    new_A = dict()
    new_c = dict()
    for i in range(1, m + 1):
        new_b[n + i] = b[i - 1]
        new_A[n + i] = dict()
        new_A[n + i][0] = -1
        for j in range(1, n + 1):
            new_A[n + i][j] = A[i - 1][j - 1]
    for j in range(1, n + 1):
        new_c[j] = 0
    new_c[0] = -1
    A = new_A
    b = new_b
    c = new_c
    N = set(range(0, n + 1))
    B = set(range(n + 1, n + m + 1))
    v = 0
    l = n + k
    (N, B, A, b, c, v) = pivot(N, B, A, b, c, v, l, 0)
    print(N, B, A, b, c, v)
    while True:
        e = None
        print(N)
        for j in sorted(N):
            print("c[{}] = {}".format(j, c[j]))
            if c[j] > 0:
                e = j
                break
        print("e = {}".format(e))
        if not e:
            break
        minimum = float("Inf")
        for i in sorted(B):
            if A[i][e] > 0:
                delta = b[i] / A[i][e]
                if minimum > delta:
                    l = i
                    minimum = delta
        print("l = {}".format(l))
        if minimum == float("Inf"):
            #            return "unbounded"
            break
        else:
            (N, B, A, b, c, v) = pivot(N, B, A, b, c, v, l, e)
            print(N, B, A, b, c, v)
    if abs(v) <= 2.0e-10:
        # if v == 0:
        if 0 in B:
            for e in N:
                if A[0][e] != 0:
                    (N, B, A, b, c, v) = pivot(N, B, A, b, c, v, 0, e)
                    break
        new_A = dict()
        new_c = dict()
        for i in B:
            new_A[i] = dict()
            for j in N - {0}:
                new_A[i][j] = A[i][j]
        v = 0
        c = c_original
        N = N - {0}
        for j in N:
            new_c[j] = 0
        print(N, B, A, b, c, v)
        for i in range(1, n + 1):
            if i in B:
                v = v + c[i] * b[i]
                for j in N:
                    new_c[j] = new_c[j] - c[i] * A[i][j]
            else:
                print("i = {}".format(i))
                print(N)
                print(B)
                print(new_c)
                print(c)
                new_c[i] = new_c[i] + c[i - 1]
        print(N, B, new_A, b, new_c, v)
        return N, B, new_A, b, new_c, v
    else:
        sys.exit("infeasible")
