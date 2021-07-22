import random


def partition(array, left, right):
    pivot_index = left
    pivot = array[right]
    for i in range(left, right):
        if array[i] <= pivot:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1
    array[pivot_index], array[right] = array[right], array[pivot_index]
    return pivot_index


def partition2(array, left, right):
    """
    Partition A into three parts: < x, = x, > x. The return value is the median of the second part.
    So the return value is (left + right) // 2 when all elements in the array A[left .. right] have the same value. Partition in place.
    """
    x = array[right]
    i = left - 1
    k = i
    for j in range(left, right):
        if array[j] < x:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            k = k + 1
            if i != k:
                array[j], array[k] = array[k], array[j]
        elif array[j] == x:
            k = k + 1
            array[k], array[j] = array[j], array[k]
    array[k + 1], array[right] = array[right], array[k + 1]
    return (k + 2 + i) // 2


def partition3(array, left, right):
    """
    Variant of partition. Requires O(n) extra space, but it is easier to implement.
    """
    pivot = array[right]
    left_part = [array[i] for i in range(left, right) if array[i] <= pivot]
    right_part = [array[i] for i in range(left, right) if array[i] > pivot]
    pivot_index = left + len(left_part)
    array[left:pivot_index] = left_part[:]
    array[pivot_index + 1:right + 1] = right_part[:]
    array[pivot_index] = pivot
    return pivot_index


def randomized_partition(array, left, right):
    i = random.randint(left, right)
    array[i], array[right] = array[right], array[i]
    return partition(array, left, right)
