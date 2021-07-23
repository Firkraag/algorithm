from unittest import TestCase
from binary_add import binary_add


class Test(TestCase):
    def test_binary_add(self):
        array1 = [1, 0, 1, 0]
        array2 = [0, 1, 1, 0]
        self.assertEqual(binary_add(array1, array2), [1, 0, 0, 0, 0])
