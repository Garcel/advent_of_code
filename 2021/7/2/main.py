import os
import sys


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        positions = [int(number) for number in input_file.readline().strip().split(',')]

    lowest_fuel_consumption = None

    for position in range(0, max(positions)):
        total_fuel = 0

        for index in range(0, len(positions)):
            crab_position = positions[index]

            fuel = sum(range(0, abs(crab_position - position) + 1))
            total_fuel += fuel

        lowest_fuel_consumption = total_fuel if lowest_fuel_consumption is None or \
                                                total_fuel < lowest_fuel_consumption else lowest_fuel_consumption

    print(lowest_fuel_consumption)


if __name__ == "__main__":
    main()
