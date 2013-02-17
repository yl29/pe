def fib(n):
    current = 1
    after = 1
    for i in range(1, n):
        current , after = after, current + after
    return current
print  fib(12)
def p25(n):
    i = 1
    while True:
        num = fib(i)
        if len(str(num)) < n:
            i += 1
        else:
            return i
print p25(1000)