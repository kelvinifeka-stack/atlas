class ConfidenceEngine:
    """
    Computes confidence for every node in a reasoning graph.
    """

    def __init__(self, graph):
        self.graph = graph

    def compute(self):
        confidence = {}

        G = self.graph.graph

        # Evidence nodes keep their own confidence
        for node, data in G.nodes(data=True):
            if data["type"] == "Evidence":
                confidence[node] = data.get("confidence", 1.0)

        changed = True

        while changed:
            changed = False

            for node, data in G.nodes(data=True):

                if node in confidence:
                    continue

                predecessors = list(G.predecessors(node))

                if not predecessors:
                    continue

                if all(p in confidence for p in predecessors):
                    values = [confidence[p] for p in predecessors]
                    confidence[node] = sum(values) / len(values)
                    changed = True

        return confidence