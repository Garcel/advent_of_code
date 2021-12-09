import os
import sys


def main():
    total_nice_words = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        if not is_nice(row.strip()):
            continue

        total_nice_words += 1

    print(total_nice_words)


def is_nice(word: str) -> bool:
    previous = None
    vowels_count = 0
    double_letter = False
    excluded = ['ab', 'cd', 'pq', 'xy']

    for c in word:
        if previous is not None and f"{previous}{c}" in excluded:
            return False

        if c in ['a', 'e', 'i', 'o', 'u']:
            vowels_count += 1

        if previous is not None and previous == c:
            double_letter = True

        previous = c

    return vowels_count >= 3 and double_letter


if __name__ == "__main__":
    main()
