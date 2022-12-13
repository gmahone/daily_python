def average(array):
    result = sum(array) / len(array)
    return round(result)


# less readible
def average(array):
    return round(sum(array) / len(array))

# cheating and importing mean
from statistics import mean

def average(array):
    return round(mean(array))
