#!/usr/bin/ipython

from segment_intersect import segments_intersect

def right_horizontal_ray_intersect(p0, p1, p2):
    '''An algorithm to determine whether a given right horizontal ray from p0 intersects a line segment p1p2'''
    max_x = max(p1[0], p2[0])
    if max_x < p0[0]:
        return False
    # When max(x1, x2) = x0, if intersecting, the intersection point must be po, then po must be on the line segment p1p2
    elif max_x == p0[1]:
        if p1[0] == p2[0] and min(p1[1], p2[1]) <= p0[1] and max(p1[1], p2[1]) >= p0[1]:
            return True
        else:
            return equal(p0, p1) or equal(p0, p2)
    else:
        return segments_intersect(p1, p2, p0, (max_x, p0[1]))
    
def equal(p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]
