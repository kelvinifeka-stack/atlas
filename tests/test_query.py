from atlas_core.graph import AtlasGraph
from atlas_core.algorithms.query import QueryEngine


def test_explain_decision():

    graph = AtlasGraph()

    graph.add_node("E1", "Evidence")
    graph.add_node("A1", "Assumption")
    graph.add_node("M1", "Model")
    graph.add_node("D1", "Decision")

    graph.add_edge("E1", "A1", "supports")
    graph.add_edge("A1", "M1", "used_by")
    graph.add_edge("M1", "D1", "produces")

    engine = QueryEngine(graph)

    explanation = engine.explain_decision("D1")

    assert "E1" in explanation
    assert "A1" in explanation
    assert "M1" in explanation