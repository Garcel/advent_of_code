import os
import sys
from copy import copy


def main():
    numbers = []

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        row = row.strip()

        numbers.append(row)

    oxygen_gen_rating_values = copy(numbers)
    c02_scrubber_rating_values = copy(numbers)

    pos = 0
    while len(oxygen_gen_rating_values) > 1:
        oxygen_gen_rating_values = filter_oxygen_values(oxygen_gen_rating_values, pos)
        pos = pos + 1

    pos = 0
    while len(c02_scrubber_rating_values) > 1:
        c02_scrubber_rating_values = filter_c02_values(c02_scrubber_rating_values, pos)
        pos = pos + 1

    oxygen_gen_rating = int(oxygen_gen_rating_values[0], 2)
    c02_scrubber_rating = int(c02_scrubber_rating_values[0], 2)

    print(oxygen_gen_rating * c02_scrubber_rating)


def filter_oxygen_values(values: list, pos: int) -> list:
    new_values = []
    most_repeated_bit_at_pos = get_most_repeated_bit_at_pos(pos, values)

    for value in values:
        if int(value[pos]) != most_repeated_bit_at_pos:
            continue

        new_values.append(value)

    return new_values


def filter_c02_values(values: list, pos: int) -> list:
    new_values = []
    less_repeated_bit_at_pos = get_less_repeated_bit_at_pos(pos, values)

    for value in values:
        if int(value[pos]) != less_repeated_bit_at_pos:
            continue

        new_values.append(value)

    return new_values


def get_most_repeated_bit_at_pos(pos, values):
    count_zero = 0
    count_one = 0

    for value in values:
        if value[pos] == '0':
            count_zero += 1
        else:
            count_one += 1

    return 0 if count_zero > count_one else 1


def get_less_repeated_bit_at_pos(pos, values):
    count_zero = 0
    count_one = 0

    for value in values:
        if value[pos] == '0':
            count_zero += 1
        else:
            count_one += 1

    return 0 if count_zero <= count_one else 1


if __name__ == "__main__":
    main()
