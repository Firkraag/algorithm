#!/usr/bin/env ipython
import unittest
from graph import Vertex, Graph
from hamiltonian_path import hamiltonian_path


class TestHamiltonianPath(unittest.TestCase):
    def testHamPath(self):
        r = Vertex('r')
        s = Vertex('s')
        t = Vertex('t')
        x = Vertex('x')
        y = Vertex('y')
        z = Vertex('z')
        vertices = [r, s, t, x, y, z]
        edges = [(r, s), (s, t), (t, x), (x, y), (y, z)]
        G = Graph(vertices, edges)
        self.assertEqual([hamiltonian_path(G, r, v) for v in vertices], [False, False, False, False, False, True])
        edges = [(r, s), (r, t), (s, x), (s, y), (t, z)]
        G = Graph(vertices, edges)
        self.assertEqual([hamiltonian_path(G, r, v) for v in vertices], [False, False, False, False, False, False])
        edges = [(r, s), (s, t), (s, x), (t, x)]
        vertices = [r, s, t, x]
        G = Graph(vertices, edges)
        self.assertEqual([hamiltonian_path(G, r, v) for v in vertices], [False, False, False, True])
        edges = [(r, s), (s, t), (s, x), (t, x), (r, y), (y, s)]
        vertices = [r, s, t, x, y]
        G = Graph(vertices, edges)
        self.assertEqual([hamiltonian_path(G, r, v) for v in vertices], [False, False, False, True, False])
        edges = [(r, s), (s, t), (s, x), (t, x), (r, y)]
        vertices = [r, s, t, x, y]
        G = Graph(vertices, edges)
        self.assertEqual([hamiltonian_path(G, r, v) for v in vertices], [False, False, False, False, False])
