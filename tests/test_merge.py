from unittest import TestCase
from merge import merge_without_sentinel, merge_with_sentinel
from random_array import random_arrays


class MergeTest(TestCase):
    def test_merge_with_sentinel(self):
        for array in random_arrays():
            left_array = array[:len(array) // 2]
            right_array = array[len(array) // 2:]
            left_array.sort()
            right_array.sort()
            result_array = left_array + right_array
            merge_with_sentinel(result_array, 0, len(array) // 2 - 1, len(array) - 1)
            self.assertEqual(result_array, sorted(array))

    def test_merge_without_sentinel(self):
        for array in random_arrays():
            left_array = array[:len(array) // 2]
            right_array = array[len(array) // 2:]
            left_array.sort()
            right_array.sort()
            result_array = left_array + right_array
            merge_without_sentinel(result_array, 0, len(array) // 2 - 1, len(array) - 1)
            self.assertEqual(result_array, sorted(array))
