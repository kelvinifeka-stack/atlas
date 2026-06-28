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

    def add_edge(self, source, target, relationship):
        self.graph.add_edge(
            source,
            target,
            relationship=relationship
        )

    def successors(self, node):
        return list(self.graph.successors(node))

    def predecessors(self, node):
        return list(self.graph.predecessors(node))

    def show(self):
        print("Nodes")
        for n, d in self.graph.nodes(data=True):
            print(n, d)

        print("\nEdges")
        for u, v, d in self.graph.edges(data=True):
            print(f"{u} --{d['relationship']}--> {v}")

    def get_node(self, node_id):
        return self.graph.nodes[node_id]


    def neighbors(self, node_id):
        return list(self.graph.neighbors(node_id))