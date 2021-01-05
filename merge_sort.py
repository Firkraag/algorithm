from insertion_sort import insertion_sort
from merge import merge_with_sentinel


def merge_sort(array, merge_method=merge_with_sentinel):
    """
    inplace O(nlgn) sort
    :param array:
    :param merge_method:
    :return:
    """
    _merge_sort(array, 0, len(array) - 1, merge_method)


def _merge_sort(array, left, right, merge_method):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(array, left, mid, merge_method)
        _merge_sort(array, mid + 1, right, merge_method)
        merge_method(array, left, mid, right)


def merge_ins_sort_bottom_to_top(array, partition: int = 2):
    """
    Although merge sort runs faster than insertion sort asymptotically,
    the constant factors in insertion sort can make it faster in practice for small problem sizes on many machines.
    Thus, it makes sense to coarsen the leaves of the recursion by using insertion sort within merge sort when
    subproblems become sufficiently small. Consider a modification to merge sort in which n/k sublists of length k are
    sorted using insertion sort and then merged using the standard merging mechanism, where k is a value to be determined.

    bottom to top version with number of sublists specified
    :param array:
    :param partition: number of sublists
    :return:
    """
    assert partition > 0
    n = len(array)
    sublist_length = n // partition
    sublist_number = partition
    for i in range(sublist_number):
        left = sublist_length * i
        right = min(sublist_length * (i + 1) - 1, n - 1)
        insertion_sort(array, left, right)
    while sublist_number > 1:
        for i in range(0, sublist_number - 1, 2):
            merge_with_sentinel(array, sublist_length * i, sublist_length * (i + 1) - 1,
                                min(sublist_length * (i + 2) - 1, n - 1))
        sublist_length *= 2
        sublist_number = sublist_number // 2


def merge_ins_sort_top_to_bottom(array, sublist_length):
    """
    Although merge sort runs faster than insertion sort asymptotically, the constant factors in insertion sort can make
    it faster in practice for small problem sizes on many machines.
    Thus, it makes sense to coarsen the leaves of the recursion by using insertion sort within merge sort when
    subproblems become sufficiently small. Consider a modification to merge sort in which n/k sublists of length k are
    sorted using insertion sort and then merged using the standard merging mechanism, where k is a value to be determined.

    top to bottom version with sublist length specified
    :param array:
    :param sublist_length:
    :return:
    """
    n = len(array)
    assert 0 < sublist_length < n
    _merge_ins_sort_top_to_bottom(array, 0, n - 1, sublist_length)


def _merge_ins_sort_top_to_bottom(array, start, end, sublist_length):
    """

    :param array:
    :param start:
    :param end:
    :param sublist_length:
    :return:
    """
    length = end - start + 1
    if length > sublist_length:
        mid = (start + end) // 2
        _merge_ins_sort_top_to_bottom(array, start, mid, sublist_length)
        _merge_ins_sort_top_to_bottom(array, mid + 1, end, sublist_length)
        merge_with_sentinel(array, start, mid, end)
    else:
        insertion_sort(array, start, end)
