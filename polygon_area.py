#!/usr/bin/env python
from typing import Sequence, Tuple, Union

Number = Union[int, float]


def polygon_area(polygon: Sequence[Tuple[Number, Number]]) -> float:
    n = len(polygon)
    area = 0
    for i in range(n - 1):
        area += (polygon[i][0] + polygon[i + 1][0]) * (polygon[i + 1][1] - polygon[i][1])
    area += (polygon[0][0] + polygon[n - 1][0]) * (polygon[0][1] - polygon[n - 1][1])
    return 0.5 * abs(area)
