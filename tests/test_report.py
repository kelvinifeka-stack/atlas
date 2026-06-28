from atlas_core.services.report import ReportBuilder


def test_report_builder():

    report = ReportBuilder()

    report.title("ATLAS REPORT")

    report.section("Confidence")

    report.line("Decision D1 : 0.91")

    output = report.build()

    assert "ATLAS REPORT" in output
    assert "Confidence" in output
    assert "Decision D1 : 0.91" in output