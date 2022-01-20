import unittest
from typing import List


def find_an_even(L: List[int]):
  """Assumes L is a list of integers
  Returns the first even number in L
  Raises ValueError if L does not contain an even number"""
  for number in L:
    if number % 2 == 0:
      return number
  
  raise ValueError("L does not contain an even number")

class Tests(unittest.TestCase):

  def test_even_is_not_first(self):
    self.assertEqual(find_an_even([1, 3, 4]), 4)

  def test_even_is_first(self):
    self.assertEqual(find_an_even([6, 3, 4]), 6)

  def test_no_even(self):
    self.assertRaises(ValueError, lambda: find_an_even([1, 3, 5, 7]))
