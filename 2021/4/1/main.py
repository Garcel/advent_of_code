import os
import sys
from copy import copy


def main():
    bingo_numbers = []
    bingo_cards = []

    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        for line in input_file:
            if not line.strip():
                break

            bingo_numbers.extend([int(number) for number in line.split(',')])

        rows = []
        for line in input_file:
            if not line.strip():
                bingo_cards.append(BingoCard(rows))
                rows.clear()
            else:
                rows.append([int(number) for number in line.split()])
        else:
            bingo_cards.append(BingoCard(rows))
            rows.clear()

    # play
    for number in bingo_numbers:
        for card in bingo_cards:
            is_bingo, result = card.mark(number)
            if is_bingo:
                print(result)
                return


class BingoCard:
    rows: [[int]]
    marks: [[bool]]

    def __init__(self, rows):
        self.rows = copy(rows)
        self.marks = []

        for row_number in range(0, len(self.rows)):
            self.marks.append([False] * len(self.rows))

    def mark(self, number: int) -> (bool, int):
        for row_number in range(0, len(self.rows)):
            for column_number in range(0, len(self.rows)):
                if number != self.rows[row_number][column_number]:
                    continue

                self.marks[row_number][column_number] = True
                if not self.is_bingo(row_number, column_number):
                    continue

                return True, number * self.unmarked_nums_sum()

        return False, None

    def is_bingo(self, row_number: int, column_number: int):
        for column in range(0, len(self.rows[row_number])):
            if not self.marks[row_number][column]:
                break
            elif column == len(self.rows[row_number]) - 1:
                return True

        for row in range(0, len(self.rows)):
            if not self.marks[row][column_number]:
                break
            elif row == len(self.rows[column_number]) - 1:
                return True

        return False

    def unmarked_nums_sum(self) -> int:
        result = 0

        for row_number in range(0, len(self.rows)):
            for column_number in range(0, len(self.rows)):
                if not self.marks[row_number][column_number]:
                    result += self.rows[row_number][column_number]

        return result


if __name__ == "__main__":
    main()
