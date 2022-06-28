def find_divisors(x):
    result = [];
    for i in range(0, x+1):
        if x % i == 0:
            result.append(i)
    return result

def list_squared(m, n):
    pass
