def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for i in range(a, b+1):
        index = 0
        i_sum_sq = 0
        for char in str(i):
            index += 1
            i_sum_sq += int(char)**index
        if(i == i_sum_sq):
            result.append(i)
    return result

# other solutions
def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a
def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))


def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))
def sum_dig_pow(a, b): 
    return [x for x in range(a,b + 1) if x == dig_pow(x)]

def sum_dig_pow(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]

