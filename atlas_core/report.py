"""
Atlas Report Builder
"""


class ReportBuilder:
    """
    Builds a formatted engineering report.
    """

    def __init__(self):
        self.lines = []

    def title(self, text):
        self.lines.append("=" * 60)
        self.lines.append(text)
        self.lines.append("=" * 60)

    def section(self, text):
        self.lines.append("")
        self.lines.append(text)
        self.lines.append("-" * len(text))

    def line(self, text):
        self.lines.append(text)

    def blank(self):
        self.lines.append("")

    def build(self):
        return "\n".join(self.lines)


class ReportGenerator:
    """
    Legacy compatibility wrapper.
    """

    def generate(self, explanation):

        report = ReportBuilder()

        report.title("ATLAS REPORT")
        report.section("Explanation")

        for item in explanation:
            report.line(f"{item['type']} -> {item['id']}")

        return report.build()