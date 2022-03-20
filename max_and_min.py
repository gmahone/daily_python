def minimum(arr):
    out_min = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < out_min:
            out_min = arr[i]
    return out_min


def maximum(arr):
    out_max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > out_max:
            out_max = arr[i]
    return out_max


test_arr = [4,6,2,1,9,63,-134,566]
print(minimum(test_arr))

print(maximum(test_arr))
