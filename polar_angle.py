#!/usr/bin/env python

from heap import MaxHeap


class Vector(object):
    def __init__(self, p2, p1=(0, 0)):
        self.x = p2[0] - p1[0]
        self.y = p2[1] - p1[0]

    def cross_product(self, v):
        return self.x * v.y - v.x * self.y

    def __lt__(self, v):
        return self.cross_product(v) > 0

    def __gt__(self, v):
        return self.cross_product(v) < 0

    def __eq__(self, v):
        return self.cross_product(v) == 0

    def __le__(self, v):
        return self.cross_product(v) >= 0

    def __ge__(self, v):
        return self.cross_product(v) <= 0


def polar_angle(p0, point_list):
    '''sort a sequence <p1, p2, ... , pn> of n points according to
    their polar angles with respect to a given origin point p0.
    '''
    v0 = Vector((p0[0] + 1, p0[1]), p0)  # The polar angle of v0 is 0
    vector_list = [Vector(p, p0) for p in point_list]
    angle_0 = []  # list of vectors whose polar angles are  0
    angle_pi = []  # list of vectors whose polar angles are pi
    # list of vectors whose polar angles are larger than 0 and smaller than pi
    angle_0_pi = []
    # list of vectors whose polar angles are larger than pi and
    # smaller than 2pi
    angle_pi_2pi = []
    for v in vector_list:
        if v == v0:
            if v.x > 0:
                angle_0.append(v)
            elif v.x < 0:
                angle_pi.append(v)
        elif v < v0:
            angle_pi_2pi.append(v)
        elif v > v0:
            angle_0_pi.append(v)
    heap_0_pi = MaxHeap(angle_0_pi)
    heap_pi_2pi = MaxHeap(angle_pi_2pi)
    heap_0_pi.heapsort()
    heap_pi_2pi.heapsort()
    return [(v.x, v.y) for v in (angle_0 + heap_0_pi + angle_pi + heap_pi_2pi)]
