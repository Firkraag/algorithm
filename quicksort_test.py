import unittest
from quicksort import partition, quicksort

class TestHeap(unittest.TestCase):
    def test_quicksort(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        quicksort(a, 0, 7)
        self.assertEquals(a, [1, 2, 3, 4, 5, 6, 7, 8])
    def test_partition(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        partition(a, 0, 7)
        self.assertEquals(a, [2, 1, 3, 4, 7, 5, 6, 8])
