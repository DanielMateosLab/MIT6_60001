import calendar

def get_days_between_canadian_and_american_thanksgiving(year: int):
  """year a number >= 1941
  returns the number of days between the canadian and the american thanksgiving
  in year"""

def get_day_number_of_nth_weekday_of_month(nth: int, weekday: int, month: int, year: int):
  weeks_of_month = calendar.monthcalendar(year, month)
  first_week_has_weekday = weeks_of_month[0][weekday]

  return (first_week_has_weekday
    and weeks_of_month[nth -1][weekday]
    or weeks_of_month[nth][weekday])