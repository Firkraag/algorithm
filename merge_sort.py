def merge_with_sentinel(array, left, mid, right):
    """
    merge procedure with sentinels
    :param array:
    :param left:
    :param mid:
    :param right:
    :return:
    """
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


def merge_without_sentinel(array, left, mid, right):
    """
    merge procedure without sentinels
    A merge procedure without sentinels that stops once either array `left_part` or `right_part` has had all its elements
    copied back to `array` and then copying the remainder of the other array back into `array`
    :param array:
    :param left:
    :param mid:
    :param right:
    :return:
    """
    left_part = array[left: mid + 1]
    right_part = array[mid + 1: right + 1]
    i = 0
    j = 0
    k = left
    left_length = mid - left + 1
    right_length = right - mid
    while i < left_length and j < right_length:
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            k = k + 1
            i = i + 1
        else:
            array[k] = right_part[j]
            k = k + 1
            j = j + 1
    if i < left_length:
        array[k: right + 1] = left_part[i: left_length]
    else:
        array[k: right + 1] = right_part[j: right_length]


def _merge_sort(array, left, right, merge_method):
    if left < right:
        mid = (left + right) // 2
        _merge_sort(array, left, mid, merge_method)
        _merge_sort(array, mid + 1, right, merge_method)
        merge_method(array, left, mid, right)


def merge_sort(array, merge_method=merge_with_sentinel):
    """
    inplace O(nlgn) sort
    :param array:
    :param merge_method:
    :return:
    """
    _merge_sort(array, 0, len(array) - 1, merge_method)
