def p6(num):
    return sum(i for i in range(1, num+1))**2- sum(i**2 for i in range(1, num+1))

print p6(100)