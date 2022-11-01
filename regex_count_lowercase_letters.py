def lowercase_count(strng):
    result = 0
    for i in strng:
        if i.islower():
            result += 1
    return result
