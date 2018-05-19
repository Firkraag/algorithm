from numpy import zeros


def optimal_bst(p, q, n):
    e = zeros((n + 2, n + 1))
    w = zeros((n + 2, n + 1))
    root = zeros((1 + n, 1 + n))
    for i in range(1, n + 2):
        print("i = {}".format(i))
        e[i, i - 1] = q[i - 1]
        w[i, i - 1] = q[i - 1]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i, j] = float("Inf")
            w[i, j] = w[i, j - 1] + p[j - 1] + q[j]
            for r in range(i, j + 1):
                t = e[i, r - 1] + e[r + 1, j] + w[i, j]
                if t < e[i, j]:
                    e[i, j] = t
                    root[i, j] = r
    return e, root


def construct_optimal_bst(root):
    n = root.shape[1] - 1
    r = root[1, n]
    print("k{} is the root".format(int(r)))
    construct_optimal_bst_aux(root, r, 1, r - 1)
    construct_optimal_bst_aux(root, r, r + 1, n)


def construct_optimal_bst_aux(root, p, i, j):
    if j < p:
        if i <= j:
            r = root[i, j]
            print("k{} is the left child of k{}".format(int(r), int(p)))
            construct_optimal_bst_aux(root, r, i, r - 1)
            construct_optimal_bst_aux(root, r, r + 1, j)
        else:
            print("d{} is the left child of k{}".format(int(j), int(p)))
    if i > p:
        if i <= j:
            r = root[i, j]
            print("k{} is the right child of k{}".format(int(r), int(p)))
            construct_optimal_bst_aux(root, r, i, r - 1)
            construct_optimal_bst_aux(root, r, r + 1, j)
        else:
            print("d{} is the right child of k{}".format(int(j), int(p)))
