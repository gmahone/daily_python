def print_array(arr):
    for i in range(0, len(arr)):
        arr[i] = str(arr[i])
    return ",".join(arr)


# using map to str elements
def print_array(arr):
    return ','.join(map(str, arr))
