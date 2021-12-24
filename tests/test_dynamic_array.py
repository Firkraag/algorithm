from unittest import TestCase
from dynamic_array import DynamicArray


class TestDynamicArray(TestCase):
    def test_add_and_get_and_size(self):
        dynamic_array = DynamicArray(2)
        self.assertEqual(0, dynamic_array.size())
        dynamic_array.add(1)
        dynamic_array.add(2)
        dynamic_array.add(3)
        self.assertEqual(3, dynamic_array.size())
        self.assertEqual(1, dynamic_array.get(0))
        self.assertEqual(2, dynamic_array.get(1))
        self.assertEqual(3, dynamic_array.get(2))
