def fib(n):
    current = 1
    after = 1
    for i in range(0, n):
        current , after = after, current + after
    return current

def p2(num):
    sum = 0
    i = 1
    while True:
        if fib(i) <= num:
            if fib(i) % 2 == 0:
                sum += fib(i)
            i += 1
        else:
            return sum
#print p2(4000000)
