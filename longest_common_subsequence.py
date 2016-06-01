from numpy import zeros

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = zeros((m + 1, n + 1))
    b = zeros((m + 1, n + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i, j] = 0
            elif c[i - 1, j] >= c[i, j - 1]:
                c[i, j] = c[i - 1, j]
                b[i, j] = 1
            else:
                c[i, j] = c[i, j - 1]
                b[i, j] = 2
    return c,b 
def lcs_length_one_row(X, Y):
    m = len(X)
    n = len(Y)
    c = [0] * (n + 1)

    for i in range(1, m + 1):
        a = 0
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                value = a + 1
            elif c[j] >= c[j - 1]:
                value = c[j]
            else:
                value = c[j - 1]
            a = c[j]
            c[j] = value
    return c[n]
def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i, j] == 0:
        print_lcs(b, X, i - 1, j - 1)
        print X[i - 1],
    elif b[i, j] == 1:
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)

