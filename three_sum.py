#!/usr/bin/env python
# coding=utf-8

def threeSum(A):
    '''Given an array A of n integers, find one triplet
    in the array which gives the sum of zero.

    A must be in increasing order'''
    n = len(A)
    for i in range(n - 2):
        j = i + 1
        k = n - 1

        while k >= j:
            if A[i] + A[j] + A[k] == 0:
                return (A[i], A[j], A[k])
            elif A[i] + A[j] + A[k] > 0:
                k = k - 1
            else:
                j = j + 1



