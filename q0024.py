from time import *
import math
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def q24(num,pos):
    output = ""
    index = 0
    temppos = pos - 1
    numlst = [i for i in range(num+1)] # prepare all the numbers
    for i in range(num+1):
        index = temppos / math.factorial(num-i)
        temppos -= index * math.factorial(num-i)
        output += str(numlst.pop(index))
    return output

start = clock()
print q24(9, 1000000)
print clock() - start, "seconds"

