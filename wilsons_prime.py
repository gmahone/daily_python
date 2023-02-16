import math

def am_i_wilson(n):
    result = (math.factorial(n-1) + 1) / (n * n)
    return result == int(result)
