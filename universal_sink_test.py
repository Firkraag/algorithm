import universal_sink as us
import unittest
import numpy

class TestRbtree(unittest.TestCase):
    def test_universal_sink(self):
        data = numpy.array([[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 1]])
        self.assertEquals(us.universal_sink(data), 1)
        data = numpy.array([[0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 0, 1]])
        self.assertEquals(us.universal_sink(data), 2)
        data = numpy.array([[0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1]])
        self.assertEquals(us.universal_sink(data), 3)
        data = numpy.array([[0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1]])
        self.assertEquals(us.universal_sink(data), 4)
        data = numpy.array([[0, 1, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0], [1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1]])
        self.assertEquals(us.universal_sink(data), 5)
        data = numpy.array([[0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])
        self.assertEquals(us.universal_sink(data), 6)
