import io
import os
import sys

import pytest
from puzzle2 import puzzle2


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                """NNCB

                CH -> B
                HH -> N
                CB -> H
                NH -> C
                HB -> C
                HC -> B
                HN -> C
                NN -> C
                BH -> H
                NC -> B
                NB -> B
                BN -> B
                BB -> N
                BC -> B
                CC -> N
                CN -> C""",
                2188189693529
        )
    ])
def test_puzzle2_sample(test_input, expected):
    assert puzzle2(io.StringIO(test_input), 40) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                2265039461737
        )
    ])
def test_puzzle2(test_input, expected):
    assert puzzle2(test_input, 40) == expected
