def tower_builder(n_floors):
    floor_list = list(range(1,n_floors+1))
    asterisk_numbers = list(range(1, (n_floors*2), 2))
    pad_numbers = list(range(0,n_floors))[::-1]
    result = []
    for i in range(0,n_floors):
        left_pad = " " * pad_numbers[i]
        asterisk_pad = "*" * asterisk_numbers[i]
        right_pad = " " * pad_numbers[i]
        result.append("{}{}{}".format(left_pad, asterisk_pad, right_pad))
    return result


## solution using center
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
