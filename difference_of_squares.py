def sqr(x):
    return x*x

def difference_of_squares(n):
    n_vec = list(range(1,n+1))
    squared_sum = sum(n_vec)**2
    sum_of_squares = sum(map(sqr, n_vec))
    return squared_sum - sum_of_squares


# list comprehension
def difference_of_squares(n):
    return sum(range(n+1))**2 - sum(i**2 for i in range(n+1))
