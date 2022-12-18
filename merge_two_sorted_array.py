def merge_arrays(arr1, arr2):
    unique_list = []
    concat_list = arr1 + arr2
    for i in concat_list:
        if i not in unique_list:
            unique_list.append(i)
    return sorted(unique_list)


# using set
def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))
