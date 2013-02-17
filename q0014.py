def gen_num(n):
    if n % 2 == 0:
        m = n/2
    else:
        m = 3*n+1
    return m

def gen_num_list(n):
    m = n
    length = 1
    while m != 1:
        m = gen_num(m)
        length += 1
    return length

def p14(n):
    max_len = 1
    max_n = 1
    for i in range(max(1,n/2), n+1):
        print i*1./n*100, "%"
        length = gen_num_list(i)
        if length > max_len:
            max_len = length
            max_n = i
    return max_n

print p14(1000000)
