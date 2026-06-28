class AtlasQuery:

    def __init__(self, graph):
        self.graph = graph

    def find_by_type(self, node_type):

        result = []

        for node, data in self.graph.graph.nodes(data=True):

            if data.get("type") == node_type:
                result.append(node)

        return result