import typing

def find_last(s: str, sub: str) ->  typing.Union[None, int]:
  """s and sub are non-empty strings
  Returns the index of the last occurrence of sub in s.
  Returns None if sub does not occur in s"""
  last_result_index: typing.Union[None, int] = None

  def get_search_start_index():
    if last_result_index == None:
      return None
    else:
      return last_result_index + len(sub)

  while sub in s[get_search_start_index():]:
    last_result_index = s.find(
      sub,
      get_search_start_index())

  return last_result_index

print("Should be 4:", find_last("lolol", "l"))
print("Should be 2:", find_last("aabbcc", "bb"))
