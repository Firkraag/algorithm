#!/usr/bin/env ipython

import synthetic_division as di


def roots_interpolation(roots, n):
    A = [0] * (n + 1)
    if n == 1:
        A[0] = -1 * roots[n - 1]
        A[1] = 1
        return A
    else:
        B = roots_interpolation(roots, n - 1)
        x = roots[n - 1]
        A[n] = B[n - 1]
        for i in range(n - 1, 0, -1):
            A[i] = B[i - 1] - x * B[i]
        A[0] = -1 * x * B[0]
        return A


def Lagrange_interpolation(X, Y, n):
    R = roots_interpolation(X, n)
    #    print( "length of R is {}".format(len(R)))
    A = [0] * n
    for k in range(0, n):
        q, re = di.synthetic_division(R, n + 1, X[k])
        #        print( q)
        #       print( "length of q is {}".format(len(q)))
        m = 1.0
        for j in range(0, n):
            if j != k:
                m = m * (X[k] - X[j])
        #      print( "m = {}".format(m))
        m = Y[k] / m
        #     print( "m = {}".format(m))
        for j in range(0, n):
            A[j] = A[j] + q[j] * m
    return A
