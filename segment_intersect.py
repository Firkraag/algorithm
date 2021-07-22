#!/usr/bin/env python


def segments_intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)
    if ((d1 > 0 > d2) or (d1 < 0 < d2)) and ((d3 > 0 > d4) or (d3 < 0 < d4)):
        return True
    elif d1 == 0 and on_segment(p3, p4, p1):
        return True
    elif d2 == 0 and on_segment(p3, p4, p2):
        return True
    elif d3 == 0 and on_segment(p1, p2, p3):
        return True
    elif d4 == 0 and on_segment(p1, p2, p4):
        return True
    else:
        return False


def direction(pi, pj, pk):
    v1 = (pk[0] - pi[0], pk[1] - pi[1])
    v2 = (pj[0] - pi[0], pj[1] - pi[1])
    return v1[0] * v2[1] - v2[0] * v1[1]


def on_segment(pi, pj, pk):
    return min(pi[0], pj[0]) <= pk[0] <= max(pi[0], pj[0]) and min(pi[1], pj[1]) <= pk[1] <= max(
        pi[1], pj[1])
