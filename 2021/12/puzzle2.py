import os
import sys
import typing
from copy import deepcopy


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        print(puzzle2(input_file))


def puzzle2(input_file: typing.TextIO):
    edges = []

    for row in input_file:
        edges.append(parse_row(row))

    caves_map = CavesMap(edges)
    paths = caves_map.find_paths()

    return len([path for path in paths if path.contains_small_caves()])


class Node:
    name: str

    def __init__(self, name):
        self.name = name

    def is_small(self) -> bool:
        return self.name.islower()

    def is_start(self) -> bool:
        return self.name == 'start'

    def is_end(self) -> bool:
        return self.name == 'end'

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def parse_row(row: str) -> (Node, Node):
    nodes = row.strip().split('-')

    return Node(nodes[0]), Node(nodes[1])


class Path:
    nodes: [Node]
    count: {Node, int}

    def __init__(self):
        self.nodes = []
        self.count = {}

    def __str__(self):
        return str([node.name for node in self.nodes])

    def __eq__(self, other):
        return self.nodes == other.nodes

    def __hash__(self):
        return hash(tuple(self.nodes))

    def add(self, node: Node) -> bool:
        if not self.can_be_visited(node):
            return False

        if node in self.count:
            self.count[node] += 1
        else:
            self.count[node] = 1

        self.nodes.append(node)

        return True

    def pop(self):
        node = self.nodes.pop()
        self.count[node] -= 1

        return node

    def contains_small_caves(self) -> bool:
        return any([node.is_small() for node in self.nodes])

    def contains_small_cave_visited_twice(self) -> bool:
        return any([count > 1 for node, count in self.count.items() if node.is_small()])

    def can_be_visited(self, node: Node) -> bool:
        if not node.is_small():
            return True

        if (node.is_start() or node.is_end()) and node in self.nodes:
            return False

        return node not in self.nodes or not self.contains_small_cave_visited_twice()


class CavesMap:
    points: {str: Node}
    edges: {str: [Node]}

    def __init__(self, edges: (Node, Node)):
        self.edges = {}
        self.points = {}

        for edge in edges:
            self.points[edge[0].name] = edge[0]
            self.points[edge[1].name] = edge[1]

            if edge[0].name in self.edges.keys():
                self.edges[edge[0].name].append(edge[1])
            else:
                self.edges[edge[0].name] = [edge[1]]

            if edge[1].name in self.edges.keys():
                self.edges[edge[1].name].append(edge[0])
            else:
                self.edges[edge[1].name] = [edge[0]]

    def find_paths(self) -> [Path]:
        paths = set()

        start = self.points['start']

        self._find_paths(start, paths)

        return paths

    def _find_paths(self, current: Node, paths: set[Path], path: Path = None):
        if path is None:
            path = Path()

        if not path.add(current):
            return

        if current.is_end():
            paths.add(deepcopy(path))
            path.pop()
            return

        for sibling in self.edges[current.name]:
            self._find_paths(sibling, paths, path)

        path.pop()


if __name__ == "__main__":
    main()
