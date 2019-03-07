from datetime import datetime
from datetime import date

today = datetime.today()
print(type(today))
print(today)

todaydate = date.today()
print(type(todaydate))
print(todaydate)

print(todaydate.month)
print(todaydate.day)
print(todaydate.year)

pi_day = date(2019, 3, 14)
print(pi_day)

print(pi_day - todaydate)
print((pi_day - todaydate).days)

days_until_pi = (pi_day - todaydate).days
if todaydate is pi_day:
    print(f"It's {todaydate.month}/{todaydate.day}... Happy Pi Day!")
else:
    print(f'There are {days_until_pi} days until Pi Day.')

move_date = date(2019, 3, 11)
print(f'Only {(move_date - todaydate).days} days left until our best friends move to the neighborhood!')

py2_eol = date(2020, 1, 1)
py2_days_left = (py2_eol - todaydate).days
print(f'Python 2 only has {py2_days_left} days to live.')

thisyear = todaydate.year
print(thisyear)

print(f'Today is day {(todaydate - date(2019, 1, 1)).days} of {thisyear}.')

# What time is it?
print('Time to go to sleep.')