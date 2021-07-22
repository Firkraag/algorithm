import unittest
from polygon_area import polygon_area


class TestPolygonArea(unittest.TestCase):
    def test_rectangle_area(self):
        rectangle = ((0, 0), (0, 2), (2, 2), (2, 0))
        self.assertEqual(polygon_area(rectangle), 4)

    def test_triangle_area(self):
        triangle = ((0, 0), (5, 0), (2.5, 5))
        self.assertEqual(polygon_area(triangle), 12.5)
