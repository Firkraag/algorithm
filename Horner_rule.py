#!/usr/bin/env python
# encoding: utf-8
import functools


def Horner_rule(x, coefficients):
    """
    Implements Horner's rule
    :param x:
    :param coefficients:
    :return:
    """
    return functools.reduce(lambda accumulate, coefficient: coefficient + accumulate * x, reversed(coefficients), 0)
