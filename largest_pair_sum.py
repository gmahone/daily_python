def largest_pair_sum(numbers): 
    sorted_list = sorted(numbers)[::-1]
    return sum(sorted_list[0:2])
