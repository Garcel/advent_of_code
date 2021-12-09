import os
import re
import sys
from copy import copy, deepcopy
from enum import Enum

INSTRUCTION_REGEX = re.compile('(turn on|toggle|turn off) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)')


def main():
    grid = LightsGrid()

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        command, start, end = parse_instruction(row.strip())

        grid.update_lights(command, start, end)

    print(grid.count_lights_on())


class Command(Enum):
    TURN_ON = 0
    TURN_OFF = 1
    TOGGLE = 2


def parse_command(command: str) -> Command:
    if command == 'turn on':
        return Command.TURN_ON
    elif command == 'turn off':
        return Command.TURN_OFF
    else:
        return Command.TOGGLE


def parse_instruction(instruction: str) -> (Command, (int, int), (int, int)):
    m = INSTRUCTION_REGEX.match(instruction)

    command = parse_command(m.group(1))
    start = (int(m.group(2)), int(m.group(3)))
    end = (int(m.group(4)), int(m.group(5)))

    return command, start, end


class LightsGrid:
    grid: [[int]]

    def __init__(self):
        self.grid = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

    def update_lights(self, command: Command, start: (int, int), end: (int, int)):
        for row_number in range(start[0], end[0] + 1):
            for column_number in range(start[1], end[1] + 1):
                if command == Command.TURN_ON:
                    self.grid[row_number][column_number] = 1
                elif command == Command.TURN_OFF:
                    self.grid[row_number][column_number] = 0
                else:
                    self.grid[row_number][column_number] = 1 if not self.grid[row_number][column_number] else 0

    def count_lights_on(self) -> int:
        return sum([sum(row) for row in self.grid])


if __name__ == "__main__":
    main()
