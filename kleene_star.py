#!/usr/bin/env python

from numpy import zeros


def kleene_star(x, L, A):
    length = len(x)
    m = zeros((length, length))
    for l in range(1, length + 1):
        for i in range(1, length - l + 2):
            j = i + l - 1
            for k in range(i, j):
                if m[i - 1, k - 1] == 1 and m[k, j - 1] == 1:
                    m[i - 1, j - 1] = 1
            if m[i - 1, j - 1] != 1:
                m[i - 1, j - 1] = A(x[i - 1:j], L)
    if m[0, length - 1] != 0:
        return True
    else:
        return False
