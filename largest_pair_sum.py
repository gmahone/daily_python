def largest_pair_sum(numbers): 
    sorted_list = sorted(numbers)[::-1]
    return sum(sorted_list[0:2])


## different indexing
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])


## solution which finds sequential maximums
def largest_pair_sum(numbers): 
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 + max2
