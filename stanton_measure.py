# this works for what it should do
# but this is not what the question asks...
def stanton_measure(arr):
    unique_list = []
    max_count = 0
    for i in arr:
        if i not in unique_list:
            unique_list.append(i)
            tmp_count = arr.count(i)
            if tmp_count > max_count:
                max_count = tmp_count
    return max_count

# this is to actually solve the problem
def stanton_measure(arr):
    one_count = arr.count(1)
    n_count = arr.count(one_count)
    return n_count
