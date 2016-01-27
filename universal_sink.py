#!/usr/bin/env ipython

import numpy
import pdb

def universal_sink(M):
    return universal_sink_aux(M, 1)
def universal_sink_aux(M, i):
    size = M.shape[0]
    j = i
    while True:
        if j > size or M[i - 1][j - 1] != 0:
            break
        j = j + 1
#    pdb.set_trace()
    if j > size:
        for j in range(1, i):
            if M[i - 1][j - 1] != 0:
                return None
        for j in range(1, size + 1):
            if M[j - 1][i - 1] == 0 and j != i:
                return None
        return  i
    else:
        return universal_sink_aux(M, j)
