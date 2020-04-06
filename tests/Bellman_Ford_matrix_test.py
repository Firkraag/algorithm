from Bellman_Ford_matrix import Bellman_Ford_matrix, slow_all_pairs_shortest_paths
import unittest
import numpy


class TestBellmanFordMatrix(unittest.TestCase):
    def test_Bellman_Ford_matrix(self):
        W = numpy.array([[float("Inf"), 6., 7., float("Inf"), float("Inf")], [float("Inf"), float("Inf"), 8., 5., -4.],
                         [float("Inf"), float("Inf"), float("Inf"), -3., 9.],
                         [float("Inf"), -2., float("Inf"), float("Inf"), float("Inf")],
                         [2., float("Inf"), float("Inf"), 7., float("Inf")]])
        d, p = Bellman_Ford_matrix(W, 1)
        self.assertEqual(d, [0, 2.0, 7.0, 4.0, -2.0])
        self.assertEqual(p, [None, 4, 1, 3, 2])

    def test_slow_all_pairs_shortest_paths(self):
        W = numpy.array([[0, 6., 7., float("Inf"), float("Inf")], [float("Inf"), 0, 8., 5., -4.],
                         [float("Inf"), float("Inf"), 0, -3., 9.], [float("Inf"), -2., float("Inf"), 0, float("Inf")],
                         [2., float("Inf"), float("Inf"), 7., 0]])
        L = slow_all_pairs_shortest_paths(W, 1)
        print(L)
        self.assertEqual(L, [0, 2.0, 7.0, 4.0, -2.0])
