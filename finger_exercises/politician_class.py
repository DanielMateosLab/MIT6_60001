class Politician(Person):
    """A politician is a person who can belong to a political party"""

    def __init__(self, name, party=None):
        super().__init__(name)
        self._party = party
        """name and party are strings"""

    def get_party(self):
        """returns the party to which self belongs"""
        return self._party

    def might_agree(self, other):
        """returns True if self and other belong to the same party
        or at least one of then does not belong to a party"""
        if not isinstance(other, Politician):
            return True

        if self.get_party() is None or other.get_party() is None:
            return True

        return self.get_party() == other.get_party()
