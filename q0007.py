import math
def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def p7(num):
    i = 0
    zahl = 2
    while i < num:
        if is_prime(zahl):
            i += 1
            #print "i = ", i, "; Number = ",zahl
        zahl += 1
    return zahl-1


#print is_prime(4)
#print p7(10001)

prime_lst = sum([p7(i) for i in range(1, 2000000)])
print prime_lst
