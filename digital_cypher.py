def encode(message, key):
    code_string = "_abcdefghijklmnopqrstuvwxyz"
    key_cycle = list(map(int, list(str(key))))*len(message)
    result_list = []
    for i in range(0,len(message)):
        base_val = code_string.index(message[i])
        key_val = key_cycle[i]
        result_list.append(base_val + key_val)
    return result_list
