import math

def new_avg(arr, newavg):
    result = newavg * (len(arr)+1) - sum(arr)
    if result < 0:
        raise ValueError
    return math.ceil(result)
