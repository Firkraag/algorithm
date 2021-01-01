#! /usr/bin/env ipython

import math
import random
from randomized_select import randomized_select
from quicksort import randomized_quicksort


def kth_quantiles(A, B, k, p, r):
    if k > 0:
        n = r - p + 1
        location = math.floor(k / 2) * math.ceil(n / k)
        B[math.floor(k / 2)] = randomized_select(A, p, r, location)
        kth_quantiles(A, B, p, math.floor(k / 2) - 1, location - 1)
        kth_quantiles(A, B, math.floor(k / 2), location + 1, r)


def median_of_two_arrays(X, x_start, x_end, Y, y_start, y_end, size):
    print(X[x_start:x_end + 1], '\t', Y[y_start:y_end + 1], '\t', size)
    if size == 1:
        return min(X[x_start], Y[y_start])
    xc = X[x_start + int(math.floor(size / 2)) - 1]
    yc = Y[y_start + int(math.ceil(size / 2)) - 1]
    print(xc, yc)
    if xc == yc:
        return xc
    elif xc < yc:
        return median_of_two_arrays(X, x_start + int(math.floor(size / 2)), x_end, Y, y_start, y_end,
                                    math.ceil(size / 2))
    else:
        return median_of_two_arrays(X, x_start, x_end, Y, y_start + int(math.ceil(size / 2)), y_end,
                                    math.floor(size / 2))


if __name__ == '__main__':
    A = [random.randint(1, 100) for i in range(0, 15)]
    print(A)
    randomized_quicksort(A, 0, 14)
    print(A)
    B = [random.randint(1, 100) for i in range(0, 15)]
    print(B)
    randomized_quicksort(B, 0, 14)
    print(B)
    print(median_of_two_arrays(A, 0, 14, B, 0, 14, 3.0))
# randomized_select(A, 0, 14, 7)
# print( A)
# for i in range(1, 16):
#    randomized_select(A, 0, 14, i)
#    print( i, '\t', A)
#    print( randomized_select(A, 0, 14, i))
