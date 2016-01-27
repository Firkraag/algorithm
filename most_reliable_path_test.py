from most_reliable_path import most_reliable_path
import unittest
from graph import Vertex, Graph

class TestMostReliablePath(unittest.TestCase):
    def test_most_reliable_path(self):
        s = Vertex('s')
        u = Vertex('u')
        v = Vertex('v')
        w = Vertex('w')
        vertices = [s, u, v, w]
        edges = [(s, u), (s, v), (s, w), (u, v), (u, w), (w, u)]
        G = Graph(vertices, edges)
        probabilities = [0.2, 0.1, 0.15, 0.7, 0.6, 0.9] 
        re = dict()
        for i,j in zip(edges, probabilities):
            re[i] = j    
        def r(x, y):
            return re[(x, y)]        
        most_reliable_path(G, r, s)
        self.assertEquals([i.p for i in vertices], [None, s, u, s])
        self.assertEquals([round(i.r, 2) for i in vertices], [1, 0.2, 0.14, 0.15]) 
        most_reliable_path(G, r, u)
        self.assertEquals([i.p for i in vertices], [None, None, u, u])
        self.assertEquals([round(i.r, 2) for i in vertices], [0, 1, 0.7, 0.6])
