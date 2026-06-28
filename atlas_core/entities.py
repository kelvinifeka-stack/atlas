from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Entity:
    """
    Something that exists in the domain.
    """

    name: str
    description: str = ""

    def __post_init__(self):
        self.id = str(uuid4())