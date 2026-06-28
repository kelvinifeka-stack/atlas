import networkx as nx


class QueryEngine:

    def __init__(self, graph):
        self.graph = graph

    def explain_decision(self, decision_id):
        """
        Return every upstream node that influenced a decision.
        """

        return list(nx.ancestors(self.graph.graph, decision_id))