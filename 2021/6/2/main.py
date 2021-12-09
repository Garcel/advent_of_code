import os
import sys

DAYS = 256


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        initial_state = [int(number) for number in input_file.readline().strip().split(',')]

        current_state = {}
        for number in initial_state:
            if number in current_state:
                current_state[number] = current_state[number] + 1
            else:
                current_state[number] = 1

    for day in range(0, DAYS):
        new_state = {}

        for lantern_fish in current_state:
            if lantern_fish == 0:
                if 6 in new_state:
                    new_state[6] = new_state[6] + current_state[lantern_fish]
                else:
                    new_state[6] = current_state[lantern_fish]

                if 8 in new_state:
                    new_state[8] = new_state[8] + current_state[lantern_fish]
                else:
                    new_state[8] = current_state[lantern_fish]
            else:
                if lantern_fish - 1 in new_state:
                    new_state[lantern_fish - 1] = new_state[lantern_fish - 1] + current_state[lantern_fish]
                else:
                    new_state[lantern_fish - 1] = current_state[lantern_fish]

        current_state = new_state

    total_lantern_fish = 0
    for lantern_fish in current_state:
        total_lantern_fish += current_state[lantern_fish]

    print(total_lantern_fish)


if __name__ == "__main__":
    main()
