from time import *
def p1(num):
    sum = 0
    for i in range(1,num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

start = clock()
print p1(1000)
print clock() - start, "seconds"

#print p1(1000)
