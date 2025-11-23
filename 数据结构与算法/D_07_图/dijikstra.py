from graph import Graph
from vertex import Vertex
from priority_queue import PriorityQueue


def Dijkstra(graph: Graph, start: Vertex):
    """使用Dijkstra算法计算从起始顶点到所有其他顶点的最短路径

    Args:
        graph: 输入的图对象
        start: 起始顶点对象
    """
    pq = PriorityQueue()
    start.set_distance(0)
    pq.build_heap([(v.get_distance(), v) for v in graph])
    whild not pq.is_empty():
        current_vertex = pq.extract_min()


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge('u', 'v', 2)
    graph.add_edge('v', 'u', 2)
    graph.add_edge('v', 'w', 3)
    graph.add_edge('v', 'x', 2)
    graph.add_edge('x', 'u', 1)
    graph.add_edge('x', 'v', 2)
    graph.add_edge('x', 'w', 3)
    graph.add_edge('x', 'y', 1)
    graph.add_edge('w', 'v', 3)
    graph.add_edge('w', 'x', 3)
    graph.add_edge('w', 'y', 1)
    graph.add_edge('w', 'z', 5)
    graph.add_edge('y', 'x', 1)
    graph.add_edge('y', 'w', 1)
    graph.add_edge('y', 'z', 1)


# 打印图中的边和权重
for v in graph:
    for w in v.get_connections():
        print("({}, {}, {})".format(v.get_id(), w.get_id(), v.get_weight(w)))
