def true_counter(arr):
    true_vals = 0
    for i in range(0, len(arr)):
        if arr[i]:
            true_vals += 1
    return true_vals



test_arr = [True, True, False, True, False, True]

print(true_counter(test_arr))
