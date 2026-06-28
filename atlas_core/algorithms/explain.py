from networkx import shortest_path


class ExplanationEngine:
    """
    Generates reasoning paths through the Atlas graph.
    """

    def __init__(self, graph):
        self.graph = graph

    def explain(self, start_node, end_node):
        G = self.graph.graph

        try:
            return shortest_path(G, start_node, end_node)
        except Exception:
            return None