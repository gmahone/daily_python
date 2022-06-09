def filter_odd(input: [any]):
    for i in range(0, len(input)):
        if( i % 2 ):
            return False
        else:
            return True

def remove_every_other(my_list):
    return filter(filter_odd, my_list)
