def bubble_sort(array):
    """
    O(n ^ 2) inplace sort
    :param array: list
    :return:
    """
    n = len(array)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
