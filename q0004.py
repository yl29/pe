import math

def is_palidro(num):
    num=str(num)
    return num==num[::-1]


def p4(num1, num2):
    t1 = num1
    t2 = num2
    t3 = 0
    max = 0
    while t1 >= 100 and t2 >= 100: # to ensure the 3-bit requirement
        if is_palidro(t1 * t2):
            for i in range(t1, num1+1):
                for j in range(t2, num2+1):
                    if is_palidro(i*j):
                        max = i * j
            if max == 0:
                max = t1 * t2
            return max
        elif t3 % 2 == 0:
            t1 -= 1
            t3 += 1
        elif t3 % 2 == 1:
            t2 -= 1
            t3 += 1
print p4(999,999)
