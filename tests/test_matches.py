from pytest import raises
from gale_shapley.matches import match


def test_match():
    assert match([], []) == []
    assert match([[0]], [[0]]) == [0]
    assert match([[0, 1], [0, 1]], [[0, 1], [0, 1]]) == [0, 1]
    assert match(
        [[1, 2, 3, 0], [2, 1, 0, 3], [2, 1, 3, 0], [3, 2, 0, 1]],
        [[3, 1, 0, 2], [3, 1, 0, 2], [0, 1, 2, 3], [1, 3, 0, 2]]
    ) == [2, 0, 1, 3]
    assert match(
        [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]],
        [[3, 2, 0, 1], [0, 1, 3, 2], [3, 2, 0, 1], [0, 3, 2, 1]]
    ) == [1, 3, 0, 2]


def test_match_erroneous():
    with raises(RuntimeError):
        match([], [[]])
    with raises(RuntimeError):
        match([[1, 2]], [[]])
    with raises(RuntimeError):
        match([[1, 0], [0, 1]], [[0, 1], [0]])
