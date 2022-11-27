def sum_of_n(n):
    if n >= 0:
        index_list = list(range(0,n+1))
    else:
        index_list = list(range(n,1))[::-1]
    #return [sum(range(0,n)) for n in range(0,n)]
    print(index_list)
    result = [sum(index_list[0:n+1]) for n in index_list]
    print(result)
    pass
