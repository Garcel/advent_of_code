import os
import sys
from copy import copy


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        rows = []
        for line in input_file:
            rows.append([int(number) for string in line.split() for number in string])

        height_map = HeightMap(rows)

    basins = height_map.find_basins()
    basins_sizes = [len(basin) for basin in basins]
    basins_sizes = sorted(basins_sizes, reverse=True)

    print(basins_sizes[0] * basins_sizes[1] * basins_sizes[2])


class HeightMap:
    rows: [[int]]

    def __init__(self, rows):
        self.rows = copy(rows)

    def find_low_points(self) -> [int]:
        low_points = []

        for loc in self.find_low_points_locations():
            low_points.append(self.rows[loc[0], loc[1]])

        return low_points

    def find_low_points_locations(self) -> [int]:
        low_points = []

        for row_number in range(0, len(self.rows)):
            row = self.rows[row_number]

            for column_number in range(0, len(row)):
                current = row[column_number]

                top = self.rows[row_number - 1][column_number] if row_number - 1 >= 0 else None
                bottom = self.rows[row_number + 1][column_number] if row_number + 1 < len(self.rows) else None
                left = row[column_number - 1] if column_number - 1 >= 0 else None
                right = row[column_number + 1] if column_number + 1 < len(row) else None

                if self.is_lower_than(current, top) and self.is_lower_than(current, bottom) \
                        and self.is_lower_than(current, left) and self.is_lower_than(current, right):
                    low_points.append((row_number, column_number))

        return low_points

    def find_basins(self) -> [int]:
        low_points = self.find_low_points_locations()
        basins = []

        for low_point in low_points:
            current_basin = set()

            pending_locations = [low_point]

            while pending_locations:
                loc = pending_locations.pop()
                if loc in current_basin:
                    continue

                current_basin.add(loc)

                row_number = loc[0]
                column_number = loc[1]
                row = self.rows[row_number]

                current = row[column_number]

                top = self.rows[row_number - 1][column_number] if row_number - 1 >= 0 else None
                bottom = self.rows[row_number + 1][column_number] if row_number + 1 < len(self.rows) else None
                left = row[column_number - 1] if column_number - 1 >= 0 else None
                right = row[column_number + 1] if column_number + 1 < len(row) else None

                if self.is_lower_than(current, top, False) and top != 9:
                    new_loc = (row_number - 1, column_number)
                    pending_locations.append(new_loc)

                if self.is_lower_than(current, bottom, False) and bottom != 9:
                    new_loc = (row_number + 1, column_number)
                    pending_locations.append(new_loc)

                if self.is_lower_than(current, left, False) and left != 9:
                    new_loc = (row_number, column_number - 1)
                    pending_locations.append(new_loc)

                if self.is_lower_than(current, right, False) and right != 9:
                    new_loc = (row_number, column_number + 1)
                    pending_locations.append(new_loc)

            basins.append(current_basin)

        return basins

    @staticmethod
    def is_lower_than(current: int, other: int, allow_null: bool = True):
        if other is None:
            return allow_null and True

        return current < other


if __name__ == "__main__":
    main()
