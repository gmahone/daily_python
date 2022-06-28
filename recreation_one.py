def find_divisors(x):
    result = [];
    for i in range(1, x+1):
        if x % i == 0:
            result.append(i)
    return result

def list_squared(m, n):
    pass
