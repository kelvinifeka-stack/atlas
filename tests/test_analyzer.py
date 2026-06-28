from atlas_core.graph import AtlasGraph
from atlas_core.analyzer import AtlasAnalyzer


def test_full_analysis():

    g = AtlasGraph()

    g.add_node("E1", "Evidence", confidence=0.9)
    g.add_node("A1", "Assumption")
    g.add_node("M1", "Model")
    g.add_node("D1", "Decision")

    g.add_edge("E1", "A1", "supports")
    g.add_edge("A1", "M1", "used_by")
    g.add_edge("M1", "D1", "produces")

    analyzer = AtlasAnalyzer(g)

    result = analyzer.analyze("E1", "D1")

    assert result.explanation == [
        "E1",
        "A1",
        "M1",
        "D1",
    ]

    assert "D1" in result.confidence

    assert result.impact["D1"] == 3