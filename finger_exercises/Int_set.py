from typing import List


class Int_set(object):
  def __init__(self):
    self._vals: List[int] = []

  def get_members(self):
    return self._vals[:]

  def union(self, other: List[int]):
    """other is an Int_set
    mutates self so that it contains exactly the elemnts in self
    plus the elements in other."""
    self._vals += other
