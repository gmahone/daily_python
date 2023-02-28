def most_frequent_item_count(collection):
    result_max = 0
    for i in collection:
        tmp_count = collection.count(i)
        if tmp_count > result_max:
            result_max = tmp_count
    return result_max
