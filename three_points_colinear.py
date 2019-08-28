#!/usr/bin/env ipython

from heap import MaxHeap


class vector(object):
    def __init__(self, p1, p2, p1_index=0, p2_index=0):
        # gurantee that the polar angle of this vector with respect to the origin point is in the range [0, pi)
        if p1[1] > p2[1]:
            self.x = p1[0] - p2[0]
            self.y = p1[1] - p2[1]
        elif p1[1] == p2[1]:
            self.y = 0
            self.x = abs(p1[0] - p2[0])
        else:
            self.x = p2[0] - p1[0]
            self.y = p2[1] - p1[1]
        self.p1 = p1
        self.p2 = p2
        self.p1_index = p1_index
        self.p2_index = p2_index

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


def three_points_colinear(points_list):
    '''An algorithm to determine whether any three points in a set of n points are colinear'''
    n = len(points_list)
    vectors_list = []
    for i in range(n):
        for j in range(i + 1, n):
            vectors_list.append(vector(points_list[i], points_list[j], i, j))
    v0 = vector((1, 0), (0, 0))
    heap_vectors = MaxHeap(vectors_list)
    heap_vectors.heapsort()
    status = [False] * n
    v = heap_vectors[0]
    status[v.p1_index] = True
    status[v.p2_index] = True
    stack = []
    stack.append(v.p1_index)
    stack.append(v.p2_index)
    for i in range(1, len(heap_vectors)):
        v = heap_vectors[i]
        if v == heap_vectors[i - 1]:
            if status[v.p1_index]:
                return True
            elif status[v.p2_index]:
                return True
            else:
                status[v.p1_index] = True
                status[v.p2_index] = True
                stack.append(v.p1_index)
                stack.append(v.p2_index)
        else:
            print(len(stack))
            print(stack)
            for i in range(len(stack)):
                status[stack.pop()] = False
            stack.append(v.p1_index)
            stack.append(v.p2_index)
    return False
