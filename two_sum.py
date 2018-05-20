def two_sum(x, array):
    """
    an algorithm that, given a set S of n integers and another integer x,
    determines whether or not there exist two elements in S whose sum is exactly x.
    :param x:
    :param array:
    :return:
    """
    sorted_array = sorted(array)
    i = 0
    j = len(array) - 1
    while i < j:
        sum = sorted_array[i] + sorted_array[j]
        if sum == x:
            return True
        elif sum < x:
            i = i + 1
        else:
            j = j - 1
    return False
