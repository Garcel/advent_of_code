import math
import os
import sys


def main():

    total_ribbon = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        present = Present([int(number) for number in row.strip().split('x')])

        total_ribbon += present.measure_ribbon()

    print(total_ribbon)


class Present:
    edges: [[int]]
    areas: [[int]]

    def __init__(self, edges):
        self.edges = sorted(edges)
        self.areas = sorted([edges[0] * edges[1], edges[0] * edges[2], edges[1] * edges[2]])
        self.volume = math.prod(edges)

    def measure_wrapping_paper(self) -> int:
        wrapping_paper = 0
        smallest_side = None

        for area in self.areas:
            wrapping_paper += area * 2

            if smallest_side is None or smallest_side > area:
                smallest_side = area

        wrapping_paper += smallest_side

        return wrapping_paper

    def measure_ribbon(self) -> int:
        return self.edges[0] * 2 + self.edges[1] * 2 + self.volume


if __name__ == "__main__":
    main()
