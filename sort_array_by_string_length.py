# def sort_by_length(arr):
#     pass
#
#
# test = ["Eyes", "Glasses", "Monocles", "Telescopes"]
# tmp_list = []
# result = []
# for i in test:
#     tmp_list.append({"item" : i, "length": len(i)})
#
# def extr_length(x):
#     return x["length"]
#
# tmp_list.sort(key=extr_length)
# for i in tmp_list:
#     result.append(i["item"])
#
# print(result)

def extr_length(x):
    return x["length"]

def sort_by_length(arr):
    tmp_list = []
    result = []
    for i in test:
        tmp_list.append({"item" : i, "length": len(i)})
    tmp_list.sort(key=extr_length)
    for i in tmp_list:
        result.append(i["item"])
    return result
