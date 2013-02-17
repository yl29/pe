import math

def process_number(num):
    temp_num = num
    num_lst = []
    fact = 0
    while temp_num > 10:
        bit = int(math.log(temp_num)/math.log(10))
        fact = temp_num/(10**bit)
        num_lst.append(fact)
        temp_num -= fact*10**bit
    if bit != 1:
        for i in range(bit):
            num_lst.append(0)
    else:
        num_lst.append(temp_num)
    return num_lst

def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

def p20(num):
    return sum(process_number(factorial(num)))

print p20(100)
#print factorial(100)
#print process_number(44300)