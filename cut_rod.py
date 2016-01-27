def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float("-Inf")
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + r[j - i])
        r[j] = q
    return r[n]    
def bottom_up_cut_rod_two_subproblem(p, n):
    r = [0] * (n + 1)
    for i in range(1, n + 1):
        r[i] = p[i - 1]
    for j in range(1, n + 1):
        q = float("-Inf")
        for i in range(1, j + 1):
            q = max(q, r[i] + r[j - i])
        r[j] = q
    return r[n]    
def memoized_cut_rod(p, n):
    r = [float("-Inf")] * n
    return memoized_cut_rod_aux(p, n, r)
def memoized_cut_rod_aux(p, n, r):
    if n == 0:
        return 0
    if r[n - 1] >= 0:
        return r[n - 1]
    q = float("-Inf")
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i, r))
    r[n - 1] = q
    return q
def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float("-Inf")
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q
    return r,s    
def print_cut_rod_solution(p, n, cut):
    r,s = cut(p, n)
    while n != 0:
        print s[n]
        n = n - s[n]
def bottom_up_cut_rod_with_fixed_cut_cost(p, n, c):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float("-Inf")
        for i in range(1, j):
            q = max(q, r[i] + r[j - i] - c)
        q = max(q, p[j - 1])
        r[j] = q
    return r[n]    
def extended_memoized_cut_rod(p, n):
    r = [float("-Inf")] * n
    s = [0] * (n + 1)
    extended_memoized_cut_rod_aux(p, n, r, s)
    return r,s
def extended_memoized_cut_rod_aux(p, n, r, s):
    if n == 0:
        return 0
    if r[n - 1] >= 0:
        return r[n - 1]
    q = float("-Inf")
    for i in range(1, n + 1):
        value = p[i - 1] + extended_memoized_cut_rod_aux(p, n -i, r, s)
        if q < value:
            q = value
            s[n] = i
    r[n - 1] = q
    return q
