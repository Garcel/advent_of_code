import os
import sys


def main():
    h_pos = 0
    v_pos = 0
    aim = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        action, units = row.split(' ')
        units_value = int(units)

        if action == 'forward':
            h_pos = h_pos + units_value

            if aim > 0:
                v_pos = v_pos + (aim * units_value)
        elif action == 'up':
            aim = aim - units_value
        elif action == 'down':
            aim = aim + units_value

    print(h_pos * v_pos)


if __name__ == "__main__":
    main()
