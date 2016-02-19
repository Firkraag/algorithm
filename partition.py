import random

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def partition2(A, p, r):
    '''
    Partition A into three parts: < x, = x, > x. The return value is the median of the second part. So the return value is floor((p + r) / 2) when all elements in the array A[p .. r] have the same value. Partition in place.
    '''
    x = A[r]
    i = p - 1
    k = i
    for j in range(p, r):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            k = k + 1
            if i != k:
                A[j], A[k] = A[k], A[j]
        elif A[j] == x:
            k = k + 1
            A[k], A[j] = A[j], A[k]
    A[k + 1], A[r] = A[r], A[k + 1]
    return (k + 2 + i) / 2

def partition3(A, p, r):
    '''
    Variant of partition2. Requires O(n) extra space, but it is easier to implement.
    '''
    x = A[r]
    n = r - p + 1
    i = -1
    k = n
    B = [0] * n
    for j in range(p, r):
        if A[j] < x:
            i = i + 1
            B[i] = A[j]
        elif A[j] > x:
            k = k - 1
            B[k] = A[j]
    for j in range(i + 1, k):
        B[j] = x
    for j in range(p, r + 1):
        A[j] = B[j - p]
    return (2 * p + i + k) / 2

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)
