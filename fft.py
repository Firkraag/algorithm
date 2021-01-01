#!/usr/bin/env python

import math


def recursive_fft(a):
    n = len(a)
    if n == 1:
        return a
    wn = complex(math.cos(2 * math.pi / n), math.sin(2 * math.pi / n))
    w = 1.0
    a0 = [a[i] for i in range(0, n, 2)]
    a1 = [a[i] for i in range(1, n, 2)]
    y0 = recursive_fft(a0)
    y1 = recursive_fft(a1)
    y = [0.0] * n
    for k in range(0, n // 2):
        y[k] = y0[k] + w * y1[k]
        y[k + n // 2] = y0[k] - w * y1[k]
        w = w * wn
    return y


def recursive_inverse_fft(y):
    n = len(y)
    result = recursive_inverse_fft_aux(y)
    return [result[i] / n for i in range(0, n)]


def recursive_inverse_fft_aux(y):
    n = len(y)
    if n == 1:
        return y
    wn = 1.0 / complex(math.cos(2 * math.pi / n), math.sin(2 * math.pi / n))
    w = 1.0
    y0 = [y[i] for i in range(0, n, 2)]
    y1 = [y[i] for i in range(1, n, 2)]
    a0 = recursive_inverse_fft_aux(y0)
    a1 = recursive_inverse_fft_aux(y1)
    a = [0.0] * n
    for k in range(0, n // 2):
        a[k] = (a0[k] + w * a1[k])
        a[k + n // 2] = (a0[k] - w * a1[k])
        w = w * wn
    return a
