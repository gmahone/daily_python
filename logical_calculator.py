def test_xor(arr):
    if(len(arr) > 2):
        return test_xor([arr[0] != arr[1]] + arr[2:])
    elif(len(arr) == 2):
        return arr[0] != arr[1]
    else: 
        return arr[0]

def logical_calc(array, op):
    if op == "OR":
        return any(array)
    if op == "AND":
        return all(array)
    if op == "XOR":
        return test_xor(array)
