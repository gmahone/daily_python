def print_array(arr):
    for i in range(0, len(arr)):
        arr[i] = str(arr[i])
    return ",".join(arr)
