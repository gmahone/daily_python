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


# optimized solution in divisor search space
# get the divisors: iterate up to sqrt(n), check if the integer divides n with no remainder
# return the sum of the divisors squared.
def get_divisors_sum(n):
    divs=[1]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divs.extend([i, int(n/i)])
    divs.extend([n])
    
    # Get sum, return the sum 
    sm = sum([d**2 for d in list(set(divs))])
    return sm

# Search for squares amongst the sum of squares of divisors of numbers from m to n
def list_squared(m, n):
    out = []
    for j in range(m,n+1):
        s = get_divisors_sum(j)
        if  (s ** 0.5).is_integer():
            out.append([j, s])
    return out


## similar to previous but more compact code
def list_squared(m, n):
    out = []
    for i in range(m,n+1):
        # Finding all divisors below the square root of i
        possibles = set([x for x in range (1,int(i**0.5)+1) if i % x == 0])
        # And adding their counterpart
        possibles.update([i/x for x in possibles])
        # Doubles in the possibles are solved due to the set
        val = sum(x**2 for x in possibles)
        # Checking for exact square
        if (int(val**0.5))**2 == val: out.append([i, val])
    return out
