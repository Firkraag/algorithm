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
