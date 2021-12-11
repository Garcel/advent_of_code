import os
import sys
import typing


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        print(puzzle1(input_file))


def puzzle1(input_file: typing.TextIO, steps: int = 100):
    rows = []

    for row in input_file:
        rows.append([int(number) for number in row.strip()])

    grid = OctopusGrid(rows)

    for i in range(0, steps):
        grid.apply_step()

    return grid.get_flashes_count()


class OctopusGrid:
    grid: [[int]]
    flashes: int

    def __init__(self, grid: [[int]]):
        self.grid = grid
        self.flashes = 0

    def apply_step(self):
        seen = set()

        for row_number in range(0, len(self.grid)):
            for column_number in range(0, len(self.grid[row_number])):
                self._increase_octopus_energy(row_number, column_number, seen)

    def _increase_octopus_energy(self, row_number: int, column_number: int, seen: set):
        if row_number < 0 or row_number >= len(self.grid) or \
                column_number < 0 or column_number >= len(self.grid[row_number]):
            return

        position = (row_number, column_number)
        if position in seen:
            return

        self.grid[row_number][column_number] += 1

        if not self.grid[row_number][column_number] > 9:
            return

        seen.add(position)
        self._flash(row_number, column_number, seen)

    def _flash(self, row_number: int, column_number: int, seen: set):
        self.flashes += 1
        self.grid[row_number][column_number] = 0

        self._increase_octopus_energy(row_number, column_number - 1, seen)
        self._increase_octopus_energy(row_number, column_number + 1, seen)
        self._increase_octopus_energy(row_number - 1, column_number, seen)
        self._increase_octopus_energy(row_number + 1, column_number, seen)
        self._increase_octopus_energy(row_number - 1, column_number - 1, seen)
        self._increase_octopus_energy(row_number - 1, column_number + 1, seen)
        self._increase_octopus_energy(row_number + 1, column_number - 1, seen)
        self._increase_octopus_energy(row_number + 1, column_number + 1, seen)

    def get_flashes_count(self):
        return self.flashes


if __name__ == "__main__":
    main()
