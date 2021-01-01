def merge(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    n = length1 + length2
    i = 0
    j = 0
    k = 0
    result = [0] * n
    while i < length1 and j < length2:
        if list1[i] <= list2[j]:
            result[k] = list1[i]
            i += 1
        else:
            result[k] = list2[j]
            j += 1
        k += 1
    if i == length1:
        while j < length2:
            result[k] = list2[j]
            k += 1
            j += 1
    elif j == length2:
        while i < length1:
            result[k] = list1[i]
            k += 1
            i += 1
    return result


def k_way_merge(lists):
    """
    Merge k sorted lists and return it as one sorted list
    :param lists:
    :return:
    """
    length = len(lists)
    if length == 1:
        return lists[0]
    elif length == 2:
        return merge(lists[0], lists[1])
    else:
        list1 = k_way_merge(lists[0:length // 2])
        list2 = k_way_merge(lists[length // 2: length])
        return merge(list1, list2)
