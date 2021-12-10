import os
import sys


SCORE_MAPPING = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def main():
    score = 0

    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        for line in input_file:
            try:
                NavigationSubsystemParser.check_syntax(line.strip())
            except BadSyntaxError as e:
                score += get_score(e.char)

    print(score)


def get_score(char: str) -> int:
    return SCORE_MAPPING.get(char)


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
    def check_syntax(cls, line: str):
        stack = []

        for c in line:
            if c in cls.SYNTAX_MAPPING.keys():
                stack.append(cls.SYNTAX_MAPPING.get(c))
            elif stack.pop() != c:
                raise BadSyntaxError(c)


if __name__ == "__main__":
    main()
