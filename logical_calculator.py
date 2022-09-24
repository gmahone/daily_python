def logical_calc(array, op):
    if len(array) > 2 and op == "XOR":
        return False
    return any(array) if op == "OR" or op == "XOR" else all(array)
