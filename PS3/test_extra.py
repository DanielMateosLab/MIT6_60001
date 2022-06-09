from ps3 import get_letter_points, get_multiplier
import pytest


@pytest.mark.parametrize(
    "test_input,expected", [("it", 2), ("weed", 8), ("rock", 10), ("1568", 0)]
)
def test_get_letter_points(test_input, expected):
    assert get_letter_points(test_input) == expected


@pytest.mark.parametrize("word_len,hand_len,expected", [(4, 6, 22), (2, 7, 1)])
def test_get_multiplier(word_len, hand_len, expected):
    assert get_multiplier(word_len, hand_len) == expected
