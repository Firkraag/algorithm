import math
import random
from unittest import TestCase
from pow import pow1, pow2


class Test(TestCase):
    def test_pow1(self):
        x = random.randint(1, 10)
        for n in range(10):
            self.assertEqual(pow1(x, n), math.pow(x, n))

    def test_pow2(self):
        x = random.randint(1, 10)
        for n in range(10):
            self.assertEqual(pow2(x, n), math.pow(x, n))
