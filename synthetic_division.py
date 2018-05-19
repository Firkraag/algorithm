#!/usr/bin/env ipython


def synthetic_division(A, n, x):
    q = [0] * (n - 1)
    q[n - 2] = A[n - 1]
    for i in range(n - 3, -1, -1):
        q[i] = x * q[i + 1] + A[i + 1]
    r = x * q[0] + A[0]
    return q, r
