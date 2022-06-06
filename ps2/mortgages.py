def find_payment(loan: float, r: float, m: int) -> float:
    """
    Returns the monthly payment for a mortgage of size loan at a monthly rate
    r for m months.
    """
    return loan * (r * (1 + r) ** m) / ((1 + r) ** m - 1)


class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""

    def __init__(self, loan: float, ann_rate: float, months: int) -> None:
        """Creates a new mortgage of size loan, duration months, and annual
        rate of ann_rate"""
        self._loan = loan
        self._rate = ann_rate / 12
        self._months = months
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = None  # Description of the mortgage, will be set in subclasses

    def make_payment(self) -> None:
        """Make a payment"""
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1] * self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)

    def get_total_paid(self) -> float:
        """Return the total amount paid so far"""
        return sum(self._paid)

    def __str__(self) -> str:
        return self._legend
