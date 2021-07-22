from numpy import zeros


def knapsack_0_1(W, w, v):
    n = len(w)
    return knapsack_0_1_aux(W, w, v, 1, n)


def knapsack_0_1_aux(W, w, v, m, n):
    """
    m: the first item
    n: the last item
    W: total weight
    w: the list of weights of items
    v: the list of values of items
    """

    # if m > n, then we have scanned all the items
    if m > n:
        return 0
    # if W <= 0, then we can't take any more items
    if W <= 0:
        return 0
    # We have two choices: take item m or not take item m
    if W < w[m - 1]:
        return knapsack_0_1_aux(W, w, v, m + 1, n)
    else:
        return max(knapsack_0_1_aux(W - w[m - 1], w, v, m + 1, n) + v[m - 1], knapsack_0_1_aux(W, w, v, m + 1, n))


def knapsack_0_1_memoized(W, w, v):
    m = 1
    n = len(w)
    value = zeros((W + 1, n + 1))
    solution = zeros((W + 1, n + 1))
    for i in range(W + 1):
        for j in range(n + 1):
            value[i, j] = float("-Inf")
    knapsack_0_1_memoized_aux(W, w, v, m, n, value, solution)
    return value, solution


def knapsack_0_1_memoized_aux(W, w, v, m, n, value, solution):
    if m > n:
        return 0
    if value[W, m] >= 0:
        return value[W, m]
    if W < w[m - 1]:
        value[W, m] = knapsack_0_1_memoized_aux(W, w, v, m + 1, n, value, solution)
        solution[W, m] = 0
    else:
        s = knapsack_0_1_memoized_aux(W - w[m - 1], w, v, m + 1, n, value, solution) + v[m - 1]
        t = knapsack_0_1_memoized_aux(W, w, v, m + 1, n, value, solution)
        if s > t:
            solution[W, m] = 1
        value[W, m] = max(s, t)
    return value[W, m]


def print_knapsack_solution(solution, w):
    W = solution.shape[0] - 1
    n = solution.shape[1] - 1
    i = 1
    while W != 0 and i <= n:
        if solution[W, i] == 1:
            print(i)
            W = W - w[i - 1]
        i = i + 1
