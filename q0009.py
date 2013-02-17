def p9(num):
    return [a*b*(num-a-b) for a in range(1,num+1) for b in range(a,num+1) if a*a + b*b == (num-a-b)**2]

print p9(1000)