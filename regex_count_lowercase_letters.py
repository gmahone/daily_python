def lowercase_count(strng):
    result = 0
    for i in strng:
        result += 1 if i.islower()
    return result
