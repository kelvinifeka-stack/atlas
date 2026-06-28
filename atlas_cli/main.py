import argparse

from atlas_core.io.json_loader import JSONLoader
from atlas_core.algorithms.impact import ImpactAnalyzer
from atlas_core.algorithms.confidence import ConfidenceEngine


def main():
    parser = argparse.ArgumentParser(
        prog="atlas",
        description="Atlas Engineering Reasoning Engine"
    )

    subparsers = parser.add_subparsers(dest="command")

    analyze = subparsers.add_parser(
        "analyze",
        help="Analyze a case study"
    )

    analyze.add_argument(
        "file",
        help="Path to the case study JSON file"
    )

    args = parser.parse_args()

    if args.command == "analyze":

        loader = JSONLoader()
        graph = loader.load(args.file)

        engine = ConfidenceEngine(graph)

        confidence = engine.compute()

        print("\nConfidence")

        print("----------------------")

        for node, value in sorted(confidence.items()):
            print(f"{node:<4} {value:.3f}")

        analyzer = ImpactAnalyzer(graph)

        affected = analyzer.impact_radius("E2")

        print("\nAffected Nodes:")

        for node in sorted(affected):
            print(f" - {node}")

        print("=" * 50)
        print("ATLAS ANALYSIS")
        print("=" * 50)

        print(f"\nNodes : {graph.graph.number_of_nodes()}")
        print(f"Edges : {graph.graph.number_of_edges()}")

        print("\nNode Summary")

        counts = {}

        for _, data in graph.graph.nodes(data=True):
            t = data["type"]
            counts[t] = counts.get(t, 0) + 1

        for t, c in sorted(counts.items()):
            print(f"  {t:<12} {c}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()