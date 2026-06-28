from atlas_core.graph import AtlasGraph
from atlas_core.algorithms.confidence import ConfidenceEngine


def test_average_confidence():

    g = AtlasGraph()

    g.add_node("E1", "Evidence", confidence=0.8)
    g.add_node("E2", "Evidence", confidence=1.0)

    g.add_node("A1", "Assumption")

    g.add_edge("E1", "A1", "supports")
    g.add_edge("E2", "A1", "supports")

    engine = ConfidenceEngine(g)

    result = engine.compute()

    assert abs(result["A1"] - 0.9) < 1e-6