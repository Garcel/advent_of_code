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
    has_double_letters = False
    has_repeated_letter_with_letter_between = False

    for i in range(0, len(word)):
        c = word[i]

        if i + 1 < len(word) and word.count(f"{c}{word[i + 1]}") > 1:
            has_double_letters = True

        if i + 1 < len(word) and i + 2 < len(word) and word[i + 2] == c:
            has_repeated_letter_with_letter_between = True

    return has_double_letters and has_repeated_letter_with_letter_between


if __name__ == "__main__":
    main()
