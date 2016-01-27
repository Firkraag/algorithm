def swap(x, y): 
    tmp = x
    x = y
    y = tmp
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q+1, r)
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp
    return i + 1

