def largest_pair_sum(numbers): 
    sorted_list = sorted(numbers)[::-1]
    return sum(sorted_list[0:2])


## different indexing
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])
