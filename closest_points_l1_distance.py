#!/usr/bin/env ipython

from math import ceil, sqrt
from heap import max_heap

def x_sort(S):
    X = max_heap(S)
    X.heapsort()
    return X
def y_sort(S):
    Y = []
    for p in S:
        Y.append((p[1], p[0]))
    YY = max_heap(Y)
    YY.heapsort()
    Y = []
    for i in range(0, len(YY)):
        Y.append((YY[i][1], YY[i][0]))
    return Y
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def brute_force(P):
    P = list(P)
    d = float("Inf")
    for i in range(0, len(P)):
        for j in range(i + 1, len(P)):
            d = min(d, distance(P[i], P[j]))
    return d
def closest_points(S):
    X = x_sort(S)
    Y = y_sort(S)
    return closest_points_aux(S, X, Y)
def closest_points_aux(P, X, Y):
    length = len(P)
    half = int(ceil(length / 2))
    if length <= 3:
        return brute_force(P)
    XL = X[:half]
    XR = X[half:]
    PL = set(XL)
    PR = set(XR)
    l = X[half - 1][0]
    YL = []
    YR = []
    for i in range(0, len(Y)):
        if Y[i] in PL:
            YL.append(Y[i])
        else:
            YR.append(Y[i])
    dl = closest_points_aux(PL, XL, YL)
    dr = closest_points_aux(PR, XR, YR)
    d1 = min(dl, dr)
    YY = []
    for i in range(0, len(Y)):
        if abs(Y[i][0] - l) < d1:
            YY.append(Y[i])
    d2 = float("Inf")
    for i in range(0, len(YY)):
        for j in range(1, 10):
            if i + j < len(YY):
                d2 = min(distance(YY[i], YY[i + j]), d2)
    return min(d1, d2)
