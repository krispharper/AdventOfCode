from collections import defaultdict
from dataclasses import dataclass
from math import sqrt

from common.input_data import parse_input


@dataclass(frozen=True)
class Node:
    x: int
    y: int
    z: int

    def distance_to(self, point: "Node"):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2)


@dataclass(frozen=True)
class Edge:
    node1: Node
    node2: Node

    @property
    def distance(self):
        return self.node1.distance_to(self.node2)

    def __repr__(self) -> str:
        return f"distance: {self.distance}, point1: {self.node1}, point2: {self.node2}"

    def __str__(self) -> str:
        return repr(self)

    def __lt__(self, other: "Edge"):
        return self.distance < other.distance

    def __gt__(self, other: "Edge"):
        return self.distance > other.distance


def _main() -> None:
    input = parse_input(__file__)
    nodes = _parse_input_lines(input)
    edges = _find_edges(nodes)
    edge_map = defaultdict(list)

    def _recurse(node: Node, visited_nodes: set[Node]) -> set[Node]:
        visited_nodes.add(node)
        nodes_to_consider = [n for n in edge_map[node] if n not in visited_nodes]

        for node in nodes_to_consider:
            visited_nodes |= _recurse(node, visited_nodes)

        return visited_nodes

    for edge in edges:
        edge_map[edge.node1].append(edge.node2)
        edge_map[edge.node2].append(edge.node1)

        graph = _recurse(edges[0].node1, set())

        if len(graph) == len(nodes):
            print(edge.node1.x * edge.node2.x)
            break


def _find_edges(nodes: set[Node]) -> list[Edge]:
    results = []

    for node1_index, node1 in enumerate(list(nodes)):
        for node2_index, node2 in enumerate(nodes):
            if node2_index > node1_index:
                results.append(Edge(node1, node2))

    return sorted(results)


def _parse_input_lines(lines: list[str]) -> set[Node]:
    return {Node(*map(int, line.split(","))) for line in lines}


if __name__ == "__main__":
    _main()
