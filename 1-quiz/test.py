def create_tour(nodes):
    length = len(nodes)
    tour = []
    for i in range(0, len(nodes), 1):
        if i == len(nodes)-1:
            node = (nodes[i], nodes[0])
            tour.append(node)
        else:
            node = (nodes[i], nodes[i+1])
            tour.append(node)

    return tour


def edge(x, y):
    return (x, y) if x < y else (y, x)


def create_tour2(nodes):
    # there are lots of ways to do this
    # a boring solution could just connect
    # the first node with the second node
    # second with third... and the last with the
    # first
    tour = []
    l = len(nodes)
    for i in range(l):
        t = edge(nodes[i], nodes[(i+1) % l])
        tour.append(t)
    return tour
