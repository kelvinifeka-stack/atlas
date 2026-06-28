from atlas_core.algorithms.risk import RiskEngine


def test_risk_engine():

    confidence = {
        "A": 0.95,
        "B": 0.72,
        "C": 0.31,
    }

    engine = RiskEngine(confidence)

    result = engine.classify()

    assert result["A"]["risk"] == "LOW"
    assert result["B"]["risk"] == "MEDIUM"
    assert result["C"]["risk"] == "HIGH"