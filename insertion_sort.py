from binary_search import bisect_right


def insert_with_linear_search(array, length):
    """
    Use linear search to find a position in already sorted array[1...length-1] to insert array[length] into,
    making array[1: length] a sorted array.
    :param array:
    :param length: length > 0
    :return:
    """
    key = array[length - 1]
    i = length - 2
    while i >= 0 and key < array[i]:
        array[i + 1] = array[i]
        i = i - 1
    array[i + 1] = key


def insert_with_binary_search(array, length):
    """
    Use binary search to find a position in already sorted array[1...length-1] to insert array[length] into,
    making array[1: length] a sorted array.
    :param array:
    :param length: length > 0
    :return:
    """
    x = array[length - 1]
    index = bisect_right(array, x, 0, length - 1)
    array[index + 1: length] = array[index: length - 1]
    array[index] = x


def _insertion_sort_recursive_aux(array, length, insert_method):
    if length > 1:
        _insertion_sort_recursive_aux(array, length - 1, insert_method)
        insert_method(array, length)


def insertion_sort(array, insert_method=insert_with_linear_search):
    """
    inplace sort O(n ^ 2) sort
    :param array:
    :param insert_method:
    :return:
    """
    for j in range(2, len(array) + 1):
        insert_method(array, j)


def insertion_sort_recursive(array, insert_method=insert_with_linear_search):
    """
    recursive version of insertion sort
    :param array:
    :param insert_method:
    :return:
    """
    _insertion_sort_recursive_aux(array, len(array), insert_method)
