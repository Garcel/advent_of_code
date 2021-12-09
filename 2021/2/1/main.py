import os
import sys


def main():
    h_pos = 0
    v_pos = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        action, units = row.split(' ')
        units_value = int(units)

        if action == 'forward':
            h_pos = h_pos + units_value
        elif action == 'up':
            v_pos = v_pos - units_value
        elif action == 'down':
            v_pos = v_pos + units_value

    print(h_pos * v_pos)


if __name__ == "__main__":
    main()
