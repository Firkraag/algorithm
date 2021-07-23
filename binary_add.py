#!/usr/bin/env python
# encoding: utf-8


def binary_add(array1, array2):
    """
    Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B,
    in big-endian order.
    The sum of the two integers should be stored in binary form in a (n + 1)-element array C.
    :param array1: n-element array A
    :param array2: n-element array B
    :return: (n + 1)-element array C
    """
    assert len(array1) == len(array2)
    n = len(array1)
    promote = 0
    array3 = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        result = array1[i] + array2[i] + promote
        promote = result // 2
        result = result % 2
        array3[i + 1] = result
    array3[0] = promote
    return array3
