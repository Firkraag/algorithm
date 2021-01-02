#!/usr/bin/env python
# encoding: utf-8
from unittest import TestCase

from gcd import gcd


class TestGcd(TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(10, 3), 1)
        self.assertEqual(gcd(10, 4), 2)
        self.assertEqual(gcd(10, 1), 1)
        self.assertEqual(gcd(10, 5), 5)
