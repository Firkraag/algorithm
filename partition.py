import random


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def partition2(array, p, r):
    """
    Partition A into three parts: < x, = x, > x. The return value is the median of the second part. So the return value is floor((p + r) / 2) when all elements in the array A[p .. r] have the same value. Partition in place.
    """
    x = array[r]
    i = p - 1
    k = i
    for j in range(p, r):
        if array[j] < x:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            k = k + 1
            if i != k:
                array[j], array[k] = array[k], array[j]
        elif array[j] == x:
            k = k + 1
            array[k], array[j] = array[j], array[k]
    array[k + 1], array[r] = array[r], array[k + 1]
    return (k + 2 + i) // 2


def partition3(array, p, r):
    """
    Variant of partition2. Requires O(n) extra space, but it is easier to implement.
    """
    x = array[r]
    n = r - p + 1
    i = -1
    k = n
    B = [0] * n
    for j in range(p, r):
        if array[j] < x:
            i = i + 1
            B[i] = array[j]
        elif array[j] > x:
            k = k - 1
            B[k] = array[j]
    for j in range(i + 1, k):
        B[j] = x
    for j in range(p, r + 1):
        array[j] = B[j - p]
    return (2 * p + i + k) // 2


def randomized_partition(array, p, r):
    i = random.randint(p, r)
    array[i], array[r] = array[r], array[i]
    return partition(array, p, r)
