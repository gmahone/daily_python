import re

def count_smileys(arr):
    result = []
    for i in arr:
        tmp = re.findall("[:;]+[-~]?[)D]+", i)
        if len(tmp) > 0:
            result.append(tmp)
    return len(result)
