from ps3 import get_letter_points
import pytest


@pytest.mark.parametrize(
    "test_input,expected", [("it", 2), ("weed", 8), ("rock", 10), ("1568", 0)]
)
def test_get_letter_points(test_input, expected):
    assert get_letter_points(test_input) == expected
