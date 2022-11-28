def sqr(x):
    return x*x

def difference_of_squares(n):
    n_vec = list(range(1,n+1))
    print(n_vec)
    squared_sum = sum(n_vec)**2
    print(squared_sum)
    sum_of_squares = sum(map(sqr, n_vec))
    print(sum_of_squares)
    pass
