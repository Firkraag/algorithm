#!/usr/bin/env python
# encoding: utf-8
from unittest import TestCase

from euclid import euclid


class TestEuclid(TestCase):
    def test_gcd(self):
        self.assertEqual(euclid(10, 3), 1)
        self.assertEqual(euclid(10, 4), 2)
        self.assertEqual(euclid(10, 1), 1)
        self.assertEqual(euclid(10, 5), 5)
