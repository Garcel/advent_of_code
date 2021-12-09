import os
import sys


def main():
    lines = []

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        points = row.split(' -> ')
        initial_point = (int(points[0].split(',')[0]), int(points[0].split(',')[1]))
        last_point = (int(points[1].split(',')[0]), int(points[1].split(',')[1]))

        lines.append(Line(initial_point, last_point))

    diagram_points = {}
    for line in lines:
        for point in line.path():
            if point in diagram_points:
                diagram_points[point] = diagram_points[point] + 1
            else:
                diagram_points[point] = 1

    point_overlapped = set()
    for diagram_point in diagram_points:
        if diagram_points.get(diagram_point) >= 2:
            point_overlapped.add(diagram_point)

    print(len(point_overlapped))


class Line:
    initial_point: (int, int)
    last_point: (int, int)

    def __init__(self, initial_point: tuple, last_point: tuple):
        self.initial_point = initial_point
        self.last_point = last_point

    def path(self):
        if self.initial_point[0] == self.last_point[0]:
            higher = self.initial_point[1] if self.initial_point[1] > self.last_point[1] else self.last_point[1]
            lower = self.initial_point[1] if self.initial_point[1] < self.last_point[1] else self.last_point[1]
            return [(self.initial_point[0], y) for y in range(lower, higher + 1)]
        elif self.initial_point[1] == self.last_point[1]:
            higher = self.initial_point[0] if self.initial_point[0] > self.last_point[0] else self.last_point[0]
            lower = self.initial_point[0] if self.initial_point[0] < self.last_point[0] else self.last_point[0]

            return [(x, self.last_point[1]) for x in range(lower, higher + 1)]
        else:
            path = []
            current_point = self.initial_point
            path.append(current_point)

            while current_point != self.last_point:
                if current_point[0] < self.last_point[0]:
                    next_x = current_point[0] + 1
                else:
                    next_x = current_point[0] - 1

                if current_point[1] < self.last_point[1]:
                    next_y = current_point[1] + 1
                else:
                    next_y = current_point[1] - 1

                current_point = (next_x, next_y)
                path.append(current_point)

            return path


if __name__ == "__main__":
    main()
