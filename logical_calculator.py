def test_xor(arr):
    print(arr)
    if(len(arr) > 2):
        return test_xor([arr[0] != arr[1]] + arr[2:])
    else:
        return arr[0] != arr[1]

def logical_calc(array, op):
    if op == "OR":
        return any(array)
    if op == "AND":
        return all(array)
    if op == "XOR":
        return test_xor(array)
