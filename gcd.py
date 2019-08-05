#!/usr/bin/env python
# encoding: utf-8


def gcd(m: int, n: int):
    """
    compute the greatest common divisor of m and n;
    :param m:
    :param n:
    :return:
    """
    while n > 0:
        rem = m % n
        m = n
        n = rem
    return m
