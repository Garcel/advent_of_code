import os
import sys
import typing


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        print(puzzle1(input_file))


def puzzle1(input_file: typing.TextIO):
    weights = [[int(num) for num in line.strip()] for line in input_file]

    caves_map = CavesMap(weights)

    return caves_map.find_path_with_lowest_risk()


class CavesMap(object):
    weights: [[int]]
    start = (int, int)
    end = (int, int)
    cost = [[int]]
    visited = [(int, int)]

    def __init__(self, weights: [[int]]):
        self.weights = list(map(list, zip(*weights)))
        self.start = (0, 0)
        self.visited = []
        self.explored = []
        self.end = (len(self.weights) - 1, len(self.weights[0]) - 1)

        self.cost = []

        for x in range(0, len(self.weights)):
            self.cost.append([])

            for y in range(0, len(self.weights[x])):
                self.cost[x].append(sys.maxsize)

        self.cost[self.start[0]][self.start[1]] = 0

    def find_path_with_lowest_risk(self) -> int:
        self.visited.append(self.start)

        while self.visited:
            current = self._get_lowest_weight_node(self.visited)
            self.explored.append(current)

            current_cost = self.cost[current[0]][current[1]]
            siblings = self._get_siblings(current)

            for sibling in siblings:
                if sibling in self.explored or sibling in self.visited:
                    continue

                self.visited.append(sibling)

                sibling_weight = current_cost + self.weights[sibling[0]][sibling[1]]

                if sibling_weight < self.cost[sibling[0]][sibling[1]]:
                    self.cost[sibling[0]][sibling[1]] = sibling_weight

        return self.cost[self.end[0]][self.end[1]]

    def _is_end(self, current: (int, int)) -> bool:
        return current == self.end

    def _get_siblings(self, current: (int, int)) -> [(int, int)]:
        top = (current[0], current[1] - 1) if current[1] - 1 >= 0 else None
        bottom = (current[0], current[1] + 1) if current[1] + 1 < len(self.weights) else None
        left = (current[0] - 1, current[1]) if current[0] - 1 >= 0 else None
        right = (current[0] + 1, current[1]) if current[0] + 1 < len(self.weights[0]) else None

        return [sibling for sibling in [bottom, right, top, left] if sibling is not None]

    def _print_path(self):
        path = ''

        for y in range(0, len(self.weights)):
            for x in range(0, len(self.weights[y])):
                path += 'X' if (x, y) in self.explored else '.'

            path += '\n'

        print(path)

    def _get_lowest_weight_node(self, visited):
        lowest = (None, sys.maxsize)

        for node in visited:
            node_cost = self.cost[node[0]][node[1]]
            if node_cost < lowest[1]:
                lowest = (node, node_cost)

        self.visited.remove(lowest[0])

        return lowest[0]


if __name__ == "__main__":
    main()
