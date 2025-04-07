import unittest
from GraphePython import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_node("A")
        self.graph.add_node("B")
        self.graph.add_edge("A", "B", 5)

    def test_add_node(self):
        self.graph.add_node("C")
        self.assertIn("C", self.graph.graph)

    def test_add_edge(self):
        self.graph.add_node("C")    
        self.graph.add_edge("A", "C", 10)
        self.assertIn("C", self.graph.graph["A"])
        self.assertEqual(self.graph.get_edge_weight("A", "C"), 10)

    def test_get_edge_weight(self):
        weight = self.graph.get_edge_weight("A", "B")
        self.assertEqual(weight, 5)

if __name__ == "__main__":
    unittest.main()