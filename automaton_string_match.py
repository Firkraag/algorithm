#!/usr/bin/env python


def finite_automaton_matcher(T, s, m):
    n = len(T)
    q = 0
    for i in range(1, n + 1):
        q = s[(q, T[i - 1])]
        if q == m:
            print("Pattern occurs with shift {}".format(i - m))


def compute_transition_function(P, domain):
    m = len(P)
    s = dict()
    for a in domain:
        for q in range(m + 1):
            k = min(q + 1, m)
            while not (P[0:q] + a).endswith(P[0:k]):
                k = k - 1
            s[(q, a)] = k
    return s


def automaton_string_match(P, T, domain):
    s = compute_transition_function(P, domain)
    m = len(P)
    finite_automaton_matcher(T, s, m)
