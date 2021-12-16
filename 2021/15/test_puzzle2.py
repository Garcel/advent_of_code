import io
import os
import sys

import pytest
from puzzle2 import puzzle2


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                """1163751742
                1381373672
                2136511328
                3694931569
                7463417111
                1319128137
                1359912421
                3125421639
                1293138521
                2311944581""",
                315
        )
    ])
def test_puzzle2_sample(test_input, expected):
    assert puzzle2(io.StringIO(test_input)) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                2831
        )
    ])
def test_puzzle2(test_input, expected):
    assert puzzle2(test_input) == expected
