def merge_with_sentinel(array, left, mid, right):
    """
    merge procedure with sentinels

    merge array[left...mid] and array[mid + 1...right]
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
            i += 1
        else:
            array[k] = right_part[j]
            j += 1


def merge_without_sentinel(array, left, mid, right):
    """
    merge procedure without sentinels

    A merge procedure without sentinels that stops once either array `left_part` or `right_part` has had all its elements
    copied back to `array` and then copying the remainder of another array back into `array`
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
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            array[k] = left_part[i]
            k += 1
            i += 1
        else:
            array[k] = right_part[j]
            k += 1
            j += 1
    if i < len(left_part):
        array[k: right + 1] = left_part[i:]
    else:
        array[k: right + 1] = right_part[j:]