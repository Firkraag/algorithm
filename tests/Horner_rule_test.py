#!/usr/bin/env python
# encoding: utf-8

import unittest
import random
from Horner_rule import Horner_rule


class TestHornerRule(unittest.TestCase):
    def test_horner_rule(self):
        for _ in range(100):
            x = random.randint(1, 5)
            coefficients = [random.randint(0, 100) for _ in range(11)]
            expected_result = 0
            for index, coefficient in enumerate(coefficients):
                expected_result += coefficient * x ** index
            self.assertEqual(Horner_rule(x, coefficients), expected_result)
