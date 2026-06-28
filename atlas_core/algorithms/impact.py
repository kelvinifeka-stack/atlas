from collections import deque


class ImpactAnalyzer:
    """
    Finds every node that could be affected by a change
    starting from a given node.
    """

    def __init__(self, graph):
        self.graph = graph

    def impact_radius(self, start_node):
        """
        Returns a dictionary:
        {
            node: distance_from_start
        }
        """

        visited = {}
        queue = deque([(start_node, 0)])

        while queue:
            current, distance = queue.popleft()

            if current in visited:
                continue

            visited[current] = distance

            for neighbor in self.graph.graph.successors(current):
                queue.append((neighbor, distance + 1))

        return visited