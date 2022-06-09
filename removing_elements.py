def filter_odd(input: [any]):
    for i in range(0, len(input)):
        if( i % 2 ):
            return False
        else:
            return True

def remove_every_other(my_list):
    filtered_list = filter(filter_odd, my_list)
    result = []
    for x in filter_list:
        result.append(x)
    return result
