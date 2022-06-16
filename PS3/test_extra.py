from ps3 import get_letter_points, get_multiplier, update_hand
import pytest


@pytest.mark.parametrize(
    "test_input,expected", [("it", 2), ("weed", 8), ("rock", 10), ("1568", 0)]
)
def test_get_letter_points(test_input, expected):
    assert get_letter_points(test_input) == expected


@pytest.mark.parametrize("word_len,hand_len,expected", [(4, 6, 22), (2, 7, 1)])
def test_get_multiplier(word_len, hand_len, expected):
    assert get_multiplier(word_len, hand_len) == expected


@pytest.mark.parametrize(
    "hand,word,expected_hand",
    [
        ({"a": 2, "u": 1, "c": 3, "o": 1}, "launch", {"a": 1, "c": 2, "o": 1}),
        ({"e": 1, "u": 1, "c": 3, "o": 1}, "weed", {"u": 1, "c": 3, "o": 1}),
    ],
)
def test_update_hand(hand, word, expected_hand):
    assert update_hand(hand, word) == expected_hand
