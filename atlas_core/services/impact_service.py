from atlas_core.algorithms.impact import ImpactAnalyzer


class ImpactService:

    def __init__(self, graph):
        self.analyzer = ImpactAnalyzer(graph)

    def review_required(self, assumption_id):
        affected = self.analyzer.affected_nodes(assumption_id)

        return [
            node
            for node in affected
            if node.startswith("D")
        ]