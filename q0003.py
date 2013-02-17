import math

def p3(num):
    anchor = 1
    number = num
    while True:
        if number % anchor == 0 and number == anchor:
            return anchor
        elif number % anchor == 0 and number != anchor:
            number /= anchor
        anchor += 1
print p3(600851475143)