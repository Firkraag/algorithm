from partition import partition, randomized_partition


def quicksort(array, p, r, partition_method=partition):
    if p < r:
        q = partition_method(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


def randomized_quicksort(array, p, r):
    if p < r:
        q = randomized_partition(array, p, r)
        randomized_quicksort(array, p, q - 1)
        randomized_quicksort(array, q + 1, r)
