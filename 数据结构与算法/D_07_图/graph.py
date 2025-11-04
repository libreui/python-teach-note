from vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vert_list:
            self.add_vertex(from_vert)
        if to_vert not in self.vert_list:
            self.add_vertex(to_vert)
        self.vert_list[from_vert].add_neighbor(self.vert_list[to_vert], weight)
        self.num_edges += 1

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def get_vertices(self):
        return self.vert_list.keys()

    def __contains__(self, key):
        return key in self.vert_list

    def __iter__(self):
        return iter(self.vert_list.values())



if __name__ == '__main__':
    g = Graph()
    for i in range(100):
        g.add_vertex(i)

    print(g.vert_list)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        for w in v.get_connections():
            print("({}, {})".format(v.get_id(), w.get_id()))
