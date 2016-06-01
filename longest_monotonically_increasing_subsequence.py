#!/usr/bin/env python
# coding=utf-8

from longest_common_subsequence import lcs_length_one_row

def longest_monotonically_increasing_subsequence(A):
    C = sorted(set(A))
    return lcs_length_one_row(A, C)
