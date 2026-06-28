import json

from atlas_core.graph import AtlasGraph


class JSONLoader:

    def load(self, filename):

        with open(filename, "r") as f:
            data = json.load(f)

        graph = AtlasGraph()

        for evidence in data.get("evidence", []):
            graph.add_node(evidence["id"], "Evidence", **evidence)

        for assumption in data.get("assumptions", []):
            graph.add_node(assumption["id"], "Assumption", **assumption)

        for model in data.get("models", []):
            graph.add_node(model["id"], "Model", **model)

        for decision in data.get("decisions", []):
            graph.add_node(decision["id"], "Decision", **decision)

        for relationship in data.get("relationships", []):
            graph.add_edge(
                relationship["source"],
                relationship["target"],
                relationship["type"]
            )

        return graph