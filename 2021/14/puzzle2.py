import os
import sys
import typing


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
       print(puzzle2(input_file))


def puzzle2(input_file: typing.TextIO, n_steps: int = 10):
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

    return max(occurrences.values()) - min(occurrences.values())


class Polymerizer:
    initial_polymer: str
    polymer_pairs: {str: int}
    steps: int
    rules: {str: str}

    def __init__(self, polymer: str, rules: {str, str}):
        self.initial_polymer = polymer
        self.polymer_pairs = {}
        for i in range(0, len(polymer) - 1):
            pair = polymer[i:i + 2]
            Polymerizer._increase_dict_counter(pair, 1, self.polymer_pairs)

        self.rules = rules
        self.steps = 0

    def apply_step(self):
        self.steps += 1
        result_pairs = {}

        for k, v in self.polymer_pairs.items():
            new_element = self.rules[k]
            first_pair = f"{k[0]}{new_element}"
            second_pair = f"{new_element}{k[1]}"

            Polymerizer._increase_dict_counter(first_pair, v, result_pairs)
            Polymerizer._increase_dict_counter(second_pair, v, result_pairs)

        self.polymer_pairs = result_pairs

    def occurrences(self) -> [(str, int)]:
        occurrences = {}

        for k, v in self.polymer_pairs.items():
            Polymerizer._increase_dict_counter(k[0], v, occurrences)

        if len(self.initial_polymer) % 2 == 0:
            # correction when initial polymer is odd, add +1 to the ending char
            self._increase_dict_counter(self.initial_polymer[len(self.initial_polymer) - 1], 1, occurrences)

        return {k: v for k, v in sorted(occurrences.items(), key=lambda item: item[1], reverse=True)}

    @classmethod
    def _increase_dict_counter(cls, key: str, value: int, dict_counter: {str: int}):
        if key in dict_counter:
            dict_counter[key] += value
        else:
            dict_counter[key] = value


if __name__ == "__main__":
    main()
