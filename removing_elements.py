def remove_every_other(my_list):
    return my_list[::2]

# other solutions

# loop based on range
def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r

# enumerate solution
def remove_every_other(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]
