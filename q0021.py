from time import *
import math
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def process_number():
    output = 0
    outputarray = []
    tempdict = {}
    for num in range(2,10000):
        temp = 0
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                temp += i+num/i
        if not temp == 0:
            temp += 1
            if not temp == num:
                if temp not in tempdict:
                    tempdict[temp] = [num]
                else:
                    tempdict[temp].append(num)
    for index in tempdict:
        for num in tempdict[index]:
            if (num in tempdict) and (index in tempdict[num]):# and (num not in outputarray):
                outputarray.append(num)
    output = sum(outputarray)
    return output

start = clock()
print process_number()
print clock() - start, "seconds"

