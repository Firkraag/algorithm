def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

