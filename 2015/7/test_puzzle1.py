import io
import os
import sys

import pytest
from puzzle1 import puzzle1


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                """123 -> x
                456 -> y
                x AND y -> d
                x OR y -> e
                x LSHIFT 2 -> f
                y RSHIFT 2 -> g
                NOT x -> h
                NOT y -> i""",
                {'x': 123, 'y': 456, 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079}
        )
    ])
def test_puzzle1_sample(test_input, expected):
    assert puzzle1(io.StringIO(test_input)) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                {'a': 46065}
        )
    ])
def test_puzzle1(test_input, expected):
    assert puzzle1(test_input)['a'] == expected['a']
