from unittest import TestCase

from src.graph_extended import ExtendedGraph as Graph


class TestExtendedGraph(TestCase):

    def setUp(self):
        graph_dict = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 4],
            4: [3]
        }
        self.graph1 = Graph(graph_dict)

        graph_dict = {
            'a': ['b', 'c'],
            'b': ['a', 'e'],
            'c': ['a', 'f'],
            'd': ['e', 'f'],
            'e': ['b', 'd', 'g'],
            'f': ['c', 'd', 'g'],
            'g': ['e', 'f']
        }
        self.graph2 = Graph(graph_dict)

        graph_dict = {
            'A': ['B'],
            'B': ['A', 'C'],
            'C': ['B', 'D'],
            'D': ['C', 'E'],
            'E': ['D']
        }
        self.bipartite_graph = Graph(graph_dict)

    def test_edge_cut(self):
        cut = self.graph1.edge_cut([1, 2])
        self.assertEqual(cut, [{1, 3}, {2, 3}])

        cut = self.graph1.edge_cut([3, 4])
        self.assertEqual(cut, [{1, 3}, {2, 3}])

        cut = self.graph1.edge_cut([1, 2, 3, 4])
        self.assertEqual(cut, [])

        cut = self.graph1.edge_cut([2, 3])
        self.assertEqual(cut, [{1, 2}, {1, 3}, {3, 4}])

        cut = self.bipartite_graph.edge_cut(['A', 'C', 'E'])
        self.assertEqual(cut, [{'B', 'A'}, {'B', 'C'}, {'D', 'C'}, {'D', 'E'}])

    def test_is_trail(self):
        trail = [
            ('a', 'c'), ('c', 'f'), ('f', 'd')
        ]
        self.assertTrue(self.graph2.is_trail(trail))

        trail = []
        self.assertTrue(self.graph2.is_trail(trail))

        trail = [
            ('e', 'd'), ('d', 'f'), ('f', 'g'),
            ('g', 'e'), ('e', 'd'), ('d', 'f')
        ]
        self.assertFalse(self.graph2.is_trail(trail))

        trail = [
            ('e', 'd'), ('d', 'f'), ('f', 'g'),
            ('g', 'e'), ('e', 'b'), ('b', 'a')
        ]
        self.assertTrue(self.graph2.is_trail(trail))

        trail = [
            ('e', 'd'), ('d', 'f'), ('f', 'g'),
            ('g', 'e'), ('e', 'b'), ('b', 'a'),
            ('a', 'c'), ('c', 'f')
        ]
        self.assertTrue(self.graph2.is_trail(trail))

        trail = [('a', 'c'), ('c', 'f'), ('f', 'd'), ('f', 'g')]
        self.assertFalse(self.graph2.is_trail(trail))

    def test_is_euler_trail(self):
        trail = [
            ('a', 'c'), ('c', 'f'), ('f', 'd')
        ]
        self.assertFalse(self.graph2.is_euler_trail(trail))

        trail = []
        self.assertFalse(self.graph2.is_euler_trail(trail))

        trail = [
            ('e', 'd'), ('d', 'f'), ('f', 'g'),
            ('g', 'e'), ('e', 'd'), ('d', 'f')
        ]
        self.assertFalse(self.graph2.is_euler_trail(trail))

        trail = [
            ('e', 'd'), ('d', 'f'), ('f', 'g'),
            ('g', 'e'), ('e', 'b'), ('b', 'a')
        ]
        self.assertFalse(self.graph2.is_euler_trail(trail))

        trail = [
            ('e', 'd'), ('d', 'f'), ('f', 'g'),
            ('g', 'e'), ('e', 'b'), ('b', 'a'),
            ('a', 'c'), ('c', 'f')
        ]
        self.assertTrue(self.graph2.is_euler_trail(trail))

    def test_co_spanning_tree(self):
        spanning_tree = [
            ('a', 'b'), ('a', 'c'), ('c', 'f'),
            ('f', 'g'), ('b', 'e'), ('e', 'd')
        ]
        co_tree = self.graph2.co_tree(spanning_tree)
        self.assertEqual(len(co_tree), 2)
        self.assertTrue({'d', 'f'} in co_tree and {'e', 'g'} in co_tree)

        spanning_tree = [
            ('a', 'b'), ('a', 'c'), ('c', 'f'),
            ('b', 'e'), ('e', 'd'), ('e', 'g')
        ]
        co_tree = self.graph2.co_tree(spanning_tree)
        self.assertEqual(len(co_tree), 2)
        self.assertTrue({'d', 'f'} in co_tree and {'f', 'g'} in co_tree)

