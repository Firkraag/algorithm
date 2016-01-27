import numpy as np

def extend_shortest_paths(L, W):
    n = L.shape[0]
    LW = np.empty((n, n)) 
    for i in range(0, n):
        for j in range(0, n):
            LW[i, j] = float("Inf")
            for k in range(0, n):
                LW[i, j] = min(LW[i, j], L[i, k] + W[k, j])
    return LW

def slow_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = [None] * n
    L[0] = np.empty((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                L[0][i, j] = 0
            else:
                L[0][i, j] = float("Inf")
    L[1] = W
    for m in range(2, n):
        L[m] = extend_shortest_paths(L[m - 1], W)
    return L[m]

def extend_shortest_paths_with_predecessor_subgraph(L, P, W):
    n = W.shape[0]
    LW = np.empty((n, n))
    PP = np.empty((n, n))
    for i in range(0, n):
        for j in range(0, n):
            LW[i, j] = float("Inf")
            PP[i, j] = None
            for k in range(0, n):
                if LW[i, j] > L[i, k] + W[k, j]:
                    LW[i, j] = L[i, k] + W[k, j]
                    PP[i, j] = k + 1
            if LW[i, j] == L[i, j]:
                PP[i, j] = P[i, j]
#                    if j == i:
#                        PP[i, j] = None
#                    elif j != k:
#                        PP[i, j] = k + 1
#                    else:
#                        PP[i, j] = P[i, j]
    return LW, PP

def slow_all_pairs_shortest_paths_with_predecessor_subgraph(W):
    n = W.shape[0]
    L = np.empty((n, n))
    P = np.empty((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if j == i:
                L[i, j] = 0
            else:
                L[i, j] = float("Inf")
            P[i, j] = None
    for m in range(1, n):
        L, P = extend_shortest_paths_with_predecessor_subgraph(L, P, W)
        print L
        print P
    return L, P

def predecessor(W, L):
    n = W.shape[0]
    P = np.empty((n, n))
    COMPLETED = np.empty((n, n), dtype = bool)
    DEPTH = np.empty((n, n))
    for i in range(0, n):
        for j in range(0, n):
            COMPLETED[i, j] = False
            DEPTH[i, j] = None
            P[i, j] = None
    for i in range(0, n):
        P[i, i] = None
        COMPLETED[i, i] = True
        DEPTH[i, i] = 0
    for m in range(1, n):
        for i in range(0, n):
            for j in range(0, n):
                if i == 0:
                    print m
                    print COMPLETED[i, j]
                    print L[m][i]
                    print L[n - 1][j]
                if COMPLETED[i, j] == False and L[m][i, j] == L[n - 1][i, j]:
                    for k in range(0, n):
                        if DEPTH[i, k] == m - 1 and L[m][i, j] == L[m -1][i, k] + W[k, j]:
                            DEPTH[i, j] = m
                            P[i, j] = k + 1
                            COMPLETED[i, j] = True
                            break
    return P
def faster_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = W
    m = 1
    while m < n - 1:
        L = extend_shortest_paths(L, L)
        m = 2 * m
        print m
        print L
    return L

def negative_weight_cycle(W):
    L = faster_all_pairs_shortest_paths(W)
    n = W.shape[0]
    status = True
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if L[i, j] > L[i, k] + W[k, j]:
                    print "source {} contains a negative-weight cycle".format(i + 1)
                    status = False
    return status
def negative_weight_cycle_another(W):
    L = faster_all_pairs_shortest_paths(W)
    L = extend_shortest_paths(L, W)
    print L
    status = True
    n = W.shape[0]
    for i in range(0, n):
        if L[i, i] < 0:
            status = False
    return status
def minimum_negative_weight_cycle_edges_number(W):
    n = W.shape[0]
    L = W
    for m in range(2, n + 1):
        L = extend_shortest_paths(L, W)
        for i in range(0, n):
            if L[i, i] < 0:
                print "minimum negative weight cycle edges number is {}".format(m)
                return False
    return True

def Floyd_Warshall(W):
    n = W.shape[0]
    D = [None] * (n + 1)
    D[0] = W
    P = [None] * (n + 1)
    P[0] = np.empty((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or W[i - 1, j - 1] == float("Inf"):
                P[0][i - 1, j - 1] = None
            else:
                P[0][i - 1, j - 1] = i
    for k in range(1, n + 1):
        D[k] = np.empty((n, n))
        P[k] = np.empty((n, n))
        for i in range(n):
            for j in range(n):
                D[k][i,j] = min(D[k - 1][i, j], D[k - 1][i, k - 1] + D[k - 1][k - 1, j])
                if D[k - 1][i, j] > D[k - 1][i, k - 1] + D[k - 1][k - 1, j]:
                    P[k][i, j] = P[k - 1][k - 1, j]
                else:
                    P[k][i, j] = P[k - 1][i, j]
    return D[n], P[n]
def Floyd_Warshall_WITH_LI(W):
    n = W.shape[0]
    D = [None] * (n + 1)
    D[0] = W
    LI = [None] * (n + 1)
    LI[0] = np.empty((n, n), dtype = np.int32)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
                LI[0][i - 1, j - 1] = 0
    for k in range(1, n + 1):
        D[k] = np.empty((n, n))
        LI[k] = np.empty((n, n), dtype = np.int32)
        for i in range(n):
            for j in range(n):
                D[k][i,j] = min(D[k - 1][i, j], D[k - 1][i, k - 1] + D[k - 1][k - 1, j])
                if D[k - 1][i, j] > D[k - 1][i, k - 1] + D[k - 1][k - 1, j]:
                    LI[k][i, j] = k
                else:
                    LI[k][i, j] = LI[k - 1][i, j]
        print LI[k]
        print D[k]
    return D[n], LI[n]

def print_all_pairs_shortest_path(LI, i, j):
    global status
    status = [False] * LI.shape[0]
    print_all_pairs_shortest_path_aux(LI, i, j)
def print_all_pairs_shortest_path_aux(LI, i, j):
    global status
   # print "www: {}, {}, status: {}".format(i, j, status)
    if LI[i - 1, j - 1] == 0:
        if status[i - 1] == False:
            status[i - 1] = True
            print i
        if status[j - 1] == False:
            status[j - 1] = True
            print j
    else:
        print_all_pairs_shortest_path_aux(LI, i, LI[i - 1, j - 1])
        if status[LI[i - 1, j - 1] - 1] == False: 
            print LI[i - 1, j - 1]
            status[LI[i - 1, j - 1] - 1] = True 
        print_all_pairs_shortest_path_aux(LI, LI[i - 1, j - 1], j)
