import networkx as nx


class ImpactAnalyzer:

    def __init__(self, graph):
        self.graph = graph

    def affected_nodes(self, node_id):
        """
        Return every downstream node affected by a change.
        """

        return list(nx.descendants(self.graph.graph, node_id))