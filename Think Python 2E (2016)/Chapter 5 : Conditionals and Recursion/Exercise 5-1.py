# The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point.
# Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

# The epoch, is the starting point against which you can measure the passage of time.
# time.time() returns the number of seconds that have passed since the epoch. The return value is a floating point number to account for fractional seconds

import time
epoch = time.time()
seconds = epoch
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
print('Seconds since the epoch: ' + str(seconds) + '\nMinutes since the epoch: ' + str(minutes) + '\nHours since the epoch: ' + str(hours) + '\nDays since the epoch: ' + str(int(days)))

hour = days % int(days) * 24
minute = hour % int(hour) * 60
second = minute % int(minute) * 60
print('Today is ' + str(int(hour)) + ' hours, ' + str(int(minute)) + ' minutes, ' + str(int(second)) + ' seconds') 


# The string representation of time, also known as a timestamp, returned by ctime() is formatted with the following structure:
# Day of the week: Mon (Monday)
# Month of the year: Feb (February)
# Day of the month: 25
# Hours, minutes, and seconds using the 24-hour clock notation: 19:11:59
# Year: 2019

today = time.ctime()
print('Today according to timestamp: ' + today)
