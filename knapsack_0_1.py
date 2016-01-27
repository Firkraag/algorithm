from numpy import zeros

def knapsack_0_1(W, w, v, m, n):
    if m > n:
        return 0
    if W <= 0:
        return 0
    if W < w[m - 1]:
        return knapsack_0_1(W, w, v, m + 1, n)
    else:
        return max(knapsack_0_1(W - w[m - 1], w, v, m + 1, n) + v[m - 1], knapsack_0_1(W, w, v, m + 1, n))
def knapsack_0_1_memoized(W, w, v, m, n):
    c = zeros((W + 1, n + 1))    
    b = zeros((W + 1, n + 1))    
    for i in range(0, W + 1):
        for j in range(0, n + 1):
            c[i, j] = float("-Inf")
    knapsack_0_1_memoized_aux(W, w, v, m, n, c, b)
    return c,b
def knapsack_0_1_memoized_aux(W, w, v, m, n, c, b):
    if m > n:
        return 0
    if c[W, m] >= 0:
        return c[W, m]
    if W < w[m - 1]:
        c[W, m] =  knapsack_0_1_memoized_aux(W, w, v, m + 1, n, c, b)
        b[W, m] = 0
    else:
        s = knapsack_0_1_memoized_aux(W - w[m - 1], w, v, m + 1, n, c, b) + v[m - 1]
        t = knapsack_0_1_memoized_aux(W, w, v, m + 1, n, c, b)
        if s > t:
            b[W, m] = 1
        c[W, m] = max(s, t)
    return c[W, m]
def print_knapsack_solution(b, w):
    W = b.shape[0] - 1
    n = b.shape[1] - 1
    i = 1
    while W != 0 and i <= n:
        if b[W, i] == 1:
            print i
            W = W - w[i - 1]
        i = i + 1
