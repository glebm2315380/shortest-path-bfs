import unittest
from main import bfs_shortest_path

class TestBFS(unittest.TestCase):
    def test_small_graph(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C', 'E'],
            'E': ['D']
        }
        result = bfs_shortest_path(graph, 'A')
        self.assertEqual(result['E'], 3)
        self.assertEqual(result['B'], 1)

    def test_disconnected_graph(self):
        graph = {
            0: [1],
            1: [0],
            2: [],
            3: [4],
            4: [3]
        }
        result = bfs_shortest_path(graph, 0)
        self.assertEqual(result[2], float('inf'))
        self.assertEqual(result[3], float('inf'))

if __name__ == '__main__':
    unittest.main()
