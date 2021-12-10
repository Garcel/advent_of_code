import os
import sys


SCORE_MAPPING = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def main():
    scores = []

    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        for line in input_file:
            try:
                missing_closing_chars = NavigationSubsystemParser.check_syntax(line.strip())
                scores.append(get_score(missing_closing_chars))
            except BadSyntaxError:
                continue

    print(get_middle_score(scores))


def get_middle_score(scores: [int]) -> int:
    return sorted(scores)[int(len(scores) / 2)]


def get_score(chars: [str]) -> int:
    score = 0

    for char in chars:
        score = score * 5
        score += SCORE_MAPPING.get(char)

    return score


class BadSyntaxError(Exception):
    char: str

    def __init__(self, char):
        self.char = char


class NavigationSubsystemParser:
    SYNTAX_MAPPING = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    @classmethod
    def check_syntax(cls, line: str) -> [str]:
        stack = []

        for char in line:
            if char in cls.SYNTAX_MAPPING.keys():
                stack.append(char)
            elif cls.SYNTAX_MAPPING.get(stack.pop()) != char:
                raise BadSyntaxError(char)

        if not stack:
            return []

        stack.reverse()

        return [cls.SYNTAX_MAPPING.get(char) for char in stack]


if __name__ == "__main__":
    main()
