import heapq
from collections import defaultdict
from dataclasses import dataclass
from math import prod, sqrt

from common.input_data import parse_input

LIMIT = 1000


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
        return self.distance > other.distance

    def __gt__(self, other: "Edge"):
        return self.distance < other.distance


def _main() -> None:
    input = parse_input(__file__)
    nodes = _parse_input_lines(input)
    edges = _find_edges(nodes)
    edge_map = defaultdict(list)

    for edge in edges:
        edge_map[edge.node1].append(edge.node2)
        edge_map[edge.node2].append(edge.node1)

    graphs: list[set[Node]] = []

    def _recurse(node: Node, remaining_nodes: set[Node], result: set[Node]) -> set[Node]:
        result.add(node)
        nodes_to_consider = [n for n in edge_map[node] if n in remaining_nodes]

        for node_to_consider in nodes_to_consider:
            if node_to_consider in remaining_nodes:
                remaining_nodes.remove(node_to_consider)

            result |= _recurse(node_to_consider, remaining_nodes, result)

        return result

    while nodes:
        node = nodes.pop()
        subgraph = _recurse(node, nodes, set())
        graphs.append(subgraph)

    graphs = sorted(graphs, key=lambda g: len(g), reverse=True)

    print(prod(len(graph) for graph in graphs[:3]))


def _find_edges(nodes: set[Node]) -> list[Edge]:
    results = []

    def add_distance(edge) -> None:
        if len(results) < LIMIT:
            heapq.heappush(results, edge)
        elif edge > results[0]:
            heapq.heapreplace(results, edge)

    for node1_index, node1 in enumerate(list(nodes)):
        for node2_index, node2 in enumerate(nodes):
            if node2_index > node1_index:
                edge = Edge(node1, node2)
                add_distance(edge)

    return sorted(results, reverse=True)


def _parse_input_lines(lines: list[str]) -> set[Node]:
    return {Node(*map(int, line.split(","))) for line in lines}


if __name__ == "__main__":
    _main()
