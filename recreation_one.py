# passed solution
def list_squared(m, n):
    result = []
    for i in range(m, n+1):
        divisors = [1]
        if not i == 1:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    divisors.append(j)
            divisors.append(i)
        sum_squared_list = sum(number**2 for number in divisors)
        sqrt_sum = sum_squared_list**0.5
        if len(divisors) == 2 and not i == 1:
            continue        
        if int(sqrt_sum) == sqrt_sum:
            result.append([i, sum_squared_list])
    return result


## solution using a global cache
CACHE = {}

def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number] 
    
    return CACHE[number]

def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret
