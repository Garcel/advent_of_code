import os
import sys

import pytest

from puzzle2 import puzzle2


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                {'a': 14134}
        )
    ])
def test_puzzle2(test_input, expected):
    assert puzzle2(test_input)['a'] == expected['a']
