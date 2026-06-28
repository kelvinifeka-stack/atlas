from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class Evidence:
    statement: str
    source: str
    confidence: float

    def __post_init__(self):
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")

        self.id = str(uuid4())
        self.created = datetime.utcnow()