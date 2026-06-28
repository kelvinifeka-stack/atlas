from atlas_core.graph import AtlasGraph

atlas = AtlasGraph()

atlas.add_node(
    "E1",
    "Evidence",
    text="Pressure test indicates reservoir pressure is stable."
)

atlas.add_node(
    "A1",
    "Assumption",
    text="Pressure measurement is representative."
)

atlas.add_node(
    "M1",
    "Model",
    text="Reservoir simulation"
)

atlas.add_node(
    "D1",
    "Decision",
    text="Proceed with drilling."
)

atlas.add_edge("E1", "A1", "supports")
atlas.add_edge("A1", "M1", "used_by")
atlas.add_edge("M1", "D1", "produces")

atlas.show()