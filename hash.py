#!/usr/bin/env python


def hash_insert(T, k, h):
    i = 0
    while i < len(T):
        j = h(k, i)
        if T[j] is None:
            T[j] = k
            return j
        else:
            i = i + 1


def linear_probe(k, i):
    return (aux(k) + i) % len(T)


def quad_probe(k, i):
    return (aux(k) + i + 3 * i * i) % len(T)


def aux(k):
    return k


def double_hashing(k, i):
    return (k + i * (1 + k % (len(T) - 1))) % len(T)


T = [None] * 11
print("length of T is ", len(T))
for i in 10, 22, 31, 4, 15, 28, 17, 88, 59:
    hash_insert(T, i, double_hashing)

print(T)
