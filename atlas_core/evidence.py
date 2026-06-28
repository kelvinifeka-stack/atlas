from dataclasses import dataclass
from datetime import datetime


@dataclass
class Evidence:

    statement: str

    source: str

    confidence: float

    created: datetime = datetime.utcnow()