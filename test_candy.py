import pytest

import candy_chatgpt as c

grid = [
    [4,3,1,5],
    [9,15,2,7],
    [2,5,6,17],
    [11,13,4,8],
]


def test_fwd():
    assert c.max_candy(grid) == 38
