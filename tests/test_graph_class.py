from unittest import TestCase

from src.graph_class import Graph


class TestGraph(TestCase):

    def setUp(self):
        graph_dict = {1: [2, 3], 2: [1, 3], 3: [1, 4], 4: [3]}
        self.graph = Graph(graph_dict)

        graph_dict = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['D']}
        self.bipartite_graph = Graph(graph_dict)

    def test_edge_cut(self):
        cut = self.graph.edge_cut([1, 2])
        self.assertEqual(cut, [{1, 3}, {2, 3}])

        cut = self.graph.edge_cut([3, 4])
        self.assertEqual(cut, [{1, 3}, {2, 3}])

        cut = self.graph.edge_cut([1, 2, 3, 4])
        self.assertEqual(cut, [])

        cut = self.graph.edge_cut([2, 3])
        self.assertEqual(cut, [{1, 2}, {1, 3}, {3, 4}])

        cut = self.bipartite_graph.edge_cut(['A', 'C', 'E'])
        self.assertEqual(cut, [{'B', 'A'}, {'B', 'C'}, {'D', 'C'}, {'D', 'E'}])
