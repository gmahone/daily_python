def sum_of_minimums(numbers):
   return sum(map(min, numbers))


## can work with our without list[] call
def sum_of_minimums(numbers):
    return sum([min(rows) for rows in numbers])
