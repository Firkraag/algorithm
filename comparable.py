#!/usr/bin/env python

def comparable(a, b, x):
    """
    Given two segments a and b that are comparable at x, determine whether a is above b or not. Assume that neither segment is vertical
    """

    p1 = a[0]
    p2 = a[1]
    p3 = b[0]
    p4 = b[1]
    x4 = p4[0]
    x3 = p3[0]
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (
        (x4 - x3) * (p2[0] - p4[0]) + (x4 - x) * (p4[0] - p3[0]),
        (x4 - x3) * (p2[1] - p4[1]) + (x4 - x) * (p4[1] - p3[1]))
    result = v1[0] * v2[1] - v2[0] * v1[1]
    if result == 0:
        print("a intersects b at the vertical line")
    elif result > 0:
        print("a is above b")
    else:
        print("b is above a")
