from time import *
import math
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def process_number():
    output = 0
    temp = 0
    for year in range(1900,2001):
        for month in range(1,13):
            day = 31
            if month in [9,4,6,11]:
                day = 30
            elif month == 2:
                if year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0):
                    day = 29
                else:
                    day = 28
            if  year > 1900 and (temp+1) % 7 == 0:
                output += 1
            temp += day
    return output

start = clock()
print process_number()
print clock() - start, "seconds"

