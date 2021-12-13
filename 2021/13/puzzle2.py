import os
import re
import sys
import typing
from enum import Enum
from re import Match

from typing import Set, Tuple

FOLD_INSTRUCTION_REGEX = re.compile('fold along ([xy])=([0-9]+)')


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        print(puzzle2(input_file))


def puzzle2(input_file: typing.TextIO):
    paper = Paper()

    for row in input_file:
        clean_row = row.strip()

        if not clean_row:
            break

        points = clean_row.split(',')
        paper.add(int(points[0]), int(points[1]))

    for row in input_file:
        m_fold = FOLD_INSTRUCTION_REGEX.fullmatch(row.strip())
        paper.fold(*parse_fold_instruction(m_fold))

    return paper.recognize_code()


class Axis(Enum):
    X = 0
    Y = 1


def parse_fold_instruction(match: Match) -> (Axis, int):
    axis = Axis.X if match.group(1) == 'x' else Axis.Y

    return axis, int(match.group(2))


class Paper(object):
    dots: Set[Tuple[int, int]]

    def __init__(self):
        self.dots = set()

    def add(self, x: int, y: int):
        self.dots.add((x, y))

    def fold(self, axis: Axis, position: int):
        to_remove = []
        to_append = []

        if axis == Axis.X:
            for dot in self.dots:
                if dot[0] < position:
                    continue
                elif dot[0] == position:
                    to_remove.append(dot)
                else:
                    to_remove.append(dot)
                    to_append.append((position - (dot[0] - position), dot[1]))
        else:
            for dot in self.dots:
                if dot[1] < position:
                    continue
                elif dot[1] == position:
                    to_remove.append(dot)
                else:
                    to_remove.append(dot)
                    to_append.append((dot[0], position - (dot[1] - position)))

        for dot in to_remove:
            self.dots.remove(dot)

        for dot in to_append:
            self.dots.add(dot)

    def count(self):
        return len(self.dots)

    def recognize_code(self):
        max_x = max([x for x, y in self.dots])
        max_y = max([y for x, y in self.dots])

        code = ''

        for y in range(0, max_y + 1):
            for x in range(0, max_x + 1):
                code += '#' if (x, y) in self.dots else ' '

            code += '\n'

        return code


if __name__ == "__main__":
    main()
