import io
import os
import sys

import pytest
from puzzle1 import puzzle1


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
                10
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
                19
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
                226
        )
    ])
def test_puzzle1_sample(test_input, expected):
    assert puzzle1(io.StringIO(test_input)) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (
                open(os.path.join(sys.path[0], 'input'), 'r'),
                5333
        )
    ])
def test_puzzle1(test_input, expected):
    assert puzzle1(test_input) == expected
