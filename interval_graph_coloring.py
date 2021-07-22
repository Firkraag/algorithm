def interval_graph_coloring(graph):
    """
    The input graph is represented as an adjacency matrix since all we need is edge information about the graph
    """
    m = graph.shape[0]
    color = [1] * m
    number = 1
    for i in range(m):
        for j in range(m):
            if graph[i, j] == 1 and color[i] == color[j]:
                color[j] = color[i] + 1
                if color[j] > number:
                    number = color[j]
    return color,number
