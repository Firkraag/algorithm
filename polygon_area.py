#!/usr/bin/env python



def polygon_area(P):
    n = len(P)
    S = 0
    for i in range(0, n - 1):
        S = S + (P[i][0] + P[i + 1][0]) * (P[i + 1][1] - P[i][1])
    S = S + (P[0][0] + P[n - 1][0]) * (P[0][1] - P[n - 1][1])
    return 0.5 * abs(S)
