from graph import Graph
from graph import Graph, Vertex
from 数据结构与算法.D_01_队列.c_queue import Queue


def build_graph(filename):
    d = {}
    g = Graph()
    wfile = open(filename, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket  = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g

def bsf(g, start):
    """广度优先搜索算法

    Args:
        g: 图对象
        start: 起始顶点对象
    """
    start.set_distance(0)
    start.set_color('gray')
    start.set_predecessor(None)

    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current_vert = vert_queue.dequeue()
        for nbr in current_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_predecessor(current_vert)
                vert_queue.enqueue(nbr)
            current_vert.set_color('black')

def traverse(y):
    x = y
    print(f"distance: {x.get_distance()}")
    print('route:')
    while x.get_predecessor():
        print(f"\t{x.get_id()}")
        x = x.get_predecessor()
    print(f"\t{x.get_id()}")

if __name__ == '__main__':
    graph = build_graph('words.txt')
    bsf(graph, graph.get_vertex('fool'))
    traverse(graph.get_vertex('sage'))