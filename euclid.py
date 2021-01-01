#!/usr/bin/env python
# coding=utf-8


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid(b, a % b)
        return d, y, x - (a / b) * y
