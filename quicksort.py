from partition import partition, randomized_partition


def quicksort(array, left, right, partition_method=partition):
    if left < right:
        index = partition_method(array, left, right)
        quicksort(array, left, index - 1)
        quicksort(array, index + 1, right)


def randomized_quicksort(array, left, right):
    if left < right:
        index = randomized_partition(array, left, right)
        randomized_quicksort(array, left, index - 1)
        randomized_quicksort(array, index + 1, right)
