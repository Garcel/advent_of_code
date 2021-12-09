import os
import sys


def main():

    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        print(count_floor(input_file.readline().strip()))


def count_floor(characters: [str]) -> int:
    floor = 0

    for c in characters:
        if c == '(':
            floor += 1
        else:
            floor -= 1

    return floor


if __name__ == "__main__":
    main()
