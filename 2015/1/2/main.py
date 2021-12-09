import os
import sys


def main():

    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        print(get_char_position_when_basement_is_reached(input_file.readline().strip()))


def get_char_position_when_basement_is_reached(characters: [str]) -> int:
    floor = 0

    for i in range(0, len(characters)):
        c = characters[i]

        if c == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return i + 1

    return 0


if __name__ == "__main__":
    main()
