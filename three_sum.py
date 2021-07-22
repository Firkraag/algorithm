#!/usr/bin/env python
# coding=utf-8


def three_sum(array):
    """
    Given an array `array` of n integers, find one triplet
    in the array which gives the sum of zero.

    `array` must be in increasing order
    """
    n = len(array)
    for i in range(n - 2):
        j = i + 1
        k = n - 1

        while k >= j:
            if array[i] + array[j] + array[k] == 0:
                return array[i], array[j], array[k]
            elif array[i] + array[j] + array[k] > 0:
                k = k - 1
            else:
                j = j + 1
