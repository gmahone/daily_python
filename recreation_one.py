def find_divisors(x):
    if x == 1:
        return [1]
    else:
        result = [1];
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                result.append(i)
        result.append(x)
        return result

def square_num(x):
    return x*x

def list_squared(m, n):
    result = []
    for i in range(m, n+1):
        divisors = find_divisors(i)
        sum_squared_list = sum(map(square_num, divisors))
        sqrt_sum = sum_squared_list**0.5
        if len(divisors) == 2 and not i == 1:
            continue        
        if int(sqrt_sum) == sqrt_sum:
            result.append([i, sum_squared_list])
    return result
