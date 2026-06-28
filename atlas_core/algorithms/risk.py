class RiskEngine:
    """
    Converts confidence scores into engineering risk levels.
    """

    def __init__(self, confidence):
        self.confidence = confidence

    def classify(self):

        result = {}

        for node, value in self.confidence.items():

            if value >= 0.85:
                risk = "LOW"

            elif value >= 0.60:
                risk = "MEDIUM"

            else:
                risk = "HIGH"

            result[node] = {
                "confidence": round(value, 3),
                "risk": risk,
            }

        return result