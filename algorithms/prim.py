from heapq import heappop, heappush
# Prim's algorithm based on a course from princeton
# http://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/04GreedyAlgorithmsII-2x2.pdf


def Prims(G, s):
    Vertices = []
    Tree = {}
    # weight, edge1, edge2
    Queue = [(0, None, s)]
    while Queue:
        # choose edge with smallest value
        s, p, u = heappop(Queue)
        # skip vertices in tree
        if u in Vertices:
            continue
        Vertices.append(u)
        # build structure
        if p is None:
            pass
        elif p in Tree:
            Tree[p].append(u)
        else:
            Tree[p] = [u]
        for v, w in G.items():
            heappush(Queue, (w, u, v))
    return Tree


# returns {'a': ['d', 'b', 'e', 'c', 'f', 'g']}
G = {
    'a': [('b', 7), ('d', 5)],
    'b': [('a', 7), ('d', 9), ('c', 8), ('e', 7)],
    'c': [('b', 8), ('e', 5)],
    'd': [('a', 5), ('b', 9), ('e', 15), ('f', 6)],
    'e': [('b', 7), ('c', 5), ('d', 15), ('f', 8), ('g', 9)],
    'f': [('d', 6), ('e', 8), ('g', 11)],
    'g': [('e', 9), ('f', 11)]
}


# returns {'a': ['e', 'f', 'c', 'g'], 'b': ['d', 'a']}
H = {
    'd': [('a', 3), ('f', 7)],
    'e': [('c', 1)],
    'g': [('f', 9)],
    'f': [('d', 7), ('g', 9)],
    'a': [('b', 2), ('c', 3), ('d', 3)],
    'b': [('a', 2)],
    'c': [('e', 1), ('a', 3)]
}


# returns {'A': ['B', 'C']}
I = {
    'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]
}


print Prims(G, 'a')
print Prims(H, 'b')
print Prims(I, 'A')
