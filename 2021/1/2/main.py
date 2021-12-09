import os
import sys


def main():
    second = None
    third = None
    previous_result = None
    counter = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        row_value = int(row)

        first = second
        second = third
        third = row_value
        result = first + second + third if first is not None and second is not None and third is not None else None

        if previous_result is not None:
            if result > previous_result:
                counter = counter + 1

        previous_result = result

    print(counter)


if __name__ == "__main__":
    main()
