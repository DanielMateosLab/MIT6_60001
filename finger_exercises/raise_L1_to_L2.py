from typing import List

def raise_L1_to_L2(L1: List[int], L2: List[int]):
  """L1, L2 lists of same length of numbers
  returns the sum of raising each element in L1
  to the power of the element at the same index in L2
  For example, f([1,2], [2,3]) returns 9"""
  return map(lambda base, exponent: base ** exponent, L1, L2)
