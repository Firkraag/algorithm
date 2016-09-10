from queue import queue
from graph import Graph, Vertex

def wrestlers(wrestlersList, rivalriesList):
    '''
    There are two types of professional wrestlers: "babyfaces"
    ("good guys") and "heels" ("bad guys"). Between any pair of
    professional wrestlers, there may or may not be a rivalry.
    Given a list of professional wrestlers and a list of pairs of
    wrestlers for which there are rivalries, determine whether it is
    possible to designate some of the wrestlers as babyfaces and There
    remainder as heels such that each rivalry is between a babyfaces
    and a heel.
    '''
    d = dict()
    vertices = [None] * len(wrestlersList)
    edges = [None] * len(rivalriesList)
    for i in range(len(wrestlersList)):
        vertices[i] = Vertex(wrestlersList[i])
        d[wrestlersList[i]] = vertices[i]

    for i in range(len(rivalriesList)):
        w1, w2 = rivalriesList[i]
        edges[i] = (d[w1], d[w2])
    g = Graph(vertices, edges, False)

    for u in g.vertices:
        u.type = 0
    for u in g.vertices:
        if u.type == 0:
            if _bfs(g, u) == False:
                return False
    return True

def _bfs(g, s):
    s.type = 1
    q = queue(2 * len(g.vertices))
    q.enqueue(s)
    while not q.empty():
        u = q.dequeue()
        for v in g.adj[u]:
            if u.type == v.type:
                return False
            elif v.type == 0:
                if u.type == 1:
                    v.type = 2
                else:
                    v.type = 1
                q.enqueue(v)
    return True
