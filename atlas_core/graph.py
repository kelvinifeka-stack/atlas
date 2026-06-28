import networkx as nx


class AtlasGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id, node_type, **attributes):
        self.graph.add_node(
            node_id,
            type=node_type,
            **attributes
        )

    def add_edge(self, source, target, relationship, **attributes):
        self.graph.add_edge(
            source,
            target,
            relationship=relationship,
            **attributes
        )

    def node(self, node_id):
        return self.graph.nodes[node_id]

    def descendants(self, node_id):
        return list(nx.descendants(self.graph, node_id))

    def ancestors(self, node_id):
        return list(nx.ancestors(self.graph, node_id))

    def shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target)