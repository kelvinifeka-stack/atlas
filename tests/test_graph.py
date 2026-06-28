from atlas_core.graph import AtlasGraph


def test_add_node():
    graph = AtlasGraph()

    graph.add_node("E1", "Evidence")

    assert "E1" in graph.graph.nodes


def test_add_edge():
    graph = AtlasGraph()

    graph.add_node("A", "Evidence")
    graph.add_node("B", "Decision")

    graph.add_edge("A", "B", "supports")

    assert graph.graph.has_edge("A", "B")