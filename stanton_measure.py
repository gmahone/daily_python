def stanton_measure(arr):
    unique_list = []
    max_count = 0
    for i in arr:
        for i not in unique_list:
            unique_list.append(i)
            tmp_count = arr.count(i)
            if tmp_count > max_count:
                max_count = tmp_count
    return max_count
