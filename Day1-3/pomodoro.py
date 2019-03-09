"""
pomodoro.py

Pomodoro timer
"""

from datetime import timedelta
from time import sleep

def countdown(period_duration, period_name):
    time_remaining = period_duration
    print(f'{period_name} time remaining: {str(time_remaining)}', end='\r', flush=True)
    while time_remaining > timedelta():
        sleep(1)
        time_remaining = time_remaining - timedelta(seconds=1)
        print(f'{period_name} time remaining: {str(time_remaining)}', end='\r', flush=True)
    print()

try:
    short_break = timedelta(minutes=5)
    long_break = timedelta(minutes=15)
    work_period = timedelta(minutes=25)

    while(True):
        work_period_number = 1
        while work_period_number <= 4:
            countdown(work_period, f'Work period {work_period_number}')
            if work_period_number < 4:
                countdown(short_break, 'Break')
            else:
                countdown(long_break, 'Break')
            work_period_number += 1
except KeyboardInterrupt:
    quit()
