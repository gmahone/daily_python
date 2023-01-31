from math import prod

def max_product(lst, n_largest_elements):
    largest_elements = sorted(lst, reverse=True)[0:n_largest_elements]
    return prod(largest_elements)
