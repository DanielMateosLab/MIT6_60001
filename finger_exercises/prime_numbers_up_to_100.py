print([candidate for candidate in range(2, 100) if all(candidate % potentialDivisor != 0  for potentialDivisor in range(3, candidate))])