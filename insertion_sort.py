from binary_search import bisect_right


def insert_with_linear_search(array, right_index):
    """
    Use linear search to find a position in already sorted array[0...right_index-1] to insert array[right_index] into,
    making array[0...right_index] a sorted array.
    :param array:
    :param right_index: ridht_index > 0
    :return:
    """
    key = array[right_index]
    i = right_index - 1
    while i >= 0 and key < array[i]:
        array[i + 1] = array[i]
        i = i - 1
    array[i + 1] = key


def insert_with_binary_search(array, right_index):
    """
    Use binary search to find a position in already sorted array[0...right_index-1] to insert array[right_index] into,
    making array[0...right_index] a sorted array.
    :param array:
    :param right_index: right_index > 0
    :return:
    """
    x = array[right_index]
    index = bisect_right(array, x, 0, right_index)
    array[index + 1: right_index + 1] = array[index: right_index]
    array[index] = x


def _insertion_sort_recursive_aux(array, length, insert_method):
    if length > 1:
        _insertion_sort_recursive_aux(array, length - 1, insert_method)
        insert_method(array, length - 1)


def insertion_sort(array, left=0, right=None, insert_method=insert_with_linear_search):
    """
    inplace sort O(n ^ 2) sort
    :param array:
    :param insert_method:
    :param left:
    :param right:
    :return:
    """
    if right is None:
        right = len(array)
    else:
        right += 1
    for j in range(left, right):
        insert_method(array, j)


def insertion_sort_recursive(array, insert_method=insert_with_linear_search):
    """
    recursive version of insertion sort
    :param array:
    :param insert_method:
    :return:
    """
    _insertion_sort_recursive_aux(array, len(array), insert_method)
