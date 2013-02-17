from time import *
import math

def q29(start,end):
    output = 0
    outputarray = []
    for i in range(start,end+1):
        for j in range(start,end+1):
            temp = i**j
            if temp not in outputarray:
                outputarray.append(i**j)
    #print outputarray
    return len(set(outputarray))

start = clock()
print q29(2,100)
#print q29(2,5)
print clock() - start, "seconds"

