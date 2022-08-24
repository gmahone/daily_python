def tower_builder(n_floors):
    floor_list = list(range(1,n_floors+1))
    asterisk_numbers = list(range(1, (n_floors*2), 2))
    pad_numbers = list(range(0,n_floors))
    result = []
    for i in range(0,n_floors):
        result.append("{}{}{}".format(" "*pad_numbers[i], "*"*asterisk_numbers[+], " "*pad_numbers[i])
    print(pad_numbers)
    return result
