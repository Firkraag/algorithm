from binary_search import bisect_right


def insert_with_linear_search(array, left_index, right_index):
    """
    Use linear search to find a position in already sorted array[left_index...right_index-1] to insert array[right_index] into,
    making array[left_index...right_index] a sorted array.
    :param array:
    :param left_index:
    :param right_index: right_index > 0
    :return:
    """
    key = array[right_index]
    i = right_index - 1
    while i >= left_index and key < array[i]:
        array[i + 1] = array[i]
        i = i - 1
    array[i + 1] = key


def insert_with_binary_search(array, left_index, right_index):
    """
    Use binary search to find a position in already sorted array[left_index...right_index-1] to insert array[right_index] into,
    making array[left_index...right_index] a sorted array.
    :param array:
    :param left_index:
    :param right_index: right_index > 0
    :return:
    """
    x = array[right_index]
    index = bisect_right(array, x, left_index, right_index)
    array[index + 1: right_index + 1] = array[index: right_index]
    array[index] = x


def insertion_sort(array, left=0, right=None, insert_method=insert_with_linear_search):
    """
    inplace sort O(n ^ 2) sort
    :param array:
    :param left:
    :param right:
    :param insert_method:
    :return:
    """
    if right is None:
        right = len(array) - 1
    for j in range(left, right + 1):
        insert_method(array, 0, j)


def _insertion_sort_recursive(array, length, insert_method):
    if length > 1:
        _insertion_sort_recursive(array, length - 1, insert_method)
        insert_method(array, 0, length - 1)


def insertion_sort_recursive(array, insert_method=insert_with_linear_search):
    """
    recursive version of insertion sort
    :param array:
    :param insert_method:
    :return:
    """
    _insertion_sort_recursive(array, len(array), insert_method)
