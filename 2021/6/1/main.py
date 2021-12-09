import os
import sys

DAYS = 80


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        current_state = [int(number) for number in input_file.readline().strip().split(',')]

    for _ in range(0, DAYS):
        new_state = []

        for lantern_fish in current_state:
            if lantern_fish == 0:
                new_state.append(6)
                new_state.append(8)
            else:
                new_state.append(lantern_fish - 1)

        current_state = new_state

    print(len(current_state))


if __name__ == "__main__":
    main()
