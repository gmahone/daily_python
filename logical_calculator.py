def logical_calc(array, op):
    return any(array) if op == "OR" else all(array)
