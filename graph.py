def addVertex(G, v1, v2):
    G[v1].add(v2)
    G[v2].add(v1)


def chessboard(G):
    letters = 'abcdefgh'
    numbers = '12345678'
    # create empty graph for chess board
    for l in letters:
        for n in numbers:
            G[l + n] = set()

    # create graph for horse possible cell
    for i in range(8):
        for j in range(8):
            v1 = letters[j] + numbers[i]
            if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
                v2 = letters[j + 1] + numbers[i - 2]
                addVertex(G, v1, v2)
            if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
                v2 = letters[j + 2] + numbers[i - 1]
                addVertex(G, v1, v2)
            if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
                v2 = letters[j + 2] + numbers[i + 1]
                addVertex(G, v1, v2)
            if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
                v2 = letters[j + 1] + numbers[i + 2]
                addVertex(G, v1, v2)

#    print(G)


def distances_parents(G, start):
    N = len(G)
    d = {v:None for v in G}
    parents = {v:None for v in G}
    vertexes = []
    d[start] = 0
    vertexes.append(start)
    i = 0
    num = 1
    while i < num:
        v = vertexes[i]
        for neighbour in G[v]:
            if d[neighbour] is None:
                d[neighbour] = d[v] + 1
                vertexes.append(neighbour)
                parents[neighbour] = v
                num += 1
        i += 1
    """
    i=0
    for k in d:
        print(d[k], end=' ')
        i += 1
        if i == 8:
            i=0
            print()
    """
    #print(parents)
    return d, parents


def horse(start, end):
    graph = dict()
    chessboard(graph)
    dist, parents = distances_parents(graph, start)
    res = []
    res.append(end)
    p = parents[end]
    while p is not None:
        res.append(p)
        p = parents[p]
    print(res[::-1])

def main():
    horse('a1', 'a2')


main()
