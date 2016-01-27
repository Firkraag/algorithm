from queue import queue

def wrestlers(g):
    for u in g.vertices:
        u.type = 0
    for u in g.vertices:
        if u.type == 0:
            if bfs(g, u) == False:
                return False
    return True
def bfs(g, s):
#    print "s.key: {}, s.color: {}".format(s.key, s.color)
    s.type = 1
    q = queue(2 * len(g.vertices))
    q.enqueue(s)
    while not q.empty():
        u = q.dequeue()
        for v in u.edges:
#            print "v.key: {}, v.color: {}".format(v.key, v.color)
            if u.type == v.type:
                return False
            elif v.type == 0:
                if u.type == 1:
                    v.type = 2
                else:
                    v.type = 1
                q.enqueue(v)
    return True
