import random


def randomize_in_place(A):
    """
    An algorithm to permute the given array in place.
    It computes a uniform random permutation.
    """
    n = len(A)
    for i in range(n):
        j = random.randint(i, n - 1)
        A[i], A[j] = A[j], A[i]

# def permute_by_sorting(A):
#    n = len(A)
#    P = [0] * n
#    for i in
