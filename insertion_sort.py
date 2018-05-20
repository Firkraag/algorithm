from binary_search import binary_search


def insertion_sort(array):
    """
    inplace sort O(n ^ 2) sort
    :param array:
    :return:
    """
    for j in range(2, len(array) + 1):
        _insert(array, j)


def insertion_sort_recursive(array):
    """
    recursive version of insertion sort
    :param array:
    :return:
    """
    _insertion_sort_recursive_aux(array, len(array))


def insertion_sort_with_binary_search(array):
    """

    :param array:
    :return:
    """


def _insertion_sort_recursive_aux(array, length):
    if length > 1:
        _insertion_sort_recursive_aux(array, length - 1)
        _insert(array, length)


def _insert(array, length):
    """
    insert array[length] into already sorted subarray array[1: length - 1],
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
