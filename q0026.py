from time import *
import math
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def q26(num):
    output = 0
    base = {2:0, 5:0, 7:6}
    ankeindex = 0
    tempnum = 0
    length = 0
    templength = 0
    for i in range(6,num):
        tempnum = i
        print i
        while tempnum % 2 == 0:
            tempnum /= 2
        while tempnum % 5 == 0:
            tempnum /= 5
        while tempnum % 3 == 0:
            tempnum /= 3
            templength = 1
        templength += len(set(str(1./tempnum)[2:]))
        if templength > length:
            length = templength
            ankeindex = i
            print i, templength, ankeindex
    return ankeindex

start = clock()
print q26(1000)
print clock() - start, "seconds"

