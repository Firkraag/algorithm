from tree import Tree
from numpy import zeros

class tree(Tree):
    def insert(self, node):
        y = None
        x = self.root
        while x != None:
            y = x
            if node.key == x.key:
                return
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if y == None:
            self.root = node
        elif node.key <= y.key:
            y.left = node
        else:
            y.right = node
def inorder_tree_walk(node, C):
    if node.left != None:
        inorder_tree_walk(node.left, C)
    C.append(node.key)
    if node.right != None:
        inorder_tree_walk(node.right, C)
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

def largest_monotonically_increasing_subsequence(A):
    T = tree(A)
    C = []
    # walk the tree and fill C with values of A in monotonically increasing order
    inorder_tree_walk(T.root, C)
    return lcs_length_one_row(A, C)
