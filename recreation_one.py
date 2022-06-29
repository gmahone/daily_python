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
