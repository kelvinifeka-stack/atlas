from atlas_core.relationships import Relationship


def test_relationship_values():

    assert Relationship.SUPPORTS.value == "supports"
    assert Relationship.CONTRADICTS.value == "contradicts"
    assert Relationship.DEPENDS_ON.value == "depends_on"
    assert Relationship.PRODUCES.value == "produces"
    assert Relationship.DERIVED_FROM.value == "derived_from"
    assert Relationship.REQUIRES.value == "requires"
    assert Relationship.INVALIDATES.value == "invalidates"
    assert Relationship.CONFIRMS.value == "confirms"


def test_all_relationships():

    values = Relationship.all()

    assert "supports" in values
    assert "contradicts" in values
    assert "depends_on" in values
    assert "produces" in values
    assert "derived_from" in values
    assert "requires" in values
    assert "invalidates" in values
    assert "confirms" in values