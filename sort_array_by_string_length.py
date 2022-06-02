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
    for i in arr:
        tmp_list.append({"item" : i, "length": len(i)})
    tmp_list.sort(key=extr_length)
    for i in tmp_list:
        result.append(i["item"])
    return result

# add other solutions
def sort_by_length(arr):
    return sorted(arr, key=len)

# sort key can be len() apparently
def sort_by_length(arr):
  arr.sort(key = len)
  return arr

# interesting indexing solution
def sort_by_length(arr):
    words={}
    for word in arr:
        words[int(len(word))]=word
    return [words[key] for key in sorted(words.keys())]

# lambda function solution
sort_by_length = lambda a: sorted(a, key=len)
