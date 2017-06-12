from graph_base import Graph


class ExtendedGraph(Graph):

    def __init__(self, graph_dict=None):
        super(ExtendedGraph, self).__init__(graph_dict)

    def is_complete(self):
        vertices = self.vertices()
        return len(self.edges()) == len(vertices) * (len(vertices) - 1) / 2

    def is_subgraph(self, graph):
        return self.__is_subset(graph.vertices(), self.vertices()) and \
               self.__is_subset(graph.edges(),    self.edges())

    def edge_cut(self, x_vertices):
        edge_cut = []
        y_vertices = set(self.vertices()) - set(x_vertices)

        for x in x_vertices:
            for y in y_vertices:
                if x in self.graph_dict[y] or y in self.graph_dict[x]:
                    edge_cut.append({x, y})

        return edge_cut

    def is_trail(self, walk):
        edges = self.edges()

        trail = self.__get_trail(walk, edges)
        return len(trail) == len(walk)

    def is_euler_trail(self, walk):
        edges = self.edges()

        trail = self.__get_trail(walk, edges)
        return len(trail) == len(walk) and len(trail) == len(edges)

    def co_tree(self, spanning_tree):
        co_tree = []
        spanning_tree = [{u, v} for u, v in spanning_tree]

        for edge in self.edges():
            if edge not in spanning_tree:
                co_tree.append(edge)

        return co_tree

    @staticmethod
    def __get_trail(walk, edges):
        trail = set()

        _v = None
        for edge in walk:
            if type(edge) is set:
                raise AttributeError('Walk cannot contain edges represented by a set')

            u, v = edge
            if {u, v} in edges and (not _v or u == _v):
                _v = v
                trail.add((u, v))
            else:
                break

        return trail

    @staticmethod
    def __is_subset(subset, mainset):
        for element in subset:
            if element not in mainset:
                return False

        return True
