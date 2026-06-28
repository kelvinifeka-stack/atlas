from atlas_core.graph import AtlasGraph
from atlas_core.algorithms.impact import ImpactAnalyzer


def test_impact_analysis():

    graph = AtlasGraph()

    graph.add_node("E1", "Evidence")
    graph.add_node("A1", "Assumption")
    graph.add_node("M1", "Model")
    graph.add_node("D1", "Decision")

    graph.add_edge("E1", "A1", "supports")
    graph.add_edge("A1", "M1", "used_by")
    graph.add_edge("M1", "D1", "produces")

    analyzer = ImpactAnalyzer(graph)

    affected = analyzer.affected_nodes("A1")

    assert "M1" in affected
    assert "D1" in affected