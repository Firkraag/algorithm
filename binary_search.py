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
    If x is already present in a,
    the insertion point will be before (to the left of) any existing entries.
    The return value is suitable for use as the first parameter to list.insert() assuming that a is already sorted.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

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


def bisect_right(array, x, low=0, high=None):
    """
    Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    :param array:
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
        if array[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low
