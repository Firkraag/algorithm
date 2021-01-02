#!/usr/bin/env python


def polygon_area(polygon):
    n = len(polygon)
    area = 0
    for i in range(n - 1):
        area = area + (polygon[i][0] + polygon[i + 1][0]) * (polygon[i + 1][1] - polygon[i][1])
    area = area + (polygon[0][0] + polygon[n - 1][0]) * (polygon[0][1] - polygon[n - 1][1])
    return 0.5 * abs(area)
