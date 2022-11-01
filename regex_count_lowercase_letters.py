def lowercase_count(strng):
    result = 0
    for i in strng:
        if i.islower():
            result += 1
    return result


# list comprehension
def lowercase_count(strng):
    return sum(a.islower() for a in strng)
