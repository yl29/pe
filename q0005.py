# factorize the number and save all the factors into a table
def fact(num, table):
    for i in range(2, num):
        if num % i == 0:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
            if num/i != 1:
                return fact(num/i, table)
            else:
                return table
    if num not in table:
        table[num] = 1
    else:
        table[num] += 1
    return table
# process the given list with tables as element and merge the factors with corresponding counters
def process_table(lst):
    table = {}
    for i in range(len(lst)):
        for item in lst[i]:
            if item in table:
                if table[item] < lst[i][item]:
                    table[item] = lst[i][item]
            else:
                table[item] = lst[i][item]
    return table
# core function to smallest positive number that is evenly divisible by all of the numbers from 1 to num
# keep the complexity within O(n)
def p5(num):
    result = 1
    tbl = []
    for i in range(2,num+1):
        tmp_tbl = {}
        if i == 1 or i == 2 or i == 3:
            tmp_tbl[i] = 1
            tbl.append(tmp_tbl)
        else:
            tbl.append(fact(i, tmp_tbl))
    table = process_table(tbl)
    for item in table:
        result *= item**table[item]
    return result

#print fact(8, {})
print p5(20)
#print process_table([{2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}, {3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}])