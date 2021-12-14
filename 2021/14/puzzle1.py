import os
import sys
import typing
from collections import Counter


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
       print(puzzle1(input_file))


def puzzle1(input_file: typing.TextIO, n_steps: int = 10):
    polymer_template = input_file.readline().strip()
    rules = {}

    for row in input_file:
        clean_row = row.strip()

        if not clean_row:
            continue

        parts = clean_row.split(' -> ')
        rules[parts[0]] = parts[1]

    polymerizer = Polymerizer(polymer_template, rules)

    for i in range(0, n_steps):
        polymerizer.apply_step()

    occurrences = polymerizer.occurrences()

    return occurrences[0][1] - occurrences[len(occurrences) - 1][1]


class Polymerizer:
    polymer: str
    steps: int
    rules: {str: str}

    def __init__(self, polymer: str, rules: {str, str}):
        self.polymer = polymer
        self.rules = rules
        self.steps = 0

    def apply_step(self):
        self.steps += 1
        result = ''

        for i in range(0, len(self.polymer) - 1):
            pair = self.polymer[i:i + 2]
            first = pair[0]
            second = pair[1]
            new_element = self.rules[pair] if pair in self.rules else ''

            result += f"{first}{new_element}{second}" if not result else f"{new_element}{second}"

        self.polymer = result

        return self.polymer

    def occurrences(self) -> [(str, int)]:
        return Counter(self.polymer).most_common()


if __name__ == "__main__":
    main()
