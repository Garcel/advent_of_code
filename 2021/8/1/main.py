import os
import sys


def main():
    count = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        parts = row.split('|')
        output_values = parts[1].split()

        for output_value in output_values:
            if len(output_value) in [2, 3, 4, 7]:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
