import os
import sys


def main():
    total_unique_visited_houses = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        path = decode_path(row.strip())

        total_unique_visited_houses += len(path)

    print(total_unique_visited_houses)


def decode_path(movements: [str]) -> {int, int}:
    points = set()

    santa_x = 0
    santa_y = 0
    robot_x = 0
    robot_y = 0

    for movement_index in range(1, len(movements) + 1):
        movement = movements[movement_index - 1]

        if movement == '^':
            if is_santas_turn(movement_index):
                santa_y += 1
            else:
                robot_y += 1
        elif movement == 'v':
            if is_santas_turn(movement_index):
                santa_y -= 1
            else:
                robot_y -= 1
        elif movement == '<':
            if is_santas_turn(movement_index):
                santa_x -= 1
            else:
                robot_x -= 1
        else:
            if is_santas_turn(movement_index):
                santa_x += 1
            else:
                robot_x += 1

        points.add((santa_x, santa_y))
        points.add((robot_x, robot_y))

    return points


def is_santas_turn(movement_index: int) -> bool:
    return movement_index % 2 != 0


if __name__ == "__main__":
    main()
