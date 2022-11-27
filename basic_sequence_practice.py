def sum_of_n(n):
    if n >= 0:
        index_list = list(range(0,n+1))
        result = [sum(index_list[0:n+1]) for n in index_list]
    else:
        index_list = list(range(n,1))[::-1]
        result = [sum(index_list[0:n+1]) for n in list(range(0,-n+1))]
    print(index_list)
    print(result)
    return result
