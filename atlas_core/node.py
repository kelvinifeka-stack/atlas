from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Node:
    node_type: str
    properties: dict = field(default_factory=dict)

    def __post_init__(self):
        self.id = str(uuid4())