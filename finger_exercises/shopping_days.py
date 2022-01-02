import calendar as cal
import datetime

def shopping_days(year: int):
  """year a number >= 1941
  returns the number of days between U.S. Thanksgiving and
  Christmas in year"""
  thanksgiving_day = datetime.date(year, 11, get_thanksgiving_day_number(year))
  christmas = datetime.date(year, 12, 25)

  return (christmas - thanksgiving_day).days
  
def get_thanksgiving_day_number(year: int):
  weeks_of_november = cal.monthcalendar(year, 11)
  first_week_has_thursday = weeks_of_november[0][cal.THURSDAY] > 0

  return (first_week_has_thursday
    and weeks_of_november[3][cal.THURSDAY]
    or weeks_of_november[4][cal.THURSDAY]
  )
