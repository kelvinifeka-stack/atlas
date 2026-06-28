from enum import Enum


class Relationship(str, Enum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    DEPENDS_ON = "depends_on"
    PRODUCES = "produces"
    DERIVED_FROM = "derived_from"
    REQUIRES = "requires"
    INVALIDATES = "invalidates"
    CONFIRMS = "confirms"

    @classmethod
    def all(cls):
        return [r.value for r in cls]