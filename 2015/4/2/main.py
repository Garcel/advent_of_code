import hashlib
import os
import sys


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        secret_key = input_file.readline().strip()

        current = 0

        while not md5(secret_key, current).startswith('000000'):
            current += 1

        print(current)


def md5(secret_key: str, number: int) -> str:
    return hashlib.md5(f"{secret_key}{number}".encode('utf-8')).hexdigest()


if __name__ == "__main__":
    main()
