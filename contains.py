#!/usr/bin/env ipython

def contains(x, n):
    '''CLRS Exercise 16.2-5
    An algorithm that, given a set {x1, x2, ... ,xn} of points on the
    real line, determines the smallest set of unit-length closed intervals that contains
    all of the given points.'''
    x.sort()
    print x
    i = 0
    a = float("-Inf")
    S = set()
    while i < n:
        if x[i] > a:
            S = S.union({(x[i], x[i] + 1)})
            a = x[i] + 1
        i = i + 1
    print S
    return S
