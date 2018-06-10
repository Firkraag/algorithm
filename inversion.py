#!/usr/bin/env python
# encoding: utf-8


def inversion_with_insertion_sort(array):
    """
    Count number of inversions of an array using insertion sort

    Let A[1...n]  be an array of n numbers. If i < j and A[i]  > A[j] ,
    then the pair (i, j)  is called an inversion_with_insertion_sort of A
    :param array:
    :return:
    """
    array = array[:]
    return _inversion_with_insertion_sort(array)


def _inversion_with_insertion_sort(array):
    """
    :param array:
    :return:
    """
    inverse = 0
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and key < array[i]:
            inverse += 1
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return inverse


def inversion_with_merge_sort(array):
    """
    Count number of inversions of an array using merge sort

    Let A[1...n]  be an array of n numbers. If i < j and A[i]  > A[j] ,
    then the pair (i, j)  is called an inversion_with_insertion_sort of A
    :param array:
    :return:
    """
    array = array[:]
    return _inversion_with_merge_sort(array, 0, len(array) - 1)


def _inversion_with_merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        left_inverse = _inversion_with_merge_sort(array, left, mid)
        right_inverse = _inversion_with_merge_sort(array, mid + 1, right)
        inter_inverse = _merge(array, left, mid, right)
        return left_inverse + right_inverse + inter_inverse
    else:
        return 0


def _merge(array, left, mid, right):
    """

    :param array:
    :param left:
    :param mid:
    :param right:
    :return:
    """
    left_part = array[left: mid + 1]
    left_part.append(float("Inf"))
    right_part = array[mid + 1: right + 1]
    right_part.append(float("Inf"))
    i = 0
    j = 0
    inverse = 0
    for k in range(left, right + 1):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i = i + 1
        else:
            array[k] = right_part[j]
            j = j + 1
            inverse += (mid - left + 1 - i)
    return inverse

