import unittest


def sum_digits(s: str):
  """Assumes s is a string
  Returns the sum of the decimal digits in s
  For example, if s is 'a2b3c' it returns 5"""

class TestSumDigits(unittest.TestCase):

  def test_with_numbers_and_letters(self):
    self.assertEqual(sum_digits('a2b3'), 5)
  
  def test_with_letters(self):
    self.assertEqual(sum_digits('aaa'), 0)
  
  def test_with_numbers(self):
    self.assertEqual(sum_digits('1234'), 10)
