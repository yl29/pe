from time import *
import math
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def q23():
    output = (1+23)*23/2 #~24
    abundant = []
    sum_abd = []
    for num in range(12,28124):
        temp = 0
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                temp += i+num/i
        if not temp == 0:
            temp += 1
        if temp > num:
            #print num, temp
            abundant.append(num)
    print len(abundant)


    for i in abundant:
        if i < 28123/2:
            for subindex in range(index, len(abundant)):
                if abundant[subindex] < 28123 - abundant[index]:
                    print "subindex:",subindex

    print sum_abd

    return output

start = clock()
print q23()
print clock() - start, "seconds"

