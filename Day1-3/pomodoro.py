"""
pomodoro.py

Pomodoro timer
"""

from datetime import datetime
from datetime import timedelta
from time import sleep

def countdown(period_duration, period_name):
    current_time = datetime.today()
    end_time = current_time + period_duration

    while current_time <= end_time:
        time_remaining = end_time - current_time
        print(f'{period_name} time remaining: {str(time_remaining)}', end='\r', flush=True)
        sleep(1)
        current_time += timedelta(seconds=1)
    print()

short_break = timedelta(seconds=5)
long_break = timedelta(seconds=10)
work_period = timedelta(seconds=15)

work_period_number = 1
while work_period_number <= 4:
    countdown(work_period, f'Work period {work_period_number}')
    if work_period_number < 4:
        countdown(short_break, 'Break')
    else:
        countdown(long_break, 'Break')
    work_period_number += 1
