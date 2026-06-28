from atlas_core.graph import AtlasGraph
from atlas_core.algorithms.query import QueryEngine

graph = AtlasGraph()

graph.add_node(
    "PressureTest",
    "Evidence",
    text="Pressure remains stable."
)

graph.add_node(
    "ReservoirAssumption",
    "Assumption",
    text="Reservoir is hydraulically connected."
)

graph.add_node(
    "ReservoirModel",
    "Model",
    text="Simulation Model"
)

graph.add_node(
    "DrillDecision",
    "Decision",
    text="Proceed with drilling."
)

graph.add_edge(
    "PressureTest",
    "ReservoirAssumption",
    "supports"
)

graph.add_edge(
    "ReservoirAssumption",
    "ReservoirModel",
    "used_by"
)

graph.add_edge(
    "ReservoirModel",
    "DrillDecision",
    "produces"
)

engine = QueryEngine(graph)

print(engine.explain_decision("DrillDecision"))