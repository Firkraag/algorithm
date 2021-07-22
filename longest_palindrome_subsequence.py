#!/usr/bin/env python
# coding=utf-8

from longest_common_subsequence import lcs_length, print_lcs


def longest_palindrome_subsequence(s):
    # c, b = lcs_length(s, s[::-1])
    # print(_lcs(b, s, len(s), len(s)))
    n = len(s)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        c[i][i] = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            c[i][i + 1] = 2
        else:
            c[i][i + 1] = 1
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                print(i, j, c[i + 1][j - 1])
                c[i][j] = 2 + c[i + 1][j - 1]
            else:
                c[i][j] = max(c[i][j - 1], c[i + 1][j])
    return c


def print_lps(c, s):
    start = 0
    end = len(s) - 1
    l = []
    idx = []
    index = 0
    while start < end:
        if s[start] == s[end]:
            l.insert(index, s[end])
            l.insert(index, s[start])
            idx.insert(index, end)
            idx.insert(index, start)
            index += 1
            start += 1
            end -= 1
        elif c[start + 1][end] >= c[start][end - 1]:
            start += 1
        else:
            end -= 1
    if start == end:
        l.insert(index, s[start])
        idx.insert(index, start)
    return ''.join(l), idx
