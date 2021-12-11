import io
import os
import sys

import pytest
from puzzle2 import puzzle2


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                """5483143223
                2745854711
                5264556173
                6141336146
                6357385478
                4167524645
                2176841721
                6882881134
                4846848554
                5283751526""",
                195
        )
    ])
def test_puzzle2_sample(test_input, expected):
    assert puzzle2(io.StringIO(test_input)) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                344
        )
    ])
def test_puzzle2(test_input, expected):
    assert puzzle2(test_input) == expected
