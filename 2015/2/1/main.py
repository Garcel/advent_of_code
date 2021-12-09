import os
import sys
from copy import copy


def main():
    total_wrapping_paper = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        present = Present([int(number) for number in row.strip().split('x')])

        total_wrapping_paper += present.measure_wrapping_paper()

    print(total_wrapping_paper)


class Present:
    edges: [[int]]
    areas: [[int]]

    def __init__(self, edges):
        self.edges = copy(edges)
        self.areas = [edges[0] * edges[1], edges[0] * edges[2], edges[1] * edges[2]]

    def measure_wrapping_paper(self) -> int:
        wrapping_paper = 0
        smallest_side = None

        for area in self.areas:
            wrapping_paper += area * 2

            if smallest_side is None or smallest_side > area:
                smallest_side = area

        wrapping_paper += smallest_side

        return wrapping_paper


if __name__ == "__main__":
    main()
