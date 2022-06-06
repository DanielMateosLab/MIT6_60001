from typing import List


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


class Fixed(Mortgage):
    """A fixed mortgage"""

    def __init__(self, loan: float, ann_rate: float, months: int) -> None:
        Mortgage.__init__(self, loan, ann_rate, months)
        self._legend = f"Fixed, {ann_rate * 100:.1f}%"


class FixedWithPts(Mortgage):
    """A fixed mortgage with points"""

    def __init__(self, loan: float, ann_rate: float, months: int, pts: float) -> None:
        Mortgage.__init__(self, loan, ann_rate, months)
        self._pts = pts
        self._paid = [loan * (pts / 100)]
        self._legend = f"Fixed, {ann_rate * 100:.1f}%, {pts:.2f} points"


class TwoRate(Mortgage):
    """A mortgage with two different interest rates"""

    def __init__(
        self,
        loan: float,
        rate: float,
        months: int,
        teaser_rate: float,
        teaser_months: int,
    ) -> None:
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._teaser_rate = teaser_rate
        self._next_rate = rate / 12
        self._legend = (
            f"{100 * teaser_rate:.1f}% for {teaser_months} months, "
            f"then {100 * rate:.1f}%"
        )

    def make_payment(self) -> None:
        if len(self._paid) == self._teaser_months + 1:
            self._rate = self._next_rate
            self._payment = find_payment(
                self._outstanding[-1], self._rate, self._months - self._teaser_months
            )

        Mortgage.make_payment(self)


def compare_mortgages(
    amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months
):
    """
    Compare different kinds of mortgages for the same amount of money for a
    specified number of years.
    """
    tot_months = years * 12
    fixed_1 = Fixed(amt, fixed_rate, tot_months)
    fixed_2 = FixedWithPts(amt, pts_rate, tot_months, pts)
    two_rate = TwoRate(amt, var_rate2, tot_months, var_rate1, var_months)

    mortgages: List[type[Mortgage]] = [fixed_1, fixed_2, two_rate]
    for m in range(tot_months):
        for mort in mortgages:
            mort.make_payment()

    for m in mortgages:
        print(m)
        print(f"\tTotal payments: {m.get_total_paid():,.0f}")


compare_mortgages(
    amt=200000,
    years=30,
    fixed_rate=0.035,
    pts=2,
    pts_rate=0.03,
    var_rate1=0.03,
    var_rate2=0.05,
    var_months=60,
)
