import os
import sys


def main():
    total_unique_visited_houses = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        path = decode_path(row)

        total_unique_visited_houses += len(path)

    print(total_unique_visited_houses)


def decode_path(movements: [str]) -> {int, int}:
    points = set()

    x = 0
    y = 0

    for movement in movements:
        if movement == '^':
            y += 1
        elif movement == 'v':
            y -= 1
        elif movement == '<':
            x -= 1
        else:
            x += 1

        points.add((x, y))

    return points


if __name__ == "__main__":
    main()
