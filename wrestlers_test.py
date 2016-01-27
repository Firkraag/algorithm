#!/usr/bin/env ipython
import unittest
from graph import Vertex, Graph
from wrestlers import wrestlers

class TestWrestler(unittest.TestCase):
    def testBfs(self):
        s = Vertex('s')
        r = Vertex('r')
        v = Vertex('v')
        w = Vertex('w')
        t = Vertex('t')
        x = Vertex('x')
        u = Vertex('u')
        y = Vertex('y')
        z = Vertex('z')
        for i in r,w:
            s.addEdge(i)
        for i in s,v:
            r.addEdge(i)
        v.addEdge(r)
        for i in s,t, x:
            w.addEdge(i)
        for i in w, x, u:
            t.addEdge(i)
        for i in w, t, u, y:
            x.addEdge(i)
        for i in t, x, y:
            u.addEdge(i)
        for i in x, u:
            y.addEdge(i)
        g = Graph([v,r,s,w,t,x,u,y,z])
        print wrestlers(g)
#        for u in g.vertices:
#            print "key: {}, color: {}, type = {}".format(u.key, u.color, u.type)
