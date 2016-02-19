import unittest
from partition import partition, partition2, partition3

class TestPartition(unittest.TestCase):
    def test_partition(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        partition(a, 0, 7)
        self.assertEquals(a, [2, 1, 3, 4, 7, 5, 6, 8])
    def test_partition2(self):
        a = [2, 8, 7, 1, 4, 5, 6, 4]
        partition2(a, 0, 7)
        self.assertEquals(a, [2, 1, 4, 4, 7, 5, 6, 8])
    def test_partition3(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4]
        partition3(a, 0, 7)
        self.assertEquals(a, [2, 1, 3, 4, 6, 5, 7, 8])

