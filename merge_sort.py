def merge_sort(array):
    """
    inplace O(nlgn) sort
    :param array:
    :return:
    """
    _merge_sort(array, 0, len(array) - 1)


def _merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(array, left, mid)
        _merge_sort(array, mid + 1, right)
        _merge(array, left, mid, right)


def _merge(array, left, mid, right):
    left_part = array[left: mid + 1]
    left_part.append(float("Inf"))
    right_part = array[mid + 1: right + 1]
    right_part.append(float("Inf"))
    i = 0
    j = 0
    for k in range(left, right + 1):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            i = i + 1
        else:
            array[k] = right_part[j]
            j = j + 1
