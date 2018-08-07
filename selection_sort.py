#!/usr/bin/env python
# encoding: utf-8


def selection_sort(array):
    """
    Inplace sort
    Consider sorting n numbers stored in array A by first finding the smallest element of A
    and exchanging it with the element in A[1] . Then find the second smallest element of A, and exchange it with A[2].
    Continue in this manner for the first n - 1 elements of A.
    :param array:
    :return:
    """
    n = len(array)
    for i in range(n - 1):
        minimum = array[i]
        index = i
        for j in range(i + 1, n):
            if minimum > array[j]:
                minimum = array[j]
                index = j
        array[i], array[index] = array[index], array[i]
