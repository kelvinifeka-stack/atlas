from pprint import pprint

from atlas_core.graph import AtlasGraph
from atlas_core.algorithms.explain import ExplainEngine

graph = AtlasGraph()

graph.add_node(
    "PressureSurvey",
    "Evidence",
    confidence=0.95,
    description="Reservoir pressure survey"
)

graph.add_node(
    "ReservoirConnected",
    "Assumption",
    confidence=0.90
)

graph.add_node(
    "Simulation",
    "Model"
)

graph.add_node(
    "DrillWell",
    "Decision"
)

graph.add_edge(
    "PressureSurvey",
    "ReservoirConnected",
    "supports"
)

graph.add_edge(
    "ReservoirConnected",
    "Simulation",
    "used_by"
)

graph.add_edge(
    "Simulation",
    "DrillWell",
    "produces"
)

engine = ExplainEngine(graph)

pprint(engine.explain("DrillWell"))