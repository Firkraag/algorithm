from rank_tree import rank_tree, rank_node


def inversion(A):
    inversion = 0
    i = 0
    T = rank_tree([])
    if isinstance(A, list):
        for key in A:
            i = i + 1
            x = rank_node(key, None, None, None, 0, 1)
            T.insert(x)
        #    print 'x.key = {}, x.rank = {}'.format(x.key, x.rank)
            inversion = inversion + i - x.rank
        return inversion
    else:
        print "Not invalid argument"
