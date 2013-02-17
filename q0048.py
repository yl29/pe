import math
def seq_quad_add(n):
    if n == 1:
        return 1
    else:
        return n**n + seq_quad_add(n-1)

def p48():
    return (seq_quad_add(999)+1000**1000) % 10000000000

print (seq_quad_add(999)+1000**1000) % 10000000000