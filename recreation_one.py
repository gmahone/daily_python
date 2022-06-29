def find_divisors(x):
    result = [];
    for i in range(1, x+1):
        if x % i == 0:
            result.append(i)
    return result

def square_num(x):
    return x*x

def list_squared(m, n):
    result = []
    for i in range(m, n+1):
        sum_squared_list = sum(map(square_num, find_divisors(i)))
        sqrt_sum = sum_squared_list**0.5
        if int(sqrt_sum) == sqrt_sum:
            result.append([i, sum_squared_list])
    return result
