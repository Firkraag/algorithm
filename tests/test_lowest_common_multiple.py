from unittest import TestCase
from lowest_common_multiple import lcm


class LcmTest(TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(10, 1), 10)
        self.assertEqual(lcm(10, 8), 40)
        self.assertEqual(lcm(15, 9), 45)
