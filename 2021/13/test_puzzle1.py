import io
import os
import sys

import pytest
from puzzle1 import puzzle1


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                """6,10
                0,14
                9,10
                0,3
                10,4
                4,11
                6,0
                6,12
                4,1
                0,13
                10,12
                3,4
                3,0
                8,4
                1,10
                2,14
                8,10
                9,0
                
                fold along y=7
                fold along x=5""",
                17
        )
    ])
def test_puzzle1_sample(test_input, expected):
    assert puzzle1(io.StringIO(test_input)) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                770
        )
    ])
def test_puzzle1(test_input, expected):
    assert puzzle1(test_input) == expected
