from partition import partition, partition2, partition3, randomized_partition

def quicksort(A, p, r, partition_method = partition):
    if p < r:
        q = partition_method(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q+1, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q+1, r)
