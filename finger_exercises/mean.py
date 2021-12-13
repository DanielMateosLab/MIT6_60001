import typing


def mean(num_tuple: typing.Tuple[int, ...]) -> float:
  return sum(num_tuple) / len(num_tuple)

print("Should be 4.0", mean((2, 6)))
print("Should be 1.5", mean((3, 3, 0, 0)))

