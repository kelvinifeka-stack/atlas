class ReportGenerator:

    def generate(self, explanation):

        lines = []

        for item in explanation:

            lines.append(
                f"{item['type']} -> {item['id']}"
            )

        return "\n".join(lines)