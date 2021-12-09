import os
import sys
from copy import copy


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        rows = []
        for line in input_file:
            rows.append([int(number) for string in line.split() for number in string])

        height_map = HeightMap(rows)

    low_points = height_map.find_low_points()

    print(calculate_risk_level(low_points))


def calculate_risk_level(points: []) -> int:
    risk_level = 0

    for point in points:
        risk_level += point + 1

    return risk_level


class HeightMap:
    rows: [[int]]

    def __init__(self, rows):
        self.rows = copy(rows)

    def find_low_points(self) -> [int]:
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
                    low_points.append(current)

        return low_points

    @staticmethod
    def is_lower_than(current: int, other: int):
        if other is None:
            return True

        return current < other


if __name__ == "__main__":
    main()
