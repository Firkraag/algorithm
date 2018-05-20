def insertion_sort(array):
    """
    inplace sort O(n ^ 2) sort
    :param array:
    :return:
    """
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and key < array[i]:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


def insertion_sort_recursive(array):
    """
    recursive version of insertion sort
    :param array:
    :return:
    """
    _insertion_sort_recursive_aux(array, len(array))


def _insertion_sort_recursive_aux(array, length):
    if length > 1:
        _insertion_sort_recursive_aux(array, length - 1)
        _insert(array, length)
    elif length == 1:
        if array[1] > array[0]:
            array[1], array[0] = array[0], array[1]


def _insert(array, length):
    key = array[length - 1]
    i = length - 2
    while i >= 0 and key < array[i]:
        array[i + 1] = array[i]
        i = i - 1
    array[i + 1] = key
