from atlas_core.analysis import AnalysisResult
from atlas_core.algorithms.confidence import ConfidenceEngine
from atlas_core.algorithms.impact import ImpactAnalyzer
from atlas_core.algorithms.explain import ExplanationEngine


class AtlasAnalyzer:
    """
    High-level orchestration of Atlas reasoning.
    """

    def __init__(self, graph):
        self.graph = graph

    def analyze(self, start_node, end_node):

        confidence_engine = ConfidenceEngine(self.graph)
        impact_engine = ImpactAnalyzer(self.graph)
        explanation_engine = ExplanationEngine(self.graph)

        result = AnalysisResult()

        result.confidence = confidence_engine.compute()
        result.impact = impact_engine.impact_radius(start_node)
        result.explanation = explanation_engine.explain(
            start_node,
            end_node
        )

        return result