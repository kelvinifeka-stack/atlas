from dataclasses import dataclass, field


@dataclass
class AnalysisResult:
    """
    Complete result of an Atlas analysis.
    """

    confidence: dict = field(default_factory=dict)
    impact: dict = field(default_factory=dict)
    explanation: list = field(default_factory=list)

    @property
    def confidence_score(self):
        if not self.confidence:
            return 0.0

        values = list(self.confidence.values())
        return sum(values) / len(values)