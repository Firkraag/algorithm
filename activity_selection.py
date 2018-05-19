from numpy import zeros


def activity_selection(s, f, n):
    c = zeros((n + 2, n + 2))
    activities = zeros((n + 2, n + 2))
    s = [float("-Inf")] + s[0:n] + [float("Inf")]
    f = [float("-Inf")] + f[0:n] + [float("Inf")]
    for l in range(3, n + 3):
        for i in range(0, n + 3 - l):
            j = i + l - 1
            print("i = {}, j = {}".format(i, j))
            for k in range(i + 1, j):
                print("k = {}".format(k))
                print("s[{}] = {}, f[{}] = {}".format(k, s[k], k, f[k]))
                print("s[{}] = {}, f[{}] = {}".format(j, s[j], i, f[i]))
                if f[i] <= s[k] and f[k] <= s[j]:
                    t = c[i, k] + c[k, j] + 1
                    print("t = {}, c[{}, {}] = {}".format(t, i, j, c[i, j]))
                    if t > c[i, j]:
                        c[i, j] = t
                        activities[i, j] = k
    return c, activities


def activity_selection_with_weight(s, f, v, n):
    '''This is a modification to the activity-selection problem in which each activity has,
    in addition to a start and finish time, a value v. Now the object is to maximize 
    the total value of the activies scheduled. It can be solved by dynamic programming method'''
    c = zeros((n + 2, n + 2))
    activities = zeros((n + 2, n + 2))
    s = [float("-Inf")] + s[0:n] + [float("Inf")]
    f = [float("-Inf")] + f[0:n] + [float("Inf")]
    for l in range(3, n + 3):
        for i in range(0, n + 3 - l):
            j = i + l - 1
            for k in range(i + 1, j):
                if f[i] <= s[k] and f[k] <= s[j]:
                    t = c[i, k] + c[k, j] + v[k - 1]
                    if t > c[i, j]:
                        c[i, j] = t
                        activities[i, j] = k
    return c, activities


def recursive_activity_selector(s, f, n):
    f = [float("-Inf")] + f
    return recursive_activity_selector_aux(s, f, 0, n)


def recursive_activity_selector_aux(s, f, k, n):
    m = k + 1
    while m <= n and s[m - 1] < f[k]:
        m = m + 1
    if m <= n:
        return {m}.union(recursive_activity_selector_aux(s, f, m, n))
    else:
        return {}


def greedy_activity_selector(s, f):
    n = len(s)
    A = {1}
    k = 1
    for m in range(2, n + 1):
        if s[m - 1] >= f[k - 1]:
            A = A.union({m})
            k = m
    return A


def greedy_activity_selector_last(s, f):
    '''Instead of always selecting the first activity to finish, 
    select the last activity to start that is compatible with all
    previously selected activities'''
    n = len(s)
    A = {n}
    k = n
    for m in range(n - 1, 0, -1):
        if f[m - 1] <= s[k - 1]:
            A = A.union({m})
            k = m
    return A


def print_activity(activities):
    m = activities.shape[0] - 1
    n = activities.shape[1] - 1
    print_activity_aux(activities, 0, n)


def print_activity_aux(activities, m, n):
    a = activities[m, n]
    if a == 0:
        return
    print_activity_aux(activities, m, a)
    print(int(a))
    print_activity_aux(activities, a, n)
