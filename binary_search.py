def binary_search(target, array):
    """
    find target in sorted array.
    If found, return the index, otherwise return -1.
    :param target:
    :param array: list
    :return:
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < array[mid]:
            high = mid - 1
        elif target > array[mid]:
            low = mid + 1
        else:
            return mid
    return -1


def bisect_left(array, x, low=0, high=None):
    """
    Locate the insertion point for x in a to maintain sorted order.
    The parameters lo and hi may be used to specify a subset of the list which should be considered;
    by default the entire list is used. If x is already present in a,
    the insertion point will be before (to the left of) any existing entries.
    The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.

    The returned insertion point i partitions the array a into two halves so that all(val < x for val in a[lo:i])
    for the left side and all(val >= x for val in a[i:hi]) for the right side.
    :param array: sorted list
    :param x:
    :param low:
    :param high:
    :return:
    """
    if high is None:
        high = len(array)
    assert low <= high
    while low < high:
        mid = (low + high) // 2
        if array[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low
