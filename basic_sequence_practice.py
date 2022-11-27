def sum_of_n(n):
    if n >= 0:
        index_list = list(range(0,n+1))
        result = [sum(index_list[0:n+1]) for n in index_list]
    else:
        index_list = list(range(n,1))[::-1]
        result = [sum(index_list[0:n+1]) for n in list(range(0,-n+1))]
    return result


# solution using xrange
def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]
