from atlas_core.graph import AtlasGraph
from atlas_core.algorithms.explain import ExplanationEngine


def test_explanation_path():

    g = AtlasGraph()

    g.add_node("E1", "Evidence")
    g.add_node("A1", "Assumption")
    g.add_node("M1", "Model")
    g.add_node("D1", "Decision")

    g.add_edge("E1", "A1", "supports")
    g.add_edge("A1", "M1", "used_by")
    g.add_edge("M1", "D1", "produces")

    engine = ExplanationEngine(g)

    path = engine.explain("E1", "D1")

    assert path == ["E1", "A1", "M1", "D1"]