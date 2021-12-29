from typing import Dict


def get_min(d: Dict[str, int]):
  """d a dict mapping letters to ints
  returns the value in d with the key that occurs first in the
  alphabet. E.g., if d = {x = 11, b = 12}, get_min returns 12."""
  lowest_key = min(*d.keys())
  return d[lowest_key]

print(get_min({'x': 11, 'b': 12}))