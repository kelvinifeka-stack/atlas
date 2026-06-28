from dataclasses import dataclass


@dataclass
class Assumption:

    statement: str

    reason: str

    confidence: float