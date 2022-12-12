import math

def new_avg(arr, newavg):
    result = newavg * (len(arr)+1) - sum(arr)
    if result < 0:
        raise ValueError
    return math.ceil(result)


# import only ceil
from math import ceil

def new_avg(arr, newavg):
    value = int(ceil((len(arr)+1) * newavg - sum(arr)))
    if value < 0:
        raise ValueError
    return value
