import os
import sys


def main():
    previous = None
    counter = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        row_value = int(row)

        if previous is not None:
            if row_value > previous:
                counter = counter + 1

        previous = row_value

    print(counter)


if __name__ == "__main__":
    main()
