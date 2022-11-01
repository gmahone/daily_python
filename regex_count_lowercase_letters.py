def lowercase_count(strng):
    result = 0
    for i in strng:
        if i.islower():
            result += 1
    return result


# list comprehension
def lowercase_count(strng):
    return sum(a.islower() for a in strng)


# regex
import re
def lowercase_count(string):
    return len(re.findall('[a-z]',string))


# proper syntax
def lowercase_count(str):
    return sum(1 for c in str if c.islower())
