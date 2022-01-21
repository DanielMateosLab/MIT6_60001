from __future__ import annotations
from typing import List
import unittest


class Int_set(object):
  def __init__(self):
    self._vals: List[int] = []

  def add(self, elem: List[int]):
    for number in elem:
      if number not in self._vals:
        self._vals.append(number)

  def get_members(self):
    return self._vals[:]

  def union(self, other: Int_set):
    """other is an Int_set
    mutates self so that it contains exactly the elemnts in self
    plus the elements in other."""
    self._vals += other.get_members()

class Test_Int_set(unittest.TestCase):
  def test_union(self):
    set1 = Int_set()
    set1.add([1, 2])

    set2 = Int_set()
    set2.add([3, 4])

    set1.union(set2)

    self.assertEqual(set1.get_members(), [1, 2, 3, 4])