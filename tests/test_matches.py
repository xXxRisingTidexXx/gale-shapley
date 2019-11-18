from pytest import raises
from gale_shapley.matches import match


def test_match():
    assert match([], []) == []
    assert match([[0]], [[0]]) == [0]
    assert match(
        [[1, 2, 3, 0], [2, 1, 0, 3], [2, 1, 3, 0], [3, 2, 0, 1]],
        [[], [], [], []]
    ) == []


def test_match_erroneous():
    with raises(RuntimeError):
        match([], [[]])
        match([[1, 2]], [[]])
        match([[1, 0], [0, 1]], [[0, 1], [0]])
