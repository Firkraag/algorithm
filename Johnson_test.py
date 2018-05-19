from Johnson import Johnson
from graph import Vertex, Graph
import unittest


class TestJohnson(unittest.TestCase):
    def testJohnson(self):
        a1 = Vertex(1)
        a2 = Vertex(2)
        a3 = Vertex(3)
        a4 = Vertex(4)
        a5 = Vertex(5)
        vertices = [a1, a2, a3, a4, a5]
        edges = [(a1, a2), (a1, a3), (a1, a5), (a2, a4), (a2, a5), (a3, a2), (a4, a1), (a4, a3), (a5, a4)]
        g = Graph(vertices, edges)
        weight = [3, 8, -4, 1, 7, 4, 2, -5, 6]
        w = dict()
        for i, j in zip(edges, weight):
            w[i] = j
        D = Johnson(g, w)
        print(D)
        a1 = Vertex(1)
        a2 = Vertex(2)
        a3 = Vertex(3)
        a4 = Vertex(4)
        a5 = Vertex(5)
        a6 = Vertex(6)
        vertices = [a1, a2, a3, a4, a5, a6]
        edges = [(a1, a5), (a2, a1), (a2, a4), (a3, a2), (a3, a6), (a4, a1), (a4, a5), (a5, a2), (a6, a2), (a6, a3)]
        g = Graph(vertices, edges)
        weight = [-1, 1, 2, 2, -8, -4, 3, 7, 5, 10]
        w = dict()
        for i, j in zip(edges, weight):
            w[i] = j
        D = Johnson(g, w)
        print(D)
