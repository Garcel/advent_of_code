import os
import sys


def main():
    bits_counter = []

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        row = row.strip()

        for pos in range(0, len(row)):
            bit = int(row[pos])

            if len(bits_counter) != len(row):
                bits_counter.append((1, 0) if bit == 0 else (0, 1))
            else:
                bits_counter[pos] = (bits_counter[pos][0] + 1, bits_counter[pos][1]) if bit == 0 else \
                    (bits_counter[pos][0], bits_counter[pos][1] + 1)

    gamma_rate = int(''.join([str(0) if x >= y else str(1) for (x, y) in bits_counter]), 2)
    epsilon_rate = int(''.join([str(0) if x <= y else str(1) for (x, y) in bits_counter]), 2)

    print(gamma_rate * epsilon_rate)


if __name__ == "__main__":
    main()
