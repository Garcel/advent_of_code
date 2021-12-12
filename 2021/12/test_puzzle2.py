import io
import os
import sys

import pytest
from puzzle2 import puzzle2


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                """start-A
                start-b
                A-c
                A-b
                b-d
                A-end
                b-end""",
                36
        ),
        (
                """dc-end
                HN-start
                start-kj
                dc-start
                dc-HN
                LN-dc
                HN-end
                kj-sa
                kj-HN
                kj-dc""",
                103
        ),
        (
                """fs-end
                he-DX
                fs-he
                start-DX
                pj-DX
                end-zg
                zg-sl
                zg-pj
                pj-he
                RW-he
                fs-DX
                pj-RW
                zg-RW
                start-pj
                he-WI
                zg-he
                pj-fs
                start-RW""",
                3509
        )
    ])
def test_puzzle2_sample(test_input, expected):
    assert puzzle2(io.StringIO(test_input)) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                146553
        )
    ])
def test_puzzle2(test_input, expected):
    assert puzzle2(test_input) == expected
